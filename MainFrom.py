# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:03:05 2017

@author: ESER
"""
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from skimage import io
import random
import os
import sys

from ekran import Ui_Dialog
  
class MainWindow(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_olustur.clicked.connect(self.btn_olustur_clicked)
        self.btn_veri.clicked.connect(self.butun_veri)
        self.comboBox.currentIndexChanged.connect(self.secilen_veri)   
    sozluk={}
    train_sozluk={}
    test_sozluk={}
    def btn_olustur_clicked(self):
        self.btn_veri.setEnabled(True)
        path='./Database/'
        klasor=os.listdir(path)
        for item in klasor:
            liste=[]
            veri=os.listdir(path+item)
            for veriler in veri:        
                liste.append(veriler)
            self.sozluk[item]=liste
            del liste
        for eleman in self.sozluk:
            self.train_sozluk[eleman]=random.sample(self.sozluk[eleman], len(self.sozluk[eleman])*int(self.cb_yuzde.currentText())/100)
        for st_eleman_al in self.sozluk:
            liste=[]
            for st_elemani in self.sozluk[st_eleman_al]:
                if st_elemani not in self.train_sozluk[st_eleman_al]:
                    liste.append(st_elemani)
            self.test_sozluk[st_eleman_al]=liste
            del liste
            
        for item in self.sozluk:
            self.comboBox.addItem(item)
            
        num_rows=len(self.sozluk[str(self.comboBox.currentText())])
        self.table_butun.setColumnCount(1)
        
        self.table_butun.setRowCount(num_rows)
        for rowNumber,row in enumerate(self.sozluk[self.comboBox.currentText()]):
            self.table_butun.setItem(rowNumber, 0, QtGui.QTableWidgetItem(str(row)))
            
        num_rows=len(self.train_sozluk[str(self.comboBox.currentText())])
        self.table_train.setColumnCount(1)
        self.table_train.setRowCount(num_rows)
        for rowNumber,row in enumerate(self.train_sozluk[self.comboBox.currentText()]):
            self.table_train.setItem(rowNumber, 0, QtGui.QTableWidgetItem(str(row)))
            
        num_rows=len(self.test_sozluk[str(self.comboBox.currentText())])
        self.table_test.setColumnCount(1)
        self.table_test.setRowCount(num_rows)
        for rowNumber,row in enumerate(self.test_sozluk[self.comboBox.currentText()]):
            self.table_test.setItem(rowNumber, 0, QtGui.QTableWidgetItem(str(row)))
            
    def secilen_veri(self):
        num_rows=len(self.sozluk[str(self.comboBox.currentText())])
        self.table_train.setRowCount(num_rows*int(self.cb_yuzde.currentText())/100)
      
        self.table_test.setRowCount(num_rows-(num_rows*int(self.cb_yuzde.currentText())/100))
       
        self.table_butun.setRowCount(num_rows)
        for rowNumber,row in enumerate(self.sozluk[self.comboBox.currentText()]):
            self.table_butun.setItem(rowNumber, 0, QtGui.QTableWidgetItem(str(row)))
            
        for rowNumber,row in enumerate(self.train_sozluk[self.comboBox.currentText()]):
            self.table_train.setItem(rowNumber, 0, QtGui.QTableWidgetItem(str(row)))
            
        for rowNumber,row in enumerate(self.test_sozluk[str(self.comboBox.currentText())]):
            self.table_test.setItem(rowNumber, 0, QtGui.QTableWidgetItem(str(row)))
            
    def butun_veri(self):
        num_rows=len(self.sozluk)*10
        self.table_train.setRowCount(num_rows*int(self.cb_yuzde.currentText())/100)
        self.table_test.setRowCount(num_rows-(num_rows*int(self.cb_yuzde.currentText())/100))       
        self.table_butun.setRowCount(num_rows)
        for veri in self.sozluk:
            for rowNumber,row in enumerate(self.train_sozluk[veri]):
                self.table_train.setItem((rowNumber + (int(veri)*int(self.cb_yuzde.currentText())/10))-int(self.cb_yuzde.currentText())/10, 0, QtGui.QTableWidgetItem(veri+ ' - ' +str(row)))
            for rowNumber,row in enumerate(self.test_sozluk[veri]):
                self.table_test.setItem((rowNumber +(int(veri)* (10-(int(self.cb_yuzde.currentText())/10))  ))-(10-(int(self.cb_yuzde.currentText())/10)), 0, QtGui.QTableWidgetItem(veri+ ' - ' +str(row)))
            for rowNumber,row in enumerate(self.sozluk[veri]):
                self.table_butun.setItem((rowNumber + (int(veri)*10))-10, 0, QtGui.QTableWidgetItem(veri+ ' - ' +str(row)))
                
        