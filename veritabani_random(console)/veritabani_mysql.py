import mysql.connector 
import random

config = {
            'user': 'root',
            'password': '',
            'database': 'randomdnm',
            'host': '127.0.0.1'
        }
sql=mysql.connector.connect(**config)
cur=sql.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS randomekle(Sayi1 INT,Sayi2 INT,Tahmin INT,Gercek_sonuc INT,Durum TEXT)")
sayi1=random.randint(1,100)
sayi2=random.randint(1,100)
toplam=sayi1+sayi2
print(sayi1,"+",sayi2,":")
a=int(input("Sonucu giriniz :"))

if a==toplam:
    cur.execute("INSERT INTO randomekle(Sayi1,Sayi2,Tahmin,Gercek_sonuc,Durum) VALUES(%s,%s,%s,%s,%s)",
    (sayi1,sayi2,a,toplam,'Başarılı!'))
    sql.commit()
else:
    cur.execute("INSERT INTO randomekle(Sayi1,Sayi2,Tahmin,Gercek_sonuc,Durum) VALUES(%s,%s,%s,%s,%s)",
    (sayi1,sayi2,a,toplam,'Başarısız!'))
    sql.commit()

sql.close()