import sys
from calc import Ui_Dialog
from PySide import QtCore, QtGui

#
app = QtGui.QApplication(sys.argv)
#
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#Logic
#Переменные
first = 0
second = 0
equal = ''
res = 0

#Цифры
def bp0():
	ui.lineEdit.setText(ui.lineEdit.text() + '0')

def bp1():
	ui.lineEdit.setText(ui.lineEdit.text() + '1')

def bp2():
	ui.lineEdit.setText(ui.lineEdit.text() + '2')

def bp3():
	ui.lineEdit.setText(ui.lineEdit.text() + '3')

def bp4():
	ui.lineEdit.setText(ui.lineEdit.text() + '4')

def bp5():
	ui.lineEdit.setText(ui.lineEdit.text() + '5')

def bp6():
	ui.lineEdit.setText(ui.lineEdit.text() + '6')

def bp7():
	ui.lineEdit.setText(ui.lineEdit.text() + '7')

def bp8():
	ui.lineEdit.setText(ui.lineEdit.text() + '8')

def bp9():
	ui.lineEdit.setText(ui.lineEdit.text() + '9')

#Операторы
def plas():
	global first, equal
	first = float(ui.lineEdit.text())
	ui.lineEdit.setText('')
	equal = '+'

def mines():
	global first, equal
	first = float(ui.lineEdit.text())
	ui.lineEdit.setText('')
	equal = '-'

def pro():
	global first, equal
	first = float(ui.lineEdit.text())
	ui.lineEdit.setText('')
	equal = '*'

def chas():
	global first, equal
	first = float(ui.lineEdit.text())
	ui.lineEdit.setText('')
	equal = '/'

def result():
	global first, second, res, equal
	second = float(ui.lineEdit.text())
	if equal == '+':
		res = first + second
	elif equal == '-':
		res = first - second
	elif equal == '*':
		res = first * second
	elif equal == '/':
		res = first / second

	ui.lineEdit.setText(str(res))
	first = res

def reverse():
	global first
	first = float(ui.lineEdit.text())
	first = 0 - first
	ui.lineEdit.setText(str(first))

def clean():
	global first, second, res, equal
	first = 0
	second = 0
	equal = ''
	res = 0
	ui.lineEdit.setText('')

def pers():
	global res, first
	first = float(ui.lineEdit.text()) / 100
	ui.lineEdit.setText(str(first))

#Подключение кнопок
ui.pushButton_17.clicked.connect(bp0)
ui.pushButton_10.clicked.connect(bp1)
ui.pushButton_6.clicked.connect(bp2)
ui.pushButton_15.clicked.connect(bp3)
ui.pushButton_14.clicked.connect(bp4)
ui.pushButton_23.clicked.connect(bp5)
ui.pushButton_11.clicked.connect(bp6)
ui.pushButton_26.clicked.connect(bp7)
ui.pushButton_28.clicked.connect(bp8)
ui.pushButton_7.clicked.connect(bp9)
ui.pushButton_16.clicked.connect(plas)
ui.pushButton_12.clicked.connect(mines)
ui.pushButton_8.clicked.connect(pro)
ui.pushButton_4.clicked.connect(chas)
ui.pushButton_20.clicked.connect(result)
ui.pushButton_25.clicked.connect(reverse)
ui.pushButton_27.clicked.connect(clean)
ui.pushButton_24.clicked.connect(pers)





#Запуск программы
sys.exit(app.exec_())