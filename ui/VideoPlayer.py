# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Maya Video Player.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QVideoWidget

import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(714, 736)
        MainWindow.setStyleSheet(u"background-color:#444444;")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mediaPlayer = QVideoWidget(self.centralwidget)
        self.mediaPlayer.setObjectName(u"mediaPlayer")
        self.mediaPlayer.setStyleSheet(u"background-color: #373737;")

        self.verticalLayout.addWidget(self.mediaPlayer)

        self.timeSlider = QSlider(self.centralwidget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setStyleSheet(u"")
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.timeSlider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(120, -1, 120, -1)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setStyleSheet(u"background-color:#5d5d5d;")
        icon = QIcon()
        icon.addFile(u":/controls/images/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(30, 30))
        self.backButton.setFlat(False)

        self.horizontalLayout.addWidget(self.backButton)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setStyleSheet(u"background-color:#5d5d5d;")
        icon1 = QIcon()
        icon1.addFile(u":/controls/images/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.stopButton)

        self.pausePlayButton = QPushButton(self.centralwidget)
        self.pausePlayButton.setObjectName(u"pausePlayButton")
        self.pausePlayButton.setAutoFillBackground(False)
        self.pausePlayButton.setStyleSheet(u"background-color:#5d5d5d;")
        icon2 = QIcon()
        icon2.addFile(u":/controls/images/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pausePlayButton.setIcon(icon2)
        self.pausePlayButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pausePlayButton)

        self.forwardButton = QPushButton(self.centralwidget)
        self.forwardButton.setObjectName(u"forwardButton")
        self.forwardButton.setStyleSheet(u"background-color:#5d5d5d;")
        icon3 = QIcon()
        icon3.addFile(u":/controls/images/forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.forwardButton.setIcon(icon3)
        self.forwardButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.forwardButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.sampleImage = QLabel(self.centralwidget)
        self.sampleImage.setObjectName(u"sampleImage")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleImage.sizePolicy().hasHeightForWidth())
        self.sampleImage.setSizePolicy(sizePolicy)
        self.sampleImage.setStyleSheet(u"color:#eb820b;")
        self.sampleImage.setFrameShape(QFrame.NoFrame)
        self.sampleImage.setScaledContents(True)
        self.sampleImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.sampleImage)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fileNameTitle = QLabel(self.centralwidget)
        self.fileNameTitle.setObjectName(u"fileNameTitle")
        self.fileNameTitle.setStyleSheet(u"color:#eb820b;")

        self.verticalLayout_3.addWidget(self.fileNameTitle)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:#eb820b;")

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setStyleSheet(u"color:#eb820b;")

        self.horizontalLayout_3.addWidget(self.outputLabel)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"color:#eb820b;\n"
"background-color:#5d5d5d;")
        self.lineEdit.setMaxLength(32769)
        self.lineEdit.setFrame(False)

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frameRateLabel = QLabel(self.centralwidget)
        self.frameRateLabel.setObjectName(u"frameRateLabel")
        self.frameRateLabel.setStyleSheet(u"color:#eb820b;")

        self.horizontalLayout_4.addWidget(self.frameRateLabel)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"color:#eb820b;\n"
"background-color:#5d5d5d;")
        self.spinBox.setFrame(False)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(144)
        self.spinBox.setValue(24)

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy1)
        self.generateButton.setStyleSheet(u"color:#eb820b;\n"
"background-color:#5d5d5d;")

        self.horizontalLayout_2.addWidget(self.generateButton)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setStyleSheet(u"color:#eb820b;")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 714, 26))
        self.menubar.setStyleSheet(u"QMenuBar{\n"
"	color:white;\n"
"}\n"
"QMenuBar:selected{\n"
"	color:black;\n"
"}\n"
"QMenu{\n"
"	color:white;\n"
"}\n"
"QMenu:selected{\n"
"	color:#FF8800;\n"
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionOpen_2)

        self.retranslateUi(MainWindow)

        self.backButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.backButton.setText("")
        self.stopButton.setText("")
        self.pausePlayButton.setText("")
#if QT_CONFIG(shortcut)
        self.pausePlayButton.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.forwardButton.setText("")
        self.sampleImage.setText(QCoreApplication.translate("MainWindow", u"No Image Sequence Found!", None))
        self.fileNameTitle.setText(QCoreApplication.translate("MainWindow", u"Sequence Name: file.###.png", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Frames: ###", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output File Name:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"output.avi", None))
        self.frameRateLabel.setText(QCoreApplication.translate("MainWindow", u"Frame Rate (FPS):", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate Video File", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

