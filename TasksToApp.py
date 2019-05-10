import sys
import datetime
from itertools import cycle
import PyQt5
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtWidgets import QApplication, QLabel, QRadioButton, QButtonGroup, QVBoxLayout
#from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.SetWidgets_Wnd()
        self.SetWidgets_Btn()
        self.SetWidgets_Radio()

        self.SetWidgets_LabelEdit1()
        self.SetWidgets_LabelEdit2()
        self.SetWidgets_LabelEdit3()
        self.SetWidgets_LabelEdit4()

        self.show()

    def SetWidgets_Wnd(self):
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Training tasks on Python')
        self.setWindowIcon(QIcon('lamp.png'))

    def SetWidgets_Btn(self):
        self.btn = QPushButton('Run', self)
        self.btn.move(170, 130)
        self.btn.clicked.connect(self.btnClicked)

        self.btn_clear = QPushButton('Clear', self)
        self.btn_clear.move(200, 130)
        self.btn_clear.clicked.connect(self.btnClear)

    def SetWidgets_Radio(self):
        self.radiobtn1 = QRadioButton('arithmentic')
        self.radiobtn1.setChecked(True)
        self.radiobtn2 = QRadioButton('leap year')
        self.radiobtn3 = QRadioButton('square')
        self.radiobtn4 = QRadioButton('seasons')
        self.radiobtn5 = QRadioButton('bank')
        self.radiobtn6 = QRadioButton('prime numbers')
        self.radiobtn7 = QRadioButton('calendar')
        self.radiobtn8 = QRadioButton('XOR')

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radiobtn1)
        self.button_group.addButton(self.radiobtn2)
        self.button_group.addButton(self.radiobtn3)
        self.button_group.addButton(self.radiobtn4)
        self.button_group.addButton(self.radiobtn5)
        self.button_group.addButton(self.radiobtn6)
        self.button_group.addButton(self.radiobtn7)
        self.button_group.addButton(self.radiobtn8)
        self.button_group.buttonClicked.connect(self.on_radio_button_clicked)

        self.label_layout = QLabel('Choose task:')
        layout = QVBoxLayout()
        layout.addWidget(self.label_layout)
        layout.addWidget(self.radiobtn1)
        layout.addWidget(self.radiobtn2)
        layout.addWidget(self.radiobtn3)
        layout.addWidget(self.radiobtn4)
        layout.addWidget(self.radiobtn5)
        layout.addWidget(self.radiobtn6)
        layout.addWidget(self.radiobtn7)
        layout.addWidget(self.radiobtn8)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn_clear)

        self.setLayout(layout)

    def SetWidgets_LabelEdit1(self):
        self.lbl_1 = QLabel(self)
        self.lbl_1.setText("1st number:")
        self.lbl_1.move(120, 30)
        self.le1 = QLineEdit(self)
        self.le1.setGeometry(190, 35, 100, 20)

    def SetWidgets_LabelEdit2(self):
        self.lbl_2 = QLabel(self)
        self.lbl_2.setText("2nd number:")
        self.lbl_2.move(120, 60)
        self.le2 = QLineEdit(self)
        self.le2.setGeometry(190, 65, 100, 20)

    def SetWidgets_LabelEdit3(self):
        self.lbl_3 = QLabel(self)
        self.lbl_3.setText("Operation:")
        self.lbl_3.move(120, 90)
        self.le3 = QLineEdit(self)
        self.le3.setGeometry(190, 95, 100, 20)

    def SetWidgets_LabelEdit4(self):
        self.lbl_4 = QLabel(self)
        self.lbl_4.setText("Result:")
        self.lbl_4.move(120, 120)
        self.le4 = QLineEdit(self)
        self.le4.setGeometry(190, 125, 100, 20)
        self.le4.setReadOnly(True)

    def on_radio_button_clicked(self, button):
        if self.radiobtn1.isChecked():

            self.lbl_1.setText("1st number:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(190, 35, 100, 20)

            self.lbl_2.setText("2nd number:")
            self.lbl_2.setVisible(True)
            self.le2.setVisible(True)
            self.le2.setGeometry(190, 65, 100, 20)

            self.lbl_3.setText("Operation:")
            self.lbl_3.setVisible(True)
            self.le3.setVisible(True)
            self.le3.setGeometry(190, 95, 100, 20)

            self.lbl_4.setText("Result:")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(190, 125, 100, 20)

            self.funcReadOnly(self.le2, False)
            self.funcReadOnly(self.le3, False)

            self.btnClear()

        elif self.radiobtn2.isChecked():
            self.lbl_1.setText("Year:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(180, 35, 70, 20)

            self.lbl_2.setVisible(False)
            self.le2.setVisible(False)

            self.lbl_3.setVisible(False)
            self.le3.setVisible(False)

            self.lbl_4.setText("Leap Year?")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(180, 125, 100, 20)

            self.btnClear()

        elif self.radiobtn3.isChecked():
            self.lbl_1.setText("Side:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(180, 35, 100, 20)

            self.lbl_2.setText("S = :")
            self.lbl_2.setVisible(True)
            self.le2.setVisible(True)
            self.le2.setGeometry(180, 65, 100, 20)

            self.lbl_3.setText("P = :")
            self.lbl_3.setVisible(True)
            self.le3.setVisible(True)
            self.le3.setGeometry(180, 95, 100, 20)

            self.lbl_4.setText("Diagonal = ")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(180, 125, 100, 20)

            self.funcReadOnly(self.le2, True)
            self.funcReadOnly(self.le3, True)

            self.btnClear()

        elif self.radiobtn4.isChecked():
            self.lbl_1.setText("Month:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(160, 35, 100, 20)

            self.lbl_2.setVisible(False)
            self.lbl_3.setVisible(False)

            self.le2.setVisible(False)
            self.le3.setVisible(False)

            self.lbl_4.setText("Season:")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(160, 125, 100, 20)

            self.btnClear()

        elif self.radiobtn5.isChecked():
            self.lbl_1.setText("Deposit:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(170, 35, 100, 20)

            self.lbl_2.setText("Years:")
            self.lbl_2.setVisible(True)
            self.le2.setVisible(True)
            self.le2.setGeometry(170, 65, 100, 20)

            self.lbl_3.setVisible(False)
            self.le3.setVisible(False)

            self.lbl_4.setText("Total:")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(170, 125, 100, 20)

            self.funcReadOnly(self.le2, False)

            self.btnClear()

        elif self.radiobtn6.isChecked():
            self.lbl_1.setText("Number:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(170, 35, 100, 20)

            self.lbl_2.setVisible(False)
            self.lbl_3.setVisible(False)

            self.le2.setVisible(False)
            self.le3.setVisible(False)

            self.lbl_4.setText("Is Prime?:")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(170, 125, 100, 20)

            self.btnClear()

        elif self.radiobtn7.isChecked():
            self.lbl_1.setText("Day:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(210, 35, 100, 20)

            self.lbl_2.setText("Month:")
            self.lbl_2.setVisible(True)
            self.le2.setVisible(True)
            self.le2.setGeometry(210, 65, 100, 20)

            self.lbl_3.setText("Year:")
            self.lbl_3.setVisible(True)
            self.le3.setVisible(True)
            self.le3.setGeometry(210, 95, 100, 20)

            self.lbl_4.setText("Date (True/False):")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(210, 125, 100, 20)

            self.funcReadOnly(self.le2, False)
            self.funcReadOnly(self.le3, False)

            self.btnClear()

        elif self.radiobtn8.isChecked():
            self.lbl_1.setText("Source:")
            self.lbl_1.setVisible(True)
            self.le1.setVisible(True)
            self.le1.setGeometry(170, 35, 200, 20)

            self.lbl_2.setText("Key:")
            self.lbl_2.setVisible(True)
            self.le2.setVisible(True)
            self.le2.setGeometry(170, 65, 100, 20)

            self.lbl_3.setText("Encrypt:")
            self.lbl_3.setVisible(True)
            self.le3.setVisible(True)
            self.le3.setGeometry(170, 95, 200, 20)

            self.lbl_4.setText("Decrypt:")
            self.lbl_4.setVisible(True)
            self.le4.setVisible(True)
            self.le4.setGeometry(170, 125, 200, 20)

            self.funcReadOnly(self.le2, False)
            self.funcReadOnly(self.le3, True)

            self.btnClear()

    def funcReadOnly(self, sLabEd, sBools):
        sLabEd.setReadOnly(sBools)

    def btnClicked(self):
        if self.radiobtn1.isChecked():
            if self.le1.text().isdigit() and self.le2.text().isdigit():
                iNumber1 = int(self.le1.text())
                iNumber2 = int(self.le2.text())
                sOp = self.le3.text()
                sResult = str(self.arithmetic(iNumber1, iNumber2, sOp))
                self.le4.setText(sResult)
            else:
                self.le4.setGeometry(190, 125, 200, 20)
                self.le4.setText("One of two numbers isn't digit.")

        elif self.radiobtn2.isChecked():
            if self.le1.text().isdigit():
                sInpYear = int(self.le1.text())
                sIsItLeap = str(self.is_year_leap(sInpYear))
                self.le4.setText(sIsItLeap)
            else:
                self.le4.setText("Year isn't digit.")

        elif self.radiobtn3.isChecked():
            if self.le1.text().isdigit():
                iSideSquare = int(self.le1.text())
                sKortezh = self.square(iSideSquare)

                self.le2.setText(str(sKortezh[0]))
                self.le3.setText(str(sKortezh[1]))
                self.le4.setText(str(sKortezh[2]))
            else:
                self.le4.setText("Side isn't digit.")

        elif self.radiobtn4.isChecked():
            if self.le1.text().isdigit():
                iMonth = int(self.le1.text())
                sSeason = self.season(iMonth)
                self.le4.setText(str(sSeason))
            else:
                self.le4.setText("Month isn't digit.")

        elif self.radiobtn5.isChecked():
            if self.le1.text().isdigit() and self.le2.text().isdigit():
                sDeposit = int(self.le1.text())
                sYears = int(self.le2.text())

                sSum = self.bank(sDeposit, sYears)
                self.le4.setText(str(sSum))
            else:
                self.le4.setGeometry(170, 125, 200, 20)
                self.le4.setText("One of two numbers isn't digit.")

        elif self.radiobtn6.isChecked():
            if self.le1.text().isdigit():
                sNumber = int(self.le1.text())
                sRes = self.is_prime(sNumber)
                self.le4.setText(str(sRes))
            else:
                self.le4.setText("Number isn't digit.")

        elif self.radiobtn7.isChecked():
            if self.le1.text().isdigit() and self.le2.text().isdigit() and self.le3.text().isdigit():
                sDay = int(self.le1.text())
                sMonth = int(self.le2.text())
                sYear = int(self.le3.text())
                sRes = self.is_date_true(sDay, sMonth, sYear)
                self.le4.setText(str(sRes))
            else:
                self.le4.setGeometry(210, 125, 170, 20)
                self.le4.setText("One of three numbers isn't digit.")

        elif self.radiobtn8.isChecked():
            sSource = self.le1.text()
            sKey = self.le2.text()
            sEncStr = self.XOR_cipher(sSource, sKey)
            self.le3.setText(str(sEncStr))
            sDecryptStr = self.XOR_cipher(sEncStr, sKey)
            self.le4.setText(str(sDecryptStr))

    def btnClear(self):
        self.le1.setText(None)
        self.le2.setText(None)
        self.le3.setText(None)
        self.le4.setText(None)
        if self.radiobtn8.isChecked():
            self.le4.resize(200, 20)
        else:
            self.le4.resize(100, 20)

    def arithmetic(self, iNum1, iNum2, sOper):
        self.le4.setGeometry(190, 125, 100, 20)
        sRes = None
        if sOper == "+":
            sRes = iNum1 + iNum2
        elif sOper == "-":
            if iNum1 >= iNum2:
                sRes = iNum1 - iNum2
            else:
                sRes = iNum2 - iNum1
        elif sOper == "*":
            sRes = iNum1 * iNum2
        elif sOper == "/":
            if iNum2 == 0:
                self.le4.setGeometry(190, 125, 200, 20)
                sRes = "Division by zero is not allowed"
            else:
                sRes = iNum1 / iNum2
        else:
            self.le4.setGeometry(190, 125, 200, 20)
            sRes = "Unknown operation"
        return sRes

    def is_year_leap(self, iYear):
        sBool = None
        if ((iYear % 4 == 0 and iYear % 100 != 0) or iYear % 400 == 0):
            sBool = True
        else:
            sBool = False
        return sBool

    def square(self, iSide):
        sS = iSide*iSide
        sP = 4*iSide
        sDiag = round(pow(iSide, 0.5), 2)
        sKort = (sS, sP, sDiag)
        return sKort

    def season(self, iMon):
        sRes = None
        if iMon >= 1 and iMon <= 12:
            list_mons = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
            list_seasons = ["Winter", "Spring", "Summer", "Autumn"]

            for iquarter_mons in range(len(list_mons)):
                for j in list_mons[iquarter_mons]:
                    if j == iMon:
                        sRes = list_seasons[iquarter_mons]
        else:
            sRes = "Invalid month!!!"

        return sRes

    def bank(self, iDep, iDepYear):
        sProc = 0.1
        for iYear in range(iDepYear):
            iDep = iDep + iDep * sProc
        return iDep

    def is_prime(self, iNum):
        self.le4.setGeometry(170, 125, 100, 20)
        sRes = None
        bNum = True
        if iNum >= 2 and iNum <= 1000:
            for i in range (2, iNum):
                if iNum%i == 0:
                    bNum = False
        else:
            self.le4.setGeometry(170, 125, 200, 20)
            bNum = "Enter number between 2 and 1000"

        return bNum

    def is_date_true(self, iDay, iMon, iYear):
        sDat = None
        try:
            bDate = datetime.date(iYear, iMon, iDay)
            sDat = isinstance(bDate, datetime.date)
        except ValueError:
            sDat = "False"
        return sDat

    def XOR_cipher(self, sStr, sXorKey):
        sEncrypt = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(sStr, cycle(sXorKey)))
        return sEncrypt



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

