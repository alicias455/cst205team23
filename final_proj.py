#CST 205
#Celebrity Image Search
#The program allows the user to input a celebrity name and it will provide images found in our "gallery" that conatin this celebrity. If no
#images are available "No images found." will be displayed.
#John Mar Shimun, Douglas Pattison, Alicia Sandoval
#12/14/20
#John created the image_info file and input the images info
#Alicia focused on getting the images to display correctly
#Douglas debugged and researched potential APIs
#preprocess simplifies the image_info file
#MyWindow creates the GUI
#the on_click method creates an array based on the words that were typed in by the user and then using this array we display all the images 
#available in the array.

from image_info import image_info
from pprint import pprint
from PIL import Image
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit,QComboBox, QScrollArea)
from PySide2.QtCore import Slot, Qt 
from PySide2.QtGui import QPixmap, QImage, QPalette

#___________________list sorting___________________________

new_dict = {}

def preprocess(my_image_info):
    for i in my_image_info:
        new_dict[i['id']] = [tag.lower() for tag in i['tags']]

        for j in i['title'].split():
          new_dict[i['id']].append(j.rstrip(',').lower())
            
        new_dict[i['id']].insert(0,0)
        new_dict[i['id']].insert(1, i['title'][0].lower())


    return new_dict

def get_count(dictionary, search):
    for key, value in dictionary.items():
        for counter, term in enumerate(value):
            if counter > 1:
                if term in search:
                    value[0] += 1
   
    return dictionary

#____________________data entering___________________

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.label1 = QLabel('Enter Celebrity Full Name: ')
    self.line_edit = QLineEdit(self)
    preprocess(image_info)

    self.label = QLabel()
    self.label2 = QLabel("No images found.")

    self.btn = QPushButton("Search")
    self.btn.clicked.connect(self.on_click)

    #self.scrollArea = QScrollArea()

    hbox1 = QHBoxLayout()
    hbox1.addWidget(self.label1)
    hbox1.addWidget(self.line_edit)
    hbox1.addWidget(self.btn)

    self.vbox1 = QVBoxLayout()
    #vbox1.addWidget(self.label)

    gbox1 = QGroupBox()
    gbox1.setLayout(hbox1)
    self.gbox2 = QGroupBox()
    #gbox2.setLayout(self.vbox1)

    mbox = QVBoxLayout()
    mbox.addWidget(gbox1)
    mbox.addWidget(self.gbox2)

    self.setLayout(mbox)
    self.setWindowTitle("CST 205 Final Project")


  @Slot()
  def on_click(self):
        get_count(new_dict, self.line_edit.text().lower())
        max_list = []
        max_val = 0

        for key, value in new_dict.items():
            for counter, term in enumerate(value):
                if counter == 0:
                    if term >= max_val:
                        if term > max_val and len(max_list) > 0:
                            del max_list[:len(max_list)]
                        max_val = term
                        if max_val > 0:
                            max_list.append((value[1], key))

            max_list.sort()

        size = len(max_list)

        if size == 0:
            self.vbox1.addWidget(self.label2)
            self.gbox2.setLayout(self.vbox1)
            #print("No images found.")

        for i in range(size):
                #print(i)
                im = Image.open(f'images/{max_list[i][1]}.jpg')
                im.show()

                # image = QImage(f'images/{max_list[i][1]}.jpg')
                # self.label.setPixmap(QPixmap.fromImage(image))
                # self.scrollArea.setBackgroundRole(QPalette.Dark)
                # self.scrollArea.setWidget(self.label)
                # self.vbox1.addWidget(self.scrollArea)

                # pixmap = QPixmap(f'images/{max_list[i][1]}.jpg')
                # self.label.setPixmap(pixmap)
                # self.vbox1.addWidget(self.label)
                # self.gbox2.setLayout(self.vbox1)

                i += 1

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()