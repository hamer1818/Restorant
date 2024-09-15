# Restaurant Bill Management Application

This is a simple Python application to manage table bills for a restaurant. It allows you to add and remove bills for each table, as well as track the total money collected in the restaurant's cash register.

## Features
- **View Table Bills**: See the current balance for each of the 20 tables.
- **Add Bill**: Add a new bill to a specific table.
- **Remove Bill**: Remove or settle a bill for a table, and handle overpayments by giving change.
- **Persistent Data**: Bills are saved to a file and reloaded upon restarting the application.

## How to Use

1. **View Tables**: Press `1` to view all tables and their bills.
2. **Add Bill**: Press `2` to add a bill to a table.
3. **Remove Bill**: Press `3` to settle or remove a bill from a table.
4. **Exit**: Press `Q` to exit the program.

## File Structure

- **`defter.txt`**: This file stores the bill amounts for each table. It is automatically created if it doesn't exist and updated with every change made in the program.

## Requirements

- Python 3.x

## How to Run

1. Clone this repository or download the code.
2. Run the Python file:

   ```bash
   python3 restaurant_app.py
    ```

# Türkçesi
# Restoran Fatura Yönetim Uygulaması

Bu, bir restoran için masa faturalarını yönetmek için basit bir Python uygulamasıdır. Her masaya fatura eklemenize ve kaldırmanıza, restoranın kasa kaydında toplanan toplam parayı takip etmenize olanak tanır.

## Özellikler
- **Masa Faturalarını Görüntüle**: 20 masanın her biri için mevcut bakiyeyi görüntüleyin.
- **Fatura Ekle**: Belirli bir masaya yeni bir fatura ekleyin.
- **Faturayı Kaldır**: Bir masadan faturayı kapatın veya kaldırın ve fazla ödemeleri geri vererek değişiklik yapın.
- **Kalıcı Veri**: Faturalar bir dosyaya kaydedilir ve uygulama yeniden başlatıldığında yeniden yüklenir.

## Nasıl Kullanılır

1. **Masaları Görüntüle**: Tüm masaları ve faturalarını görmek için `1` tuşuna basın.
2. **Fatura Ekle**: Bir masaya fatura eklemek için `2` tuşuna basın.
3. **Faturayı Kaldır**: Bir masadan faturayı kapatın veya kaldırın.
4. **Çıkış**: Programdan çıkmak için `Q` tuşuna basın.

## Dosya Yapısı

- **`defter.txt`**: Bu dosya, her masanın fatura tutarlarını saklar. Dosya otomatik olarak oluşturulur ve programda yapılan her değişiklikle güncellenir.

## Gereksinimler

- Python 3.x

## Nasıl Çalıştırılır

1. Bu depoyu klonlayın veya kodu indirin.
2. Python dosyasını çalıştırın:

   ```bash
   python3 restaurant_app.py
    ```

