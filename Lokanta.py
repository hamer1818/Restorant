import os
import sys
import json
from datetime import datetime
from typing import Dict, Union, List, Tuple
import time

# Constants
DATA_FILE = "defter.json"
LOG_FILE = "islemler.log"
TABLE_COUNT = 20
VERSION = "2.0"

# Global variables with improved structure
class Restaurant:
    def __init__(self):
        self.cash: float = 0.0
        self.tables: Dict[int, float] = {i: 0.0 for i in range(TABLE_COUNT)}
        self.menu: Dict[str, float] = {
            "Çorba": 35.0,
            "Salata": 50.0,
            "Izgara Tavuk": 120.0,
            "Köfte": 110.0, 
            "İçecek": 25.0,
            "Tatlı": 45.0
        }
        self.daily_revenue: float = 0.0
        self.orders: Dict[int, List[Tuple[str, int, float]]] = {i: [] for i in range(TABLE_COUNT)}
        
restaurant = Restaurant()

def log_action(action: str) -> None:
    """Log actions with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} - {action}\n")

def update_cash(amount: float) -> None:
    """Update cash register amount"""
    restaurant.cash += amount
    restaurant.daily_revenue += amount
    print(f"Kasadaki toplam para: {restaurant.cash:.2f} TL")
    log_action(f"Kasa güncellendi: +{amount:.2f} TL, Toplam: {restaurant.cash:.2f} TL")

def show_tables() -> None:
    """Display all tables with their current bills"""
    print("\n" + "-" * 50)
    print(f"{'Masa No':^10} | {'Hesap Tutarı':^15} | {'Durum':^10}")
    print("-" * 50)
    
    for table_no, bill in restaurant.tables.items():
        status = "Dolu" if bill > 0 else "Boş"
        print(f"{table_no:^10} | {bill:^15.2f} TL | {status:^10}")
    
    print("-" * 50)
    input("\nAna menüye dönmek için Enter'e basın ")

def add_to_table() -> None:
    """Add items to a specific table's bill"""
    try:
        table_no = int(input("\nSiparişi ekleyeceğiniz masa numarası: "))
        if table_no not in restaurant.tables:
            print(f"Hata: Geçersiz masa numarası. 0-{TABLE_COUNT-1} arası bir değer girin.")
            return

        # Show menu
        print("\n" + "=" * 30)
        print(f"{'Ürün':^15} | {'Fiyat':^10}")
        print("=" * 30)
        
        for idx, (item, price) in enumerate(restaurant.menu.items(), 1):
            print(f"{idx}. {item:<12} | {price:>8.2f} TL")
        
        print("=" * 30)
        
        # Take orders
        while True:
            try:
                choice = int(input("\nEklemek istediğiniz ürün numarası (Çıkmak için 0): "))
                if choice == 0:
                    break
                    
                if 1 <= choice <= len(restaurant.menu):
                    item_name = list(restaurant.menu.keys())[choice-1]
                    item_price = restaurant.menu[item_name]
                    
                    quantity = int(input(f"Kaç adet {item_name} eklenecek? "))
                    if quantity <= 0:
                        print("Geçerli bir miktar girin.")
                        continue
                        
                    total_price = item_price * quantity
                    restaurant.tables[table_no] += total_price
                    restaurant.orders[table_no].append((item_name, quantity, total_price))
                    
                    print(f"{quantity} adet {item_name} eklendi. Toplam: {total_price:.2f} TL")
                    print(f"Masa {table_no} güncel hesap: {restaurant.tables[table_no]:.2f} TL")
                else:
                    print("Geçersiz seçim!")
            except ValueError:
                print("Geçerli bir sayı girin!")
    
    except ValueError:
        print("Lütfen geçerli bir masa numarası girin!")
    
    input("\nAna menüye dönmek için Enter'e basın ")

def view_table_details() -> None:
    """View detailed bill for a specific table"""
    try:
        table_no = int(input("\nHesap detaylarını görmek istediğiniz masa numarası: "))
        if table_no not in restaurant.tables:
            print(f"Hata: Geçersiz masa numarası. 0-{TABLE_COUNT-1} arası bir değer girin.")
            return
            
        if not restaurant.orders[table_no]:
            print(f"Masa {table_no} için henüz bir sipariş bulunmuyor.")
            return
            
        print(f"\n{'=' * 50}")
        print(f"{'MASA ' + str(table_no) + ' HESAP DETAYI':^50}")
        print(f"{'=' * 50}")
        print(f"{'Ürün':^20} | {'Adet':^8} | {'Tutar':^15}")
        print(f"{'-' * 50}")
        
        for item, quantity, price in restaurant.orders[table_no]:
            print(f"{item:^20} | {quantity:^8} | {price:>13.2f} TL")
            
        print(f"{'-' * 50}")
        print(f"{'TOPLAM':^30} | {restaurant.tables[table_no]:>13.2f} TL")
        print(f"{'=' * 50}")
    
    except ValueError:
        print("Lütfen geçerli bir masa numarası girin!")
    
    input("\nAna menüye dönmek için Enter'e basın ")

