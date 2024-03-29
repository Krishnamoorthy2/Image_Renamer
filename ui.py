# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(852, 445)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(220, 6, 6);")
        # MainWindow.setStyleSheet("background-color: rgb(0, 0, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CSV_Renamer = QtWidgets.QLabel(self.centralwidget)
        self.CSV_Renamer.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.CSV_Renamer.setFont(font)
        self.CSV_Renamer.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.CSV_Renamer.setObjectName("CSV_Renamer")
        self.gridLayout.addWidget(self.CSV_Renamer, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(25)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CSV_FilePath = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CSV_FilePath.sizePolicy().hasHeightForWidth())
        self.CSV_FilePath.setSizePolicy(sizePolicy)
        self.CSV_FilePath.setMaximumSize(QtCore.QSize(557, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CSV_FilePath.setFont(font)
        self.CSV_FilePath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.CSV_FilePath.setObjectName("CSV_FilePath")
        self.gridLayout_4.addWidget(self.CSV_FilePath, 0, 1, 1, 1)
        self.csv_inpu = QtWidgets.QLabel(self.centralwidget)
        self.csv_inpu.setMaximumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.csv_inpu.setFont(font)
        self.csv_inpu.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.csv_inpu.setObjectName("csv_inpu")
        self.gridLayout_4.addWidget(self.csv_inpu, 0, 0, 1, 1)
        self.csv = QtWidgets.QPushButton(self.centralwidget)
        self.csv.setMaximumSize(QtCore.QSize(71, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.csv.setFont(font)
        self.csv.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.971591, y2:0.227, stop:0 rgba(196, 196, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px\n"
"\n"
"\n"
"\n"
"")
        self.csv.setObjectName("csv")
        self.gridLayout_4.addWidget(self.csv, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 5, 0, 5)
        self.gridLayout_3.setHorizontalSpacing(25)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(557, 41))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border:none;")
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.lang = QtWidgets.QLabel(self.centralwidget)
        self.lang.setMaximumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lang.setFont(font)
        self.lang.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.lang.setObjectName("lang")
        self.gridLayout_3.addWidget(self.lang, 0, 0, 1, 1)
        self.submit_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_2.sizePolicy().hasHeightForWidth())
        self.submit_2.setSizePolicy(sizePolicy)
        self.submit_2.setMaximumSize(QtCore.QSize(71, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.submit_2.setFont(font)
        self.submit_2.setStyleSheet("background-color: transparent;")
        self.submit_2.setObjectName("submit_2")
        self.gridLayout_3.addWidget(self.submit_2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(25)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Image_FilePath = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_FilePath.sizePolicy().hasHeightForWidth())
        self.Image_FilePath.setSizePolicy(sizePolicy)
        self.Image_FilePath.setMaximumSize(QtCore.QSize(557, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Image_FilePath.setFont(font)
        self.Image_FilePath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border:none;")
        self.Image_FilePath.setObjectName("Image_FilePath")
        self.gridLayout_2.addWidget(self.Image_FilePath, 0, 1, 1, 1)
        self.renders = QtWidgets.QLabel(self.centralwidget)
        self.renders.setMaximumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.renders.setFont(font)
        self.renders.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.renders.setObjectName("renders")
        self.gridLayout_2.addWidget(self.renders, 0, 0, 1, 1)
        self.image_choose = QtWidgets.QPushButton(self.centralwidget)
        self.image_choose.setMaximumSize(QtCore.QSize(71, 41))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.image_choose.setFont(font)
        self.image_choose.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.971591, y2:0.227, stop:0 rgba(196, 196, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px\n"
"\n"
"")
        self.image_choose.setObjectName("image_choose")
        self.gridLayout_2.addWidget(self.image_choose, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMaximumSize(QtCore.QSize(239, 43))
        font = QtGui.QFont()
        font.setFamily("BebasNeue Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.971591, y2:0.227, stop:0 rgba(196, 196, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px\n"
"\n"
"")
        self.submit.setObjectName("submit")
        self.gridLayout_5.addWidget(self.submit, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.msg = QtWidgets.QTextEdit(self.centralwidget)
        self.msg.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.msg.setObjectName("msg")
        self.verticalLayout.addWidget(self.msg)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Rename = QtWidgets.QAction(MainWindow)
        self.action_Rename.setObjectName("action_Rename")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CSV_Renamer.setText(_translate("MainWindow", "CSV RENMANER Ver1.0"))
        self.CSV_FilePath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'BebasNeue Bold\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.csv_inpu.setText(_translate("MainWindow", "CSV :                        "))
        self.csv.setText(_translate("MainWindow", "..."))
        self.lang.setText(_translate("MainWindow", "LANGUAGES :    "))
        self.submit_2.setText(_translate("MainWindow", "..."))
        self.Image_FilePath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'BebasNeue Bold\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.renders.setText(_translate("MainWindow", "RENDERS :             "))
        self.image_choose.setText(_translate("MainWindow", "..."))
        self.submit.setText(_translate("MainWindow", "RENAME IT!"))
        self.msg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'BebasNeue Bold\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.action_Rename.setText(_translate("MainWindow", "&Csv_Renamer"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
