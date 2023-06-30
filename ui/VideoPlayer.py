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

import ui.resources_rc as resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(717, 600)
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 717, 26))
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
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