def pay_bill() -> None:
    """Process payment for a table"""
    try:
        table_no = int(input("\nHesap ödemesi yapılacak masa numarası: "))
        if table_no not in restaurant.tables:
            print(f"Hata: Geçersiz masa numarası. 0-{TABLE_COUNT-1} arası bir değer girin.")
            return
            
        current_bill = restaurant.tables[table_no]
        if current_bill == 0:
            print("Bu masada ödenecek bir hesap bulunmuyor.")
            input("Ana menüye dönmek için Enter'e basın ")
            return
            
        print(f"Masa {table_no} için ödenecek tutar: {current_bill:.2f} TL")
        
        # Show bill details if any orders exist
        if restaurant.orders[table_no]:
            print("\nSipariş detayı:")
            for item, quantity, price in restaurant.orders[table_no]:
                print(f"- {item}: {quantity} adet, {price:.2f} TL")
        
        payment = float(input("\nÖdenen tutarı giriniz: "))
        
        change = payment - current_bill
        if change < 0:
            print(f"Yetersiz ödeme! {abs(change):.2f} TL daha ödeme yapılması gerekiyor.")
            return
            
        update_cash(current_bill)
        
        if change > 0:
            print(f"Para üstü: {change:.2f} TL")
            
        print(f"Masa {table_no} hesabı başarıyla kapatıldı.")
        log_action(f"Masa {table_no} hesabı ödendi: {current_bill:.2f} TL")
        
        # Clear the table
        restaurant.tables[table_no] = 0
        restaurant.orders[table_no] = []
    
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
    
    input("\nAna menüye dönmek için Enter'e basın ")

def partial_payment() -> None:
    """Process partial payment for a table"""
    try:
        table_no = int(input("\nKısmi ödeme yapılacak masa numarası: "))
        if table_no not in restaurant.tables:
            print(f"Hata: Geçersiz masa numarası. 0-{TABLE_COUNT-1} arası bir değer girin.")
            return
            
        current_bill = restaurant.tables[table_no]
        if current_bill == 0:
            print("Bu masada ödenecek bir hesap bulunmuyor.")
            return
            
        print(f"Masa {table_no} için mevcut hesap: {current_bill:.2f} TL")
        
        payment = float(input("Ödenecek tutarı giriniz: "))
        if payment <= 0:
            print("Geçersiz tutar!")
            return
            
        if payment > current_bill:
            print(f"Ödenecek tutar hesaptan büyük olamaz! Maksimum {current_bill:.2f} TL ödeyebilirsiniz.")
            return
            
        restaurant.tables[table_no] -= payment
        update_cash(payment)
        
        print(f"Kısmi ödeme alındı: {payment:.2f} TL")
        print(f"Masa {table_no} kalan borç: {restaurant.tables[table_no]:.2f} TL")
        
        log_action(f"Masa {table_no} kısmi ödeme: {payment:.2f} TL, Kalan: {restaurant.tables[table_no]:.2f} TL")
    
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
    
    input("\nAna menüye dönmek için Enter'e basın ")

def daily_report() -> None:
    """Show daily sales report"""
    print("\n" + "=" * 60)
    print(f"{'GÜNLÜK RAPOR':^60}")
    print("=" * 60)
    
    print(f"Toplam masa sayısı: {TABLE_COUNT}")
    active_tables = sum(1 for bill in restaurant.tables.values() if bill > 0)
    print(f"Aktif (dolu) masa sayısı: {active_tables}")
    print(f"Günlük ciro: {restaurant.daily_revenue:.2f} TL")
    print(f"Kasadaki toplam para: {restaurant.cash:.2f} TL")
    
    if active_tables > 0:
        print("\nDolu masalar:")
        for table_no, bill in restaurant.tables.items():
            if bill > 0:
                print(f"- Masa {table_no}: {bill:.2f} TL")
    
    print("=" * 60)
    input("\nAna menüye dönmek için Enter'e basın ")

def save_data() -> None:
    """Save all restaurant data to JSON file"""
    data = {
        "cash": restaurant.cash,
        "tables": restaurant.tables,
        "daily_revenue": restaurant.daily_revenue,
        "orders": {str(table): orders for table, orders in restaurant.orders.items()}
    }
    
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        log_action("Veriler başarıyla kaydedildi")
    except Exception as e:
        print(f"Veri kaydetme hatası: {e}")
        log_action(f"Veri kaydetme hatası: {e}")

