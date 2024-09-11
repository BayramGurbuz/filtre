import pandas as pd
from datetime import datetime

# CSV dosyasını yükleyin
file_path = r"C:\Users\bayra\Desktop\Database\project\accidentt.csv"
data = pd.read_csv(file_path)

# Tarih sütununu gözden geçirin ve hatalı tarihleri tespit edin
def check_date(date):
    try:
        return datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        return None

data['date'] = data['date'].apply(check_date)

# Hatalı tarihleri içeren satırları göster
invalid_dates = data[data['date'].isnull()]
print("Hatalı tarihler:")
print(invalid_dates)

# Hatalı tarihleri içeren satırları veri kümesinden kaldırın
data = data.dropna(subset=['date'])

# Police force sütunundaki hatalı değerleri kontrol edin ve temizleyin
data = data[(data['police_force'] > 0) & (data['police_force'] <= 43)]

# Accident severity sütunundaki hatalı değerleri kontrol edin ve temizleyin
data = data[(data['accident_severity'] >= 1) & (data['accident_severity'] <= 3)]

# Urban or rural area sütunundaki hatalı değerleri kontrol edin ve temizleyin
data = data[(data['urban_or_rural_area'] >= 1) & (data['urban_or_rural_area'] <= 2)]

# Did police officer attend scene of accident sütunundaki hatalı değerleri kontrol edin ve temizleyin
data = data[(data['did_police_officer_attend_scene_of_accident'] >= 1) & (data['did_police_officer_attend_scene_of_accident'] <= 2)]

# Temizlenmiş veri kümesini kaydedin
cleaned_file_path = r"C:\Users\bayra\Desktop\Database\project\cleaned_accidentt.csv"
data.to_csv(cleaned_file_path, index=False)

print(f"Temizlenmiş veri kümesi '{cleaned_file_path}' dosyasına kaydedildi.")
