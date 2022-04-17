


import os


masalar = dict()

for a in range(20):
    masalar[a] = 0

def osSystem(sistem):
    if sistem == "linux":
        os.system("clear")
    elif sistem == "windows":
        os.system("cls")

def ekle():
    masa_no = int(input("Hesap ekleyeceğiniz masayı seçin: "))
    gecerliHesap = masalar[masa_no]
    
    yeniHesap = float(input("Hesap tutarını girin: "))
    toplam = gecerliHesap+yeniHesap
    masalar[masa_no] = toplam

def sil():
    masa_no = int(input("Hesap sileceğiniz masayı seçin: "))
    silinecekMiktar = 0
    print(f"seçtiğiniz {masa_no} numaraları masanın borcu {masalar[masa_no]} ")
    silinecekMiktar = int(input("Lütfen silincek tutarı giriniz: "))
    eksiMi = masalar[masa_no] - silinecekMiktar
    if eksiMi <=-1:
        print("Hesap eksiye düştü Lütfen tekrar deneyiniz!!!")
        input("Ana menüye dönmek için Enter'e basın ")

    elif eksiMi >=0:
        eksildi = masalar[masa_no] - silinecekMiktar
        print("Hesap başarıyla eksildi/silindi")
        masalar[masa_no] = eksildi
        input("Ana menüye dönmek için Enter'e basın ")

def cikis():
    print("Program kapanıyor...")
    quit()

def kontrol(kayıt_adi):
    try:
        dosya = open(f"{kayıt_adi}")
        veriler = dosya.read()
        veriler=veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True
    except FileNotFoundError:
        dosya = open(f"{kayıt_adi}","w")
        print("Kayıt dosyası oluşturuldu!!")
        dosya.close()
        flag = False
    if flag:
        for a in enumerate(veriler):
            masalar[a[0]] = float(a[1])
    else:
        pass

def guncelle():
    dosya = open("defter.txt","w")
    for a in range(20):
        ucret = masalar[a]
        ucret = str(ucret)
        dosya.write(ucret+"\n")
    dosya.close()
def main():
    kontrol("defter.txt")
    isletimSisteminiSec = str(input("Lütfen işletim sistemini gir: "))
    while True:
        osSystem(isletimSisteminiSec)
        guncelle()

        print("""
                Lokanta Hesap Uygulamasına Hoşgeldiniz :

        1) Masaları Görüntüle
        2) Hesap Ekle
        3) Hesap Sil
        Q) Çık  


        """)
        secim = input("İşlem numarası gir: ")

        if secim == "1":
            for a in range(20):
                print(f"Masa {a} için hesap {masalar[a]} ")
            print("İşlem tamamlandı \n Ana menüye dönmek için Enter'e basın ")
            input()
        elif secim == "2":

            ekle()
            input("Ekleme işlemi tamamlandı\nAna menüye dönmek için Enter'e basınız ")
        elif secim == "3":
            sil()
        elif secim == "q" or secim == "Q":
            cikis()
        else:
            input("Yanlış/Eksik Seçim yaptınız\nMenüye dönmek için Enter'e basınız!")





main()