def load_data() -> None:
    """Load restaurant data from JSON file"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                
            restaurant.cash = data.get("cash", 0.0)
            restaurant.tables = {int(table): bill for table, bill in data.get("tables", {}).items()}
            restaurant.daily_revenue = data.get("daily_revenue", 0.0)
            
            # Convert order data back from strings to integers
            orders_data = data.get("orders", {})
            restaurant.orders = {int(table): orders for table, orders in orders_data.items()}
            
            log_action("Veriler başarıyla yüklendi")
        else:
            # Create new files if they don't exist
            save_data()
            with open(LOG_FILE, "a"):  # Create log file if it doesn't exist
                pass
            log_action("Yeni kayıt dosyaları oluşturuldu")
    except Exception as e:
        print(f"Veri yükleme hatası: {e}")
        log_action(f"Veri yükleme hatası: {e}")

def menu_management() -> None:
    """Manage restaurant menu items"""
    while True:
        print("\n" + "=" * 40)
        print(f"{'MENÜ YÖNETİMİ':^40}")
        print("=" * 40)
        print("1. Menüyü Görüntüle")
        print("2. Ürün Ekle")
        print("3. Ürün Sil")
        print("4. Ürün Fiyatı Güncelle")
        print("0. Ana Menüye Dön")
        print("=" * 40)
        
        choice = input("\nSeçiminiz: ")
        
        if choice == "1":
            # Display menu
            print("\n" + "=" * 40)
            print(f"{'RESTORAN MENÜSÜ':^40}")
            print("=" * 40)
            print(f"{'Ürün':^20} | {'Fiyat':^15}")
            print("-" * 40)
            
            for item, price in restaurant.menu.items():
                print(f"{item:^20} | {price:>13.2f} TL")
            
            print("=" * 40)
            
        elif choice == "2":
            # Add new menu item
            item_name = input("\nYeni ürün adı: ")
            try:
                item_price = float(input("Ürün fiyatı: "))
                if item_price <= 0:
                    print("Geçersiz fiyat! Pozitif bir değer girin.")
                    continue
                    
                if item_name in restaurant.menu:
                    confirm = input(f"{item_name} menüde zaten var. Fiyatını güncellemek istiyor musunuz? (E/H): ")
                    if confirm.upper() != "E":
                        continue
                        
                restaurant.menu[item_name] = item_price
                print(f"{item_name} menüye {item_price:.2f} TL fiyatla eklendi.")
                log_action(f"Menüye ürün eklendi: {item_name}, {item_price:.2f} TL")
                
            except ValueError:
                print("Geçersiz fiyat! Sayısal bir değer girin.")
                
        elif choice == "3":
            # Delete menu item
            if not restaurant.menu:
                print("Menüde silinecek ürün bulunmuyor.")
                continue
                
            print("\nMevcut Ürünler:")
            for idx, item in enumerate(restaurant.menu.keys(), 1):
                print(f"{idx}. {item}")
                
            try:
                item_idx = int(input("\nSilmek istediğiniz ürünün numarası: "))
                if 1 <= item_idx <= len(restaurant.menu):
                    item_name = list(restaurant.menu.keys())[item_idx-1]
                    
                    confirm = input(f"{item_name} ürününü silmek istediğinize emin misiniz? (E/H): ")
                    if confirm.upper() == "E":
                        del restaurant.menu[item_name]
                        print(f"{item_name} menüden silindi.")
                        log_action(f"Menüden ürün silindi: {item_name}")
                else:
                    print("Geçersiz numara!")
            except ValueError:
                print("Geçerli bir sayı girin!")
                
        elif choice == "4":
            # Update menu item price
            if not restaurant.menu:
                print("Menüde güncellenecek ürün bulunmuyor.")
                continue
                
            print("\nMevcut Ürünler:")
            for idx, (item, price) in enumerate(restaurant.menu.items(), 1):
                print(f"{idx}. {item} - {price:.2f} TL")
                
            try:
                item_idx = int(input("\nFiyatını güncellemek istediğiniz ürünün numarası: "))
                if 1 <= item_idx <= len(restaurant.menu):
                    item_name = list(restaurant.menu.keys())[item_idx-1]
                    current_price = restaurant.menu[item_name]
                    
                    try:
                        new_price = float(input(f"{item_name} için yeni fiyat ({current_price:.2f} TL): "))
                        if new_price <= 0:
                            print("Geçersiz fiyat! Pozitif bir değer girin.")
                            continue
                            
                        restaurant.menu[item_name] = new_price
                        print(f"{item_name} fiyatı {new_price:.2f} TL olarak güncellendi.")
                        log_action(f"Ürün fiyatı güncellendi: {item_name}, {current_price:.2f} TL -> {new_price:.2f} TL")
                        
                    except ValueError:
                        print("Geçerli bir fiyat girin!")
                else:
                    print("Geçersiz numara!")
            except ValueError:
                print("Geçerli bir sayı girin!")
                
        elif choice == "0":
            break
        else:
            print("Geçersiz seçim!")
            
        input("\nDevam etmek için Enter'e basın ")

def reset_day() -> None:
    """Reset daily revenue and optionally clear unpaid tables"""
    confirm = input("\nGünlük ciroyu sıfırlamak istediğinize emin misiniz? (E/H): ")
    if confirm.upper() == "E":
        # Check for unpaid tables
        unpaid_tables = [(table, bill) for table, bill in restaurant.tables.items() if bill > 0]
        
        if unpaid_tables:
            print("\nDikkat! Aşağıdaki masalarda hala ödenmemiş hesaplar var:")
            for table, bill in unpaid_tables:
                print(f"- Masa {table}: {bill:.2f} TL")
                
            clear_tables = input("\nTüm masa hesaplarını da sıfırlamak istiyor musunuz? (E/H): ")
            if clear_tables.upper() == "E":
                for table in restaurant.tables:
                    restaurant.tables[table] = 0
                    restaurant.orders[table] = []
                print("Tüm masa hesapları sıfırlandı.")
                log_action("Gün sonu - Tüm masalar sıfırlandı")
        
        # Log the end-of-day revenue
        log_action(f"Gün sonu - Toplam ciro: {restaurant.daily_revenue:.2f} TL")
        
        # Reset daily revenue
        restaurant.daily_revenue = 0
        print("Günlük ciro sıfırlandı.")
        
        save_data()
    else:
        print("İşlem iptal edildi.")
    
    input("\nAna menüye dönmek için Enter'e basın ")

def main() -> None:
    """Main application loop"""
    # Load existing data
    load_data()
    
    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w"):
            pass
    
    # Log application start
    log_action("Program başlatıldı")
    
    # Splash screen with loading animation
    print("\n" + "=" * 60)
    print(f"{'LOKANTA YÖNETİM SİSTEMİ':^60}")
    print(f"{'v' + VERSION:^60}")
    print("=" * 60)
    print("\nYükleniyor", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")
    
    while True:
        # Autosave data
        save_data()
        
        # Clear screen for better visibility
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Main menu
        print("\n" + "=" * 60)
        print(f"{'LOKANTA YÖNETİM SİSTEMİ':^60}")
        print("=" * 60)
        print(f"{'1. Masaları Görüntüle':^30} | {'6. Günlük Rapor':^27}")
        print(f"{'2. Sipariş Ekle':^30} | {'7. Menü Yönetimi':^27}")
        print(f"{'3. Masa Detayları':^30} | {'8. Günü Kapat':^27}")
        print(f"{'4. Hesap Ödeme':^30} | {'9. Hakkında':^27}")
        print(f"{'5. Kısmi Ödeme':^30} | {'0. Çıkış':^27}")
        print("=" * 60)
        print(f"Kasadaki Para: {restaurant.cash:.2f} TL | Günlük Ciro: {restaurant.daily_revenue:.2f} TL")
        print("=" * 60)
        
        choice = input("\nİşlem seçin: ")
        
        if choice == "1":
            show_tables()
        elif choice == "2":
            add_to_table()
        elif choice == "3":
            view_table_details()
        elif choice == "4":
            pay_bill()
        elif choice == "5":
            partial_payment()
        elif choice == "6":
            daily_report()
        elif choice == "7":
            menu_management()
        elif choice == "8":
            reset_day()
        elif choice == "9":
            print("\n" + "=" * 60)
            print(f"{'LOKANTA YÖNETİM SİSTEMİ':^60}")
            print(f"{'v' + VERSION:^60}")
            print("=" * 60)
            print("\nBu uygulama restoranlar için geliştirilmiş\nbir yönetim sistemidir.")
            print("\nÖzellikler:")
            print("- Masa hesaplarının takibi")
            print("- Menü yönetimi")
            print("- Sipariş takibi")
            print("- Günlük ciro raporları")
            print("- Otomatik veri kaydetme")
            print("\n(c) 2025 - Tüm hakları saklıdır.")
            input("\nAna menüye dönmek için Enter'e basın ")
        elif choice == "0":
            # Save data before exiting
            save_data()
            log_action("Program kapatıldı")
            print("\nVeriler kaydedildi. Program kapatılıyor...")
            time.sleep(1)
            sys.exit()
        else:
            input("\nGeçersiz seçim! Tekrar denemek için Enter'e basın.")

if __name__ == "__main__":
    main()