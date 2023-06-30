from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia

from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

import cv2
import glob
import numpy
import sys
import importlib

import ui.VideoPlayer as VideoPlayer

try:
    importlib.reload(VideoPlayer)
    import maya.OpenMayaUI as omui
    import shiboken2

except:
    pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = VideoPlayer.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.media = QtMultimedia.QMediaPlayer(self)
        self.ui.media.setVideoOutput(self.ui.mediaPlayer)

        buildVideo('C:\\Users\\derek\\Desktop\\Video Testing\\images\\output.*.png', 'output.avi')

        # Setup Slider before loading media
        self.setupSlider()

        #TODO: change this to do something useful
        self.loadMedia("output.avi")
        self.mediaPlaying = False

        self.loadPausePlayIcons()

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
        url = QtCore.QUrl.fromLocalFile(fileName)
        self.ui.media.setMedia(QtMultimedia.QMediaContent(url))
        self.ui.mediaPlayer.show()

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
        if not self.mediaPlaying:
            self.ui.media.play()
            self.ui.pausePlayButton.setIcon(self.pauseIcon)
        else:
            self.ui.media.pause()
            self.ui.pausePlayButton.setIcon(self.playIcon)

        self.mediaPlaying = not self.mediaPlaying


# Takes a sequence of frames and converts it to a video file
def buildVideo(framePath, outputPath):
    img_array = []
    for filename in glob.glob(framePath):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    # Example used AVI format
    out = cv2.VideoWriter(outputPath, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()



def getMayaWindow():
    # type: () -> shiboken2.wrapInstance()
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """

    pointer = omui.MQtUtil.mainWindow()
    if pointer is not None:
        return shiboken2.wrapInstance(int(pointer), QtWidgets.QWidget)
    
def runInMaya():
    mainWindow = MainWindow(getMayaWindow())
    mainWindow.show()

def runStandAlone():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #runInMaya()
    runStandAlone()