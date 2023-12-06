from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia

from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, QCoreApplication, QRunnable, QThreadPool, Signal


import cv2
import glob
import numpy
import sys
import importlib
import os
import re
import maya.cmds as cmds


dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, dir_path)

import VideoPlayer as VideoPlayer

try:
    importlib.reload(VideoPlayer)
    import maya.OpenMayaUI as omui
    import shiboken2

except:
    pass

path = 'C:/Users/derek/Desktop/Video Testing/images/output.#.png'
firstImage = 'C:/Users/derek/Desktop/Video Testing/images/output.0001.png'
projectPath = 'C:/Users/derek/Desktop/Video Testing/'


'''
Main Window Class controls the main functionality
'''
class MainWindow(QtWidgets.QMainWindow):
    progress = Signal(int)
    range = Signal(int)
    finished = Signal()
    def __init__(self, path, firstImage, projectPath, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = VideoPlayer.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.media = QtMultimedia.QMediaPlayer(self)
        self.ui.media.setVideoOutput(self.ui.mediaPlayer)
        self.ui.media.mediaStatusChanged.connect(self.videoEnded)

        # path = cmds.renderSettings(genericFrameImageName="#",fullPath=True)[0]
        # firstImage = cmds.renderSettings(firstImageName=True, fullPath=True)[0]

        self.projectPath = projectPath
        self.regex, displayPath, frameCount = findFiles(path)
        self.configureLabels(firstImage, displayPath, frameCount)


        # Async video builder setup
        self.threadpool = QThreadPool()

        self.ui.generateButton.clicked.connect(self.buildVideo)

        # Setup Slider before loading media
        self.setupSlider()

        self.mediaLoaded = False
        self.mediaPlaying = False

        self.loadPausePlayIcons()
        self.ui.progressBar.setHidden(True)

        # Video Generation Signals
        self.progress.connect(lambda value: self.ui.progressBar.setValue(value))
        self.range.connect(lambda value: self.ui.progressBar.setMaximum(value))
        self.finished.connect(lambda: self.loadMedia(os.path.join(self.projectPath, "movies", self.ui.lineEdit.text())))

        # Configure event handlers for control buttons
        self.ui.pausePlayButton.clicked.connect(self.pausePlay)
        self.ui.stopButton.clicked.connect(self.ui.media.stop)
        self.ui.backButton.clicked.connect(lambda: self.ui.media.setPosition(0))
        self.ui.forwardButton.clicked.connect(
            lambda: self.ui.media.setPosition(self.ui.media.duration())
        )

        self.setupSlider
    
    # Load a video into the media player and make it visible
    def loadMedia(self, fileName):
        self.ui.progressBar.setHidden(True)
        url = QtCore.QUrl.fromLocalFile(fileName)
        print(fileName)
        self.ui.media.setMedia(QtMultimedia.QMediaContent(None))
        self.ui.media.setMedia(QtMultimedia.QMediaContent(url))
        self.ui.mediaPlayer.show()
        self.mediaLoaded = True

        self.pausePlay()

    # Grab image resources for the pause and play buttons
    def loadPausePlayIcons(self):
        self.playIcon = QIcon()
        self.playIcon.addFile(u":/controls/images/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseIcon = QIcon()
        self.pauseIcon.addFile(u":/controls/images/pause.svg", QSize(), QIcon.Normal, QIcon.Off)

    # Configure Scrub Bar
    def setupSlider(self):
        # Make video duration and slider range equal
        self.ui.media.durationChanged.connect(
            lambda duration: self.ui.timeSlider.setRange(0, duration)
        )

        # Make the scrub bar move with the video
        self.ui.media.positionChanged.connect(
            lambda position: self.ui.timeSlider.setValue(position)
        )

        self.ui.timeSlider.sliderMoved.connect(
            lambda position: self.ui.media.setPosition(position)
        )


    def pausePlay(self):
        if self.mediaLoaded:
            if not self.mediaPlaying:
                self.ui.media.play()
                self.ui.pausePlayButton.setIcon(self.pauseIcon)
            else:
                self.ui.media.pause()
                self.ui.pausePlayButton.setIcon(self.playIcon)

            self.mediaPlaying = not self.mediaPlaying
        else:
            pass # do nothing for now

    def configureLabels(self, imagePath, genericPath, frameCount):
        try:
            self.ui.generateButton.setHidden(False)
            pixmap = QtGui.QPixmap(imagePath)
            self.ui.sampleImage.setPixmap(pixmap)    
            self.ui.sampleImage.show()
            self.ui.fileNameTitle.setText(QCoreApplication.translate("MainWindow", u"Sequence Name: {}".format(genericPath), None))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Frames: {}".format(frameCount), None))
        except FileNotFoundError:
            self.ui.generateButton.setHidden(True)
            self.ui.sampleImage.setText("File Sequence Not Found!")
    
    def buildVideo(self):
        self.ui.progressBar.setHidden(False)
        
        worker = VideoBuilder(self.regex, self.ui.lineEdit.text(), self.ui.spinBox.value(), self.progress, self.range, self.finished, self.projectPath)
        self.threadpool.start(worker)

    def videoEnded(self, status):
        if status == QtMultimedia.QMediaPlayer.EndOfMedia:
            self.ui.pausePlayButton.setIcon(self.playIcon)
            self.mediaPlaying = False


'''
Contains the QThread that launches to create the video file
''' 
class VideoBuilder(QRunnable):
    def __init__(self, framePath, outputPath, frameRate, progress, range, finished, projectPath):
        super(VideoBuilder, self).__init__()
        self.framePath = framePath
        self.outputPath = outputPath    
        self.progress = progress
        self.range = range
        self.finished = finished  
        self.frameRate = frameRate
        self.projectPath = projectPath

    # Async Thread (Converts files to videos)
    def run(self):
               
        fullPath = os.path.join(projectPath, "movies", self.outputPath)

        files = glob.glob(self.framePath)
        self.range.emit(len(files) * 2)
        step = 0

        img_array = []
        for filename in files:
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
            step += 1
            self.progress.emit(step)

        if len(img_array) == 0:
            print("No Images Found")
            return 
        
        if os.path.isfile(fullPath):
            os.remove(fullPath)

        # Example used AVI format
        out = cv2.VideoWriter(fullPath, cv2.VideoWriter_fourcc(*'DIVX'), self.frameRate, size)
        
        for i in range(len(img_array)):
            out.write(img_array[i])
            step += 1
            self.progress.emit(step)
        out.release()
        self.finished.emit()


'''
 Other Functions
'''
# Takes in generic name from Maya command call, creates a regex and also a display name
def findFiles(imageGenericName):
    buildRegex = imageGenericName.replace("#","[0-9]*")
    displayName = os.path.basename(imageGenericName)

    # Get Frame Count
    searchRegex = os.path.basename(imageGenericName)
    searchRegex = searchRegex.replace("#",r"([0-9]+)")
    searchRegex = searchRegex.replace(".", r"\.")


    folder = os.path.dirname(imageGenericName)
    searchRegex = re.compile(searchRegex)
    files = [file for file in os.listdir(folder) if searchRegex.match(file)]
    if len(files) > 0:
        files.sort()
        last = files[-1]
        match = searchRegex.match(last)
        frameNumber = int(match.group(1))
    else:
        frameNumber = 0


    return buildRegex, displayName, frameNumber



def getMayaWindow():
    # type: () -> shiboken2.wrapInstance()
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """

    pointer = omui.MQtUtil.mainWindow()
    if pointer is not None:
        return shiboken2.wrapInstance(int(pointer), QtWidgets.QWidget)
    
def runInMaya(path, firstImage, projectPath):
    mainWindow = MainWindow(path, firstImage, projectPath, getMayaWindow())
    mainWindow.show()

def runStandAlone(path, firstImage, projectPath):
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow(path, firstImage, projectPath)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #runInMaya(path, firstImage)
    runStandAlone(path, firstImage, projectPath)