from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.uic import loadUi
import sys
r=""
l=[]
def int_number(x):
    global r
    if l==0:
       r=r+w.pushButton_x.text

def c():
    message_box = QMessageBox()
    message_box.setIcon(QMessageBox.Warning)
    message_box.setText("")
    message_box.show()
    message_box.exec()
def opposite():
    global r
    global l
    r=int(r)
    r=-r
    r=str(r)
    l.append(r)
def percent():
    global r
    global l
    l.append(r/100)
def sum():
    global r
    global l
    l.append("+")
    l.append(r)
    r=''
def sub():
    global r
    global l
    l.append("-")
    l.append(r)
    r=''
def divide():
    global r
    global l
    l.append("/")
    l.append(r)
    r=''
def multi():
    global r
    global l
    l.append("*")
    l.append(r)
    r=''
def run():
    z=l[0]
    for i in range (len(l)):
        if l[i]=="/":
            z=z/eval(l[i+1])
        if l[i]=="+":
            z=z+eval(l[i+1])
        if l[i]=="-":
            z=z-eval(l[i+1])
        if l[i]=="*":
            z=z*eval(l[i+1])
    message_box = QMessageBox()
    message_box.setIcon(QMessageBox.Warning)
    message_box.setText(z)
    message_box.show()
    message_box.exec()
    exec ()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = loadUi('calculator.ui')
    w.show()
    while True:
        w.pushButton_5.clicked.connect(int_number(5))
        w.pushButton_6.clicked.connect(int_number(6))
        w.pushButton_7.clicked.connect(int_number(7))
        w.pushButton_9.clicked.connect(int_number(9))
        w.pushButton_10.clicked.connect(int_number(10))
        w.pushButton_11.clicked.connect(int_number(11))
        w.pushButton_13.clicked.connect(int_number(13))
        w.pushButton_14.clicked.connect(int_number(14))
        w.pushButton_15.clicked.connect(int_number(15))
        w.pushButton_17.clicked.connect(int_number(17))
        w.pushButton_18.clicked.connect(int_number(18))
        w.pushButton.clicked.connect(c)
        w.pushButton_2.clicked.connect(opposite)
        w.pushButton_3.clicked.connect(percent)
        w.pushButton_4.clicked.connect(devide)
        w.pushButton_8.clicked.connect(multi)
        w.pushButton_16.clicked.connect(sum)
        w.pushButton_12.clicked.connect(sub)
        w.pushButton_19.clicked.connect(int_number(19))
        w.pushButton_20.clicked.connect(run)
    app.exec()