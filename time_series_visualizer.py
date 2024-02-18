import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Web sitesinden tıklanma verilerini çek
url = "https://www.freecodecamp.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Tıklanma verilerini içeren etiketleri bul
click_elements = soup.find_all("span", class_="click-counter")

# Verileri bir CSV dosyasına yaz
csv_file = "click_data.csv"
header = ["Element", "Clicks"]

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for element in click_elements:
        element_name = element.get("data-name")
        click_count = element.get("data-count")
        writer.writerow([element_name, click_count])

print(f"Click data has been saved to {csv_file}")

# Sayfa görüntüleme verilerini içe aktar
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Verileri temizle
df_cleaned = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

# Çizgi grafiği çizme fonksiyonu
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 7))
    df_cleaned.plot(kind="line", ax=ax, title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")
    plt.show(block=False)  # block=False ile plt.show()'un beklemesini engelle
    time.sleep(1)
    plt.close()

# Çubuk grafiği çizme fonksiyonu
def draw_bar_plot():
    df_bar = df_cleaned.copy()
    df_bar["month"] = df_bar.index.month
    df_bar["year"] = df_bar.index.year

    df_bar = df_bar.groupby(["year", "month"]).mean()
    df_bar = df_bar.unstack()

    fig, ax = plt.subplots(figsize=(14, 7))
    df_bar.plot(kind="bar", ax=ax, xlabel="Years", ylabel="Average Page Views", title="Months")
    plt.legend(title="Months", labels=[month.strftime("%B") for month in pd.date_range("2022-01-01", "2022-12-01", freq="M")])
    plt.show(block=False)
    time.sleep(1)
    plt.close()

# Kutu grafiğini çizme fonksiyonu
def draw_box_plot():
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box["date"]]
    df_box["month"] = [d.strftime("%b") for d in df_box["date"]]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0]).set(title="Year-wise Box Plot (Trend)")
    sns.boxplot(x="month", y="value", data=df_box, order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=axes[1]).set(title="Month-wise Box Plot (Seasonality)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    plt.show(block=False)
    time.sleep(1)
    plt.close()

# Fonksiyonları çağır
draw_line_plot()
draw_bar_plot()
draw_box_plot()

# Sonsuz döngü ekleyerek pencereyi manuel olarak kapatana kadar bekleyebilirsiniz
while True:
    plt.pause(0.1)
