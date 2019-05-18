from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import sqlite3
import random

sql=sqlite3.connect("random.db")
cursor=sql.cursor()
class benimEkranim(QMainWindow):
    def __init__(self):
        super(benimEkranim,self).__init__()

        uic.loadUi("Guiveritabani.ui",self)
        self.setWindowTitle("Toplama Islemi")
        self.tablo_olustur()
        self.islem()
        self.verilerigoster()
        self.Hesaplabtn.clicked.connect(self.veritabanina_ekle)
        self.KayitSil.clicked.connect(self.verileri_sil)
        
    def tablo_olustur(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS randomekle(Sayi1 ,
        Sayi2 ,Tahmin TEXT,Gercek_sonuc INT,Durum TEXT)""")

    def verilerigoster(self):
        model=QStandardItemModel()
        cursor.execute("SELECT * FROM randomekle")
        for i in cursor.fetchall():
            model.appendRow(QStandardItem(str(i)))
        self.listView.setModel(model)
    
    def verileri_sil(self):
        pass

    def islem(self):
        self.a=random.randint(1,100)
        self.b=random.randint(1,100)
        
        self.gerceksonuc=self.a+self.b
        self.sayi1.setText(str(self.a))
        self.sayi2.setText(str(self.b))

    def veritabanina_ekle(self):
        tahmin=self.linetahmin.text()
        
        if int(tahmin)==self.gerceksonuc:
            cursor.execute("INSERT INTO randomekle(Sayi1,Sayi2,Tahmin,Gercek_sonuc,Durum) VALUES(?,?,?,?,?)",
            (self.a,self.b,tahmin,self.gerceksonuc,'Başarılı!'))
            sql.commit()
            self.verilerigoster()
            self.islem()
        else:
            cursor.execute("INSERT INTO randomekle(Sayi1,Sayi2,Tahmin,Gercek_sonuc,Durum) VALUES(?,?,?,?,?)",
            (self.a,self.b,tahmin,self.gerceksonuc,'Başarısız!'))
            sql.commit()
            self.verilerigoster()
            self.islem()
        
    
app=QApplication(sys.argv)
selim=benimEkranim()
selim.show()
sys.exit(app.exec_())