from image_info import image_info
from pprint import pprint
from PIL import Image

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                        QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit,QComboBox)
from PySide2.QtCore import Slot, Qt 





#___________________list sorting___________________________

string1 ='cactus near a beach'.lower()
string2 ='buildings in Italy'.lower()
string3 = 'quiet beach in Mexico'.lower()
string4 = 'amsterdam netherlands'.lower()
string5 = 'clouds over Berlin'.lower()

new_dict = {}

def preprocess(my_image_info):
    for i in my_image_info:
        new_dict[i['id']] = [tag.lower() for tag in i['tags']]

        for j in i['title'].split():
          new_dict[i['id']].append(j.rstrip(',').lower())
            
        new_dict[i['id']].insert(0,0)
        new_dict[i['id']].insert(1, i['title'][0].lower())


    return new_dict


def get_count_from_search(dictionary, search):
    for key, value in dictionary.items():   
      for counter, term in enumerate(value):
         if counter > 1:
           if term in search:
             value[0] += 1
    return dictionary

#def submit(self):
 #   your_photo = self.my_lineedit.text().lower 
preprocess(image_info)
get_count_from_search(new_dict, string1) # when I place your_photo in place of
#string1 I get NameError: name 'your_photo' is not defined

max_list=[]
max_val= 0
for key, value in new_dict.items():
    for counter, term in enumerate(value):
        if counter ==0:
            if term >= max_val:
                if term > max_val and len(max_list) > 0:
                    del max_list[:len(max_list)]
                max_val = term
                if max_val > 0:
                    max_list.append((value[1], key))

print(max_list)
max_list.sort()
#im = Image.open(f'images/{max_list[0][1]}.jpg')
im = Image.open(f'images/SJ001.jpg')
im.show()
    


max_list = []

#____________________data entering___________________

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        vbox1 = QVBoxLayout()
        self.my_lineedit = QLineEdit("Scarlett Johansson")
        self.label1 = QLabel('Enter Celebrity Name: ')
        self.my_lineedit.setMinimumWidth(250)
        self.my_lineedit.selectAll()
        self.my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('')
        self.my_btn.clicked.connect(self.on_submit)
        self.my_lineedit.returnPressed.connect(self.on_submit)
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.my_lineedit)
        vbox1.addWidget(self.my_btn)
        vbox1.addWidget(self.my_lbl)
        self.setLayout(vbox1)

        gbox1 = QGroupBox('Photo Search')
        gbox1.setLayout(vbox1)

        self.my_list = ["Pick a filter",'None', 'Sepia', 'Negative', 'Grayscale', 'Thumbnail']
        #                        0             1       2          3           4          5
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(self.my_list)
        self.my_label = QLabel("")

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.my_combo_box)
        vbox2.addWidget(self.my_label)

        self.setLayout(vbox2)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

        gbox2 = QGroupBox("Filters")
        gbox2.setLayout(vbox2)


        mbox = QVBoxLayout()
        mbox.addWidget(gbox1)
        mbox.addWidget(gbox2)

        self.setLayout(mbox)
        self.setWindowTitle("CST 205 Final Project")


    @Slot()
    def on_submit(self):
        your_photo = self.my_lineedit.text()
        self.my_lbl.setText(f'Your photo is {your_photo}')
    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_label.setText(f'You chose {self.my_list[my_index]}.')
      
##class filters(): 
##    def grey(im2):
##        im2 = Image.open('your_photo')
##    new_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
##    for a in im2.getdata() ]
##    im2.putdata(new_list)
##    im2.show()
##
##    def sepia(p):
##        p = Image.open('your_photo')
##    # tint shadows
##        if p[0] < 63:
##            r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
##    # tint midtones
##        elif p[0] > 62 and p[0] < 192:
##            r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
##    # tint highlights
##        else:
##            r = int(p[0] * 1.08)
##            if r > 255:
##                r = 255
##            g,b = p[1], int(p[2] * 0.5)
##        return r, g, b
##    
##
##    def neg(im2):
##        im2 = Image.open('your_photo')
##    # Using lambda with map()
##    # def negative_image(pixel):
##    # return tuple(map(lambda a : 255-a, pixel))
##    # negative_list = map(negative_image, im2.getdata())
##    negative_list = [(255-p[0], 255-p[1], 255-p[2])
##    for p in im2.getdata()]
##    im2.putdata(negative_list)
##    im2.show()
##
##    def thumb():
##        source = Image.open('your_photo')
##        w, h = source.width,source.height
##        target = Image.new('RGB', (w, h),
##        'rosybrown')
##        target_x = 0
##        for source_x in range(0, source.width, 2):
##            target_y = 0
##            for source_y in range(0, source.height, 2):
##              pixel = source.getpixel((source_x, source_y))
##              target.putpixel((target_x, target_y), pixel)
##              target_y += 1
##              target_x += 1
##        target.show()
##    


##for i in range(self.my_list):
##    if  submit.my_index== self.my_list[2]
##        let p = submit.my_index
##            filters.sepia(p)
##    elif  submit.my_index== self.my_list[3]
##        let im2 = submit.my_index
##            filters.neg(im2)
##    elif  submit.my_index== self.my_list[4]
##        let p = submit.my_index
##            filters.grey(im2)
##    elif  submit.my_index== self.my_list[5]
##        let p = submit.my_index
##            filters.thumbs(im2)
##    else 
##        im = Image.open(f'images/{max_list[0][1]}.jpg')
##        im.show()
##        

app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()