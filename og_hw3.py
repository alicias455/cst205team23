#Alicia Sandoval
#CST 205
#10/23/2020
#Create a GUI for an image search engine in which will produce an image with most words in common with the 
# search terms. If there is a tie then the picture whose first letter in the title comes first in the 
# alphabet will be chosen.

from image_info import image_info
from pprint import pprint
from PIL import Image
import sys
from PySide2.QtWidgets import QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QGroupBox, QPushButton
from PySide2.QtCore import Slot

#s1 ='cactus near a beach'.lower()
#s2 = 'building in Italy'.lower()

new_dict ={}

def preprocess(my_image_info):
    for i in my_image_info:
        new_dict[i['id']] = [tag.lower() for tag in i['tags']]

        #adds each word of title to list of values eliminating commas in title
        for j in i['title'].split():
            new_dict[i['id']].append(j.rstrip(',').lower())
        
        #adds a counter that we'll increment w/# of hits
        new_dict[i['id']].insert(0,0)
        #adds first letter of title to be used in case of tie
        new_dict[i['id']].insert(1, i['title'][0].lower()) 

    return new_dict

def get_count(dictionary, search):
    for key, value in dictionary.items():
        for counter, term in enumerate(value):
            if counter > 1:
                if term in search:
                    value[0] += 1
   
    return dictionary

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.label1 = QLabel('Describe the picture: ')
    self.line_edit = QLineEdit(self)
    #print(self.line_edit.QLineEdit.text())
    preprocess(image_info)
    self.btn = QPushButton("Search")
    self.btn.clicked.connect(self.on_click)

    hbox1 = QHBoxLayout()
    hbox1.addWidget(self.label1)
    hbox1.addWidget(self.line_edit)
    hbox1.addWidget(self.btn)

    gbox1 = QGroupBox()
    gbox1.setLayout(hbox1)

    mbox = QVBoxLayout()
    mbox.addWidget(gbox1)

    self.setLayout(mbox)
    self.setWindowTitle("CST 205 HW3")

  @Slot()
  def on_click(self):
      get_count(new_dict, self.line_edit.text().lower())
      #print(get_count(new_dict, self.line_edit.text().lower()))
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
      #print(max_list)
      im = Image.open(f'images/{max_list[0][1]}.jpg')
      im.show()

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()


#pprint(preprocess(image_info))
#pprint(new_dict)
#print(max_list)