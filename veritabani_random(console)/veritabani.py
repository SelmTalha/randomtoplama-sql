import sqlite3
import random

sql=sqlite3.connect("random.db")
cur=sql.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS randomekle(Sayi1 INT,Sayi2 INT,Tahmin INT,Gercek_sonuc INT,Durum TEXT)")
sayi1=random.randint(1,100)
sayi2=random.randint(1,100)
toplam=sayi1+sayi2
print(sayi1,"+",sayi2,":")
a=int(input("Sonucu giriniz :"))

if a==toplam:
    cur.execute("INSERT INTO randomekle(Sayi1,Sayi2,Tahmin,Gercek_sonuc,Durum) VALUES(?,?,?,?,?)",
    (sayi1,sayi2,a,toplam,'Başarılı!'))
    sql.commit()
else:
    cur.execute("INSERT INTO randomekle(Sayi1,Sayi2,Tahmin,Gercek_sonuc,Durum) VALUES(?,?,?,?,?)",
    (sayi1,sayi2,a,toplam,'Başarısız!'))
    sql.commit()

sql.close()