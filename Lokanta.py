import os
import sys

# Global variable to track the total money in the restaurant's cash register
kasadakiPara = 0

# Dictionary to store the account (bill) for each table. Initially, all values are set to 0.
masalar = dict()

for a in range(20):
    masalar[a] = 0

# Function to add money to the cash register
def kasaPara(girenPara):
    global kasadakiPara
    kasadakiPara += girenPara
    print(f"Kasadaki toplam para {kasadakiPara} ")

# Function to add a bill to a specific table
def ekle():
    masa_no = int(input("Hesap ekleyeceğiniz masayı seçin: "))
    gecerliHesap = masalar[masa_no]

    yeniHesap = float(input("Hesap tutarını girin: "))
    toplam = gecerliHesap + yeniHesap
    masalar[masa_no] = toplam

# Function to subtract a bill or settle the table's bill
def sil():
    masa_no = int(input("Hesap sileceğiniz masayı seçin: "))
    print(f"Seçtiğiniz {masa_no} numaralı masanın borcu {masalar[masa_no]} ")
    
    # If the table already has no debt, exit the function
    if masalar[masa_no] == 0.0:
        print("Hesap tutarı 0 olduğu için işlem gerçekleştirilemiyor")
        input("Ana menüye dönmek için Enter'e basın ")
        return
    
    silinecekMiktar = int(input("Lütfen silinecek tutarı giriniz: "))
    eksiMi = masalar[masa_no] - silinecekMiktar

    if eksiMi < 0:
        para_ustu = abs(eksiMi)  # Calculate the change to be given back
        print(f"Hesap tutarından fazla ödeme yapıldı. Para üstü: {para_ustu} ")
        kasaPara(masalar[masa_no])
        masalar[masa_no] = 0
    else:
        masalar[masa_no] = eksiMi
        print("Hesap başarıyla eksildi/silindi")
        kasaPara(silinecekMiktar)
    
    input("Ana menüye dönmek için Enter'e basın ")

# Function to exit the program
def cikis():
    print("Program kapanıyor...")
    sys.exit()

# Function to check and load existing data from a file
def kontrol(kayıt_adi):
    try:
        # Try to open the file containing the table data
        with open(kayıt_adi) as dosya:
            veriler = dosya.read().splitlines()  # Split by lines
        for idx, value in enumerate(veriler):
            masalar[idx] = float(value)
    except FileNotFoundError:
        # Create a new file if it doesn't exist
        with open(kayıt_adi, "w") as dosya:
            print("Kayıt dosyası oluşturuldu!!")

# Function to update the file with the current table bills
def guncelle():
    with open("defter.txt", "w") as dosya:
        for ucret in masalar.values():
            dosya.write(f"{ucret}\n")

# Main loop to control the application's menu
def main():
    kontrol("defter.txt")  # Check if the file exists, otherwise create it

    while True:
        guncelle()

        print("""
                Lokanta Hesap Uygulamasına Hoşgeldiniz:

        1) Masaları Görüntüle
        2) Hesap Ekle
        3) Hesap Sil
        Q) Çık  

        """)
        
        secim = input("İşlem numarası gir: ")

        if secim == "1":
            for masa_no, hesap in masalar.items():
                print(f"Masa {masa_no} için hesap: {hesap} ")
            input("İşlem tamamlandı \nAna menüye dönmek için Enter'e basın ")
        elif secim == "2":
            ekle()
            input("Ekleme işlemi tamamlandı\nAna menüye dönmek için Enter'e basınız ")
        elif secim == "3":
            sil()
        elif secim.lower() == "q":
            cikis()
        else:
            input("Yanlış/Eksik Seçim yaptınız\nMenüye dönmek için Enter'e basınız!")

# Run the main program
main()
