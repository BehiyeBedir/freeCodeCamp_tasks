import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Veriyi içe aktar
data = pd.read_csv('epa-sea-level.csv')

# 'Year' sütununu sayısal formata dönüştür
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

# Eksik değerleri manuel olarak tamamla
data.at[137, 'CSIRO Adjusted Sea Level'] = (data.at[136, 'CSIRO Adjusted Sea Level'] + data.at[138, 'CSIRO Adjusted Sea Level']) / 2

# Tekrar eden satırları sil
data = data.drop_duplicates()

# Boş değerleri hemen üstündeki değerle doldur
data = data.fillna(method='ffill')

# Eksik değerleri temizle
data = data.dropna(subset=['Year', 'CSIRO Adjusted Sea Level'])

# Geçerli veri kontrolü
if not data.empty:
    # Dağılım grafiği oluştur
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data')

    # En uygun çizgiyi bulmak için lineer regresyon uygula
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    # En uygun çizgiyi çiz
    plt.plot(data['Year'], slope * data['Year'] + intercept, color='red', label='Best Fit Line')

    # 2050 yılına kadar olan tahmin
    future_years = range(data['Year'].min(), 2051)
    plt.plot(future_years, slope * future_years + intercept, linestyle='dashed', color='green', label='Prediction till 2050')

    # 2000 yılından sonraki en iyi uyum çizgisini çiz
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(future_years, slope_recent * future_years + intercept_recent, linestyle='dashed', color='blue', label='Prediction from 2000 onwards')

    # Etiketler ve başlık ekle
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Görüntüyü kaydet
    plt.savefig('sea_level_rise.png')

    # Görüntüyü göster
    plt.show()
else:
    print("Veride geçerli kayıt bulunamadı.")
