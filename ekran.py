# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekran.ui'
#
# Created: Wed Dec 13 15:01:33 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(516, 498)
        self.btn_olustur = QtGui.QPushButton(Dialog)
        self.btn_olustur.setGeometry(QtCore.QRect(230, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_olustur.setFont(font)
        self.btn_olustur.setObjectName(_fromUtf8("btn_olustur"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 60, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_veri = QtGui.QPushButton(Dialog)
        self.btn_veri.setEnabled(False)
        self.btn_veri.setGeometry(QtCore.QRect(340, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_veri.setFont(font)
        self.btn_veri.setObjectName(_fromUtf8("btn_veri"))
        self.lb_durum_2 = QtGui.QLabel(Dialog)
        self.lb_durum_2.setGeometry(QtCore.QRect(10, 20, 171, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.lb_durum_2.setFont(font)
        self.lb_durum_2.setObjectName(_fromUtf8("lb_durum_2"))
        self.table_butun = QtGui.QTableWidget(Dialog)
        self.table_butun.setGeometry(QtCore.QRect(10, 90, 151, 391))
        self.table_butun.setObjectName(_fromUtf8("table_butun"))
        self.table_butun.setColumnCount(0)
        self.table_butun.setRowCount(0)
        self.table_train = QtGui.QTableWidget(Dialog)
        self.table_train.setGeometry(QtCore.QRect(180, 90, 151, 391))
        self.table_train.setObjectName(_fromUtf8("table_train"))
        self.table_train.setColumnCount(0)
        self.table_train.setRowCount(0)
        self.table_test = QtGui.QTableWidget(Dialog)
        self.table_test.setGeometry(QtCore.QRect(350, 90, 151, 391))
        self.table_test.setObjectName(_fromUtf8("table_test"))
        self.table_test.setColumnCount(0)
        self.table_test.setRowCount(0)
        self.cb_yuzde = QtGui.QComboBox(Dialog)
        self.cb_yuzde.setGeometry(QtCore.QRect(180, 20, 41, 22))
        self.cb_yuzde.setObjectName(_fromUtf8("cb_yuzde"))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))
        self.cb_yuzde.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_olustur.setText(_translate("Dialog", "Veri Oluştur", None))
        self.label_2.setText(_translate("Dialog", "Veri Seti", None))
        self.label_3.setText(_translate("Dialog", "Train Veri Seti", None))
        self.label_4.setText(_translate("Dialog", "Test Veri Seti", None))
        self.btn_veri.setText(_translate("Dialog", "Bütün Veri Setini Göster", None))
        self.lb_durum_2.setText(_translate("Dialog", "Yüzde Kaç Train Oluşturulsun :", None))
        self.cb_yuzde.setItemText(0, _translate("Dialog", "10", None))
        self.cb_yuzde.setItemText(1, _translate("Dialog", "20", None))
        self.cb_yuzde.setItemText(2, _translate("Dialog", "30", None))
        self.cb_yuzde.setItemText(3, _translate("Dialog", "40", None))
        self.cb_yuzde.setItemText(4, _translate("Dialog", "50", None))
        self.cb_yuzde.setItemText(5, _translate("Dialog", "60", None))
        self.cb_yuzde.setItemText(6, _translate("Dialog", "70", None))
        self.cb_yuzde.setItemText(7, _translate("Dialog", "80", None))
        self.cb_yuzde.setItemText(8, _translate("Dialog", "90", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

