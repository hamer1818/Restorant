# Restaurant Management System

A comprehensive Python application for managing restaurant operations including table billing, order tracking, menu management, and daily revenue reporting.

## Features

- **Table Management**
  - View all tables with their current bill status
  - See detailed bill breakdowns by item
  - Support for up to 20 tables (configurable)
  
- **Order Processing**
  - Add individual menu items to tables
  - Track quantities and prices per item
  - View detailed order history for each table
  
- **Payment Handling**
  - Process full table payments
  - Support partial payments
  - Calculate change automatically
  - Update cash register immediately
  
- **Menu Management**
  - View, add, edit and remove menu items
  - Update prices for existing items
  - Full menu customization
  
- **Financial Reporting**
  - Daily revenue tracking
  - End-of-day reporting and reset
  - Cash register balance monitoring
  
- **Data Persistence**
  - Automatic saving of all data to JSON file
  - Detailed activity logging
  - Data recovery on program restart

## How to Use

1. **View Tables**: Press `1` to see all tables with their status and bills
2. **Add Orders**: Press `2` to add menu items to a specific table
3. **Table Details**: Press `3` to see detailed bill breakdown for a table
4. **Process Payment**: Press `4` to settle a bill for a table
5. **Partial Payment**: Press `5` to process a partial payment
6. **Daily Report**: Press `6` to see daily sales summary
7. **Menu Management**: Press `7` to manage restaurant menu items
8. **End of Day**: Press `8` to close the day and reset daily revenue
9. **About**: Press `9` for application information
10. **Exit**: Press `0` to exit the program and save data

## File Structure

- **`defter.json`**: Stores all restaurant data in JSON format including tables, orders, and cash register
- **`islemler.log`**: Maintains a detailed log of all operations with timestamps

## Technical Improvements

- Object-oriented design for better code organization
- Type annotations for enhanced code quality
- Improved error handling throughout the application
- Optimized data storage with JSON format
- Clean user interface with formatted tables

## Requirements

- Python 3.6 or higher

## How to Run

1. Clone this repository or download the code
2. Navigate to the application folder
3. Run the Python file:

   ```bash
   python Lokanta.py
   ```

# Türkçesi
# Lokanta Yönetim Sistemi

Masa faturalandırma, sipariş takibi, menü yönetimi ve günlük gelir raporlaması dahil olmak üzere restoran işlemlerini yönetmek için kapsamlı bir Python uygulaması.

## Özellikler

- **Masa Yönetimi**
  - Tüm masaları mevcut hesap durumlarıyla görüntüleme
  - Ürün bazında detaylı hesap dökümlerini görme
  - 20 masaya kadar destek (yapılandırılabilir)
  
- **Sipariş İşleme**
  - Masalara tek tek menü öğeleri ekleme
  - Ürün başına miktar ve fiyatları takip etme
  - Her masa için detaylı sipariş geçmişini görüntüleme
  
- **Ödeme İşlemleri**
  - Tam masa ödemelerini işleme
  - Kısmi ödemeleri destekleme
  - Para üstünü otomatik hesaplama
  - Kasa kaydını anında güncelleme
  
- **Menü Yönetimi**
  - Menü öğelerini görüntüleme, ekleme, düzenleme ve kaldırma
  - Mevcut öğelerin fiyatlarını güncelleme
  - Tam menü özelleştirme
  
- **Finansal Raporlama**
  - Günlük gelir takibi
  - Gün sonu raporlama ve sıfırlama
  - Kasa bakiyesi izleme
  
- **Veri Kalıcılığı**
  - Tüm verilerin JSON dosyasına otomatik kaydedilmesi
  - Detaylı aktivite günlüğü tutma
  - Program yeniden başlatıldığında veri kurtarma

## Nasıl Kullanılır

1. **Masaları Görüntüle**: Tüm masaları durumları ve hesaplarıyla görmek için `1` tuşuna basın
2. **Sipariş Ekle**: Belirli bir masaya menü öğeleri eklemek için `2` tuşuna basın
3. **Masa Detayları**: Bir masa için detaylı hesap dökümünü görmek için `3` tuşuna basın
4. **Ödeme İşleme**: Bir masa için hesap kapatmak için `4` tuşuna basın
5. **Kısmi Ödeme**: Kısmi ödeme işlemek için `5` tuşuna basın
6. **Günlük Rapor**: Günlük satış özetini görmek için `6` tuşuna basın
7. **Menü Yönetimi**: Restoran menü öğelerini yönetmek için `7` tuşuna basın
8. **Gün Sonu**: Günü kapatmak ve günlük geliri sıfırlamak için `8` tuşuna basın
9. **Hakkında**: Uygulama bilgilerini görmek için `9` tuşuna basın
10. **Çıkış**: Programdan çıkmak ve verileri kaydetmek için `0` tuşuna basın

## Dosya Yapısı

- **`defter.json`**: Masalar, siparişler ve kasa dahil tüm restoran verilerini JSON formatında saklar
- **`islemler.log`**: Zaman damgalı olarak tüm işlemlerin detaylı bir günlüğünü tutar

## Teknik İyileştirmeler

- Daha iyi kod organizasyonu için nesne yönelimli tasarım
- Geliştirilmiş kod kalitesi için tip açıklamaları
- Uygulama genelinde geliştirilmiş hata yönetimi
- JSON formatı ile optimize edilmiş veri depolama
- Biçimlendirilmiş tablolar ile temiz kullanıcı arayüzü

## Gereksinimler

- Python 3.6 veya daha yüksek

## Nasıl Çalıştırılır

1. Bu depoyu klonlayın veya kodu indirin
2. Uygulama klasörüne gidin
3. Python dosyasını çalıştırın:

   ```bash
   python Lokanta.py
   ```