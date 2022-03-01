from lib2to3.pytree import LeafPattern
import os, shutil
import csv
import re
from unittest import skip
import imagesize
import sys, datetime, glob, threading, time

from PyQt5 import QtCore, QtGui, QtWidgets


from ui import Ui_MainWindow

class Image_Renamer(QtWidgets.QMainWindow):
    def __init__(self):
        super(Image_Renamer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.CSV_Renamer.clicked.connect()
        self.ui.csv.clicked.connect(self.CSV_file)
        self.ui.image_choose.clicked.connect(self.Image_file)
        # self.ui.pushButton.clicked.connect(self.get_language)
        self.ui.submit.clicked.connect(self.Change)
        # timer = Qtimer
        # self.kill_me = True
        # self.thread = threading.Thread(target =self.date_time,  args =(lambda : self.kill_me, ))
        # self.thread.start()
        self.ui.actionExit.triggered.connect(self.closeEvent)
    # def thread(self):
    #     T1 = threading.Thread(target =self.Change)
        
    #     T1.setDaemon(True)
    #     # T2.setDaemon(True)
    #     T1.start()
        # T2.start()
    def CSV_file(self):
        filename, check  = QtWidgets.QFileDialog.getOpenFileName(None, "Choose CSV File",
                                               "", "Python Files (*.csv);;All Files (*)")
        if check:
            print(filename.replace("/", "\\"))
        # filename = filename.replace("/", "\\")
        self.ui.CSV_FilePath.setText(filename)
        self.get_language()
        return filename
    def Image_file(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Image Folder")
        # if check:
        #     print(filename)
        Image_FilePath = self.ui.Image_FilePath.setText(filename)
        filename = filename.replace("/", '\\')
        return Image_FilePath
    def date_time(self, args):
        try:
                
            while True:
                now = datetime.datetime.now()
                self.date = now.strftime("%m/%d/%Y")
                self.times = now.strftime("%H:%M:%S")
                self.ui.Date.setText(self.date)
                self.ui.Time.setText(self.times)
                time.sleep(1)
        except Exception as e:
            pass
    def get_language(self):
        language = []
        csv_path = self.ui.CSV_FilePath.toPlainText()
        with open(csv_path, 'r') as f:
            lines = csv.reader(f, delimiter = '.')
            for line in lines:
                name = line[0].split('_')[-1]
                if "name" in name:
                    print("name", name)
                elif not language:
                    language.append(name)
                elif name not in language:
                    language.append(name)
                elif ('ALL' not in language) and  (len(language) > 1):
                    language.insert(0, 'ALL')
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(language)
            
    def Change(self):
        # try:

        csv_file, image = self.ui.CSV_FilePath.toPlainText(), self.ui.Image_FilePath.toPlainText()
        # print(csv_file, image)
        dir_path = f"{image}_Renamed"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # shutil.copytree(image, f"{image}_Renamed")

        
        with open(csv_file, 'r') as f:
            lines = csv.reader(f, delimiter = '.')
            select_lang = self.ui.comboBox.currentText()
            print(image)

            if not glob.glob(os.path.join(image, "*.jpg")):
                print("HI")
                self.ui.msg.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'BebasNeue Bold\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No Images</p></body></html>")
                os.rmdir(f"{dir_path}")
            else:
                for line in lines:
                    if select_lang == "ALL": 
                        self.ConditionCheck(image, dir_path, line)

                    elif line[0].split('_')[-1] == select_lang:
                        self.ConditionCheck(image, dir_path, line)
                    # for line in lines:
                    #     current_file_path = line[0]
                        
                    #     if "name" in current_file_path:
                    #         pass
                    #     else:
                    #         lang_dir = f"{dir_path}/{line[0].split('_')[-1]}"
                    #         if not os.path.exists(lang_dir):
                    #             os.makedirs(lang_dir)
                    #         for (jpgfile) in glob.iglob(os.path.join(image, "*.jpg")):
                    #             print("jpgfile", jpgfile)
                    #         for (root, dirs, file) in os.walk(image):
                    #             for f in file:
                    #                 if '.jpg' in f:
                    #                     print("Filename", file)
                    #                     shutil.copy2(os.path.join(image,f), dir_path)
                    #                     width, height = imagesize.get(f"{dir_path}\{f}")      

                    #                     filesize = f"{width}x{height}"
                    #                     regex = re.compile(filesize)
                                        
                    #                     print(filesize, regex)
                    #                     if os.path.isfile(f"{lang_dir}/{current_file_path}.jpg"):pass    
                    #                     elif regex.findall(current_file_path):
                    #                         os.rename(f"{dir_path}/{f}", f"{lang_dir}/{current_file_path}.jpg")
                removing_files = os.listdir(dir_path) 
                filtered_files = [file for file in removing_files if file.endswith(".jpg")]
                for i in filtered_files:
                    path_to_file  = os.path.join(dir_path, i)
                    os.remove(path_to_file)
                
                self.ui.msg.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'BebasNeue Bold\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Successfully Converted</p></body></html>")
                shutil.rmtree(image)
                os.rename(f"{dir_path}", f"{image}")
                print("I'm Happy")
            # except Exception as e:
            #     print(e)
            #     with open("log.txt", "w+") as f:
            #         f.write(f"{datetime.datetime.now()} \n"
            #         "Error Log:0{e}\n"
            #         "Contact Device Administrator / Deveolper")


    def ConditionCheck(self, image, dir_path, line):
        current_file_path = line[0]
        if "name" in current_file_path:
            pass
        else:
            lang_dir = f"{dir_path}/{line[0].split('_')[-1]}"
            # print(lang_dir)
            if not os.path.exists(lang_dir):
                os.makedirs(lang_dir)
            for jpgfile in glob.iglob(os.path.join(image, "*.jpg")):
                shutil.copy(jpgfile, dir_path)
                _, tail = os.path.split(jpgfile)
                width, height = imagesize.get(f"{dir_path}\{tail}")      

                filesize = f"{width}x{height}"
                regex = re.compile(filesize)
                        
                if os.path.isfile(f"{lang_dir}/{current_file_path}.jpg"):pass    
                elif regex.findall(current_file_path):
                    os.rename(f"{dir_path}/{tail}", f"{lang_dir}/{current_file_path}.jpg")


    def closeEvent(self, event):
        dir_path = self.ui.Image_FilePath.toPlainText()
        QtWidgets.QMessageBox.setStyleSheet(self,"background:rgb(225, 225, 225)\n;"
        "color:rgb(0,0,0)")
        close = QtWidgets.QMessageBox.question(self, 
                                        "QUIT",
                                        "Are you sure want to stop process?",
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            if not type(event) == bool:
                # shutil.rmtree(dir_path)
                # os.rename(f"{dir_path}_Renamed", f"{dir_path}")
                event.accept()
            else:
                               
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()
        QtWidgets.QMainWindow.setStyleSheet(self,"background-color: rgb(220, 6, 6);")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Image_Renamer()
    ui.show()
    app.exec_()
       