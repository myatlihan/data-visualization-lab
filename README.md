# Data Visualization Lab

Interactive data visualization and statistics learning application built with Python, FastAPI, JavaScript and Plotly.

Python, FastAPI, JavaScript ve Plotly kullanılarak geliştirilen interaktif veri görselleştirme ve istatistik öğrenme uygulamasıdır.

> **Project Status / Proje Durumu: Under Active Development / Aktif Geliştirme**
>
> This project is currently under active development. The **Histogram** module is the first complete visualization module and serves as the foundation for the remaining modules.
>
> Proje şu anda aktif olarak geliştirilmektedir. **Histogram** modülü geliştirilen ilk kapsamlı görselleştirme modülüdür ve diğer modüller için temel oluşturmaktadır.
>
> Additional visualization types, statistical analysis tools, interactive features, and educational content will be added progressively.
>
> İlerleyen süreçte farklı grafik türleri, istatistiksel analiz araçları, interaktif özellikler ve eğitici içerikler aşamalı olarak eklenecektir.

---

## Project Goal / Projenin Amacı

Data Visualization Lab is designed not only to visualize data, but also to help users understand the statistical concepts behind different visualization techniques.

Data Visualization Lab yalnızca veri görselleştirmek için değil, farklı görselleştirme tekniklerinin arkasındaki istatistiksel kavramların anlaşılmasına yardımcı olmak amacıyla tasarlanmaktadır.

Users will be able to:

Kullanıcılar:

- Enter their own numerical datasets — Kendi sayısal veri setlerini girebilecek
- Visualize data distributions — Veri dağılımlarını görselleştirebilecek
- Adjust visualization parameters interactively — Görselleştirme parametrelerini interaktif olarak değiştirebilecek
- Calculate descriptive statistics — Betimsel istatistikleri hesaplayabilecek
- Explore statistical concepts through explanations — İstatistiksel kavramları açıklamalar üzerinden keşfedebilecek
- Observe how changes in the dataset affect statistical results — Veri setindeki değişikliklerin sonuçları nasıl etkilediğini gözlemleyebilecek
- Experiment with different visualization techniques — Farklı görselleştirme tekniklerini deneyebilecek

The project is being developed as both a **data visualization application** and an **interactive statistics learning environment**.

Proje hem bir **veri görselleştirme uygulaması** hem de **interaktif bir istatistik öğrenme ortamı** olarak geliştirilmektedir.

---

##  Current Features / Mevcut Özellikler

### Histogram

The **Histogram** is currently the first complete visualization module.

**Histogram**, şu anda tamamlanan ilk görselleştirme modülüdür.

Current functionality / Mevcut özellikler:

- Custom numerical dataset input — Özel sayısal veri seti girişi
- Adjustable number of bins — Ayarlanabilir bin sayısı
- Interactive Plotly histogram — İnteraktif Plotly histogram grafiği
- Dynamic chart updates — Dinamik grafik güncelleme
- Responsive user interface — Responsive kullanıcı arayüzü
- Educational explanation of histogram concepts — Histogram kavramlarını açıklayan eğitici içerik
- Descriptive statistics — Betimsel istatistikler

### Descriptive Statistics / Betimsel İstatistikler

The application currently calculates / Uygulama şu anda hesaplamaktadır:

- Mean — Aritmetik Ortalama
- Median — Medyan
- Mode — Mod
- Minimum — Minimum
- Maximum — Maksimum
- Range — Aralık
- First Quartile (Q1) — Birinci Çeyrek
- Third Quartile (Q3) — Üçüncü Çeyrek
- Interquartile Range (IQR) — Çeyrekler Açıklığı
- Variance — Varyans
- Standard Deviation — Standart Sapma
- Outliers — Aykırı Değerler
- Sorted Data — Sıralanmış Veri

The statistical calculations are implemented manually in Python to better understand the mathematical principles behind common statistical operations.

İstatistiksel hesaplamalar, yaygın istatistiksel işlemlerin arkasındaki matematiksel prensipleri daha iyi anlamak amacıyla Python ile manuel olarak uygulanmaktadır.

---

## Technologies / Kullanılan Teknolojiler

### Backend

- Python
- FastAPI
- Pydantic

### Data Visualization / Veri Görselleştirme

- Plotly

### Frontend

- HTML
- CSS
- JavaScript

### Testing / Test

- Pytest

---

## Project Structure / Proje Yapısı

```text
data-visualization-lab/
│
├── backend/
│   ├── __init__.py
│   ├── api/
│   ├── statistics/
│   │   ├── __init__.py
│   │   └── statics.py
│   ├── transformations/
│   │   └── __init__.py
│   └── visualizations/
│       ├── __init__.py
│       └── histogram.py
│
├── frontend/
│   ├── css/
│   │   └── histogram.css
│   ├── js/
│   │   └── histogram.js
│   └── templates/
│       └── histogram.html
│
├── tests/
│   └── test_statics.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation / Kurulum

Clone the repository / Repoyu klonlayın:

```bash
git clone https://github.com/myatlihan/data-visualization-lab.git
```

Navigate to the project directory / Proje klasörüne girin:

```bash
cd data-visualization-lab
```

Create a virtual environment / Sanal ortam oluşturun:

```bash
python -m venv .venv
```

Activate the virtual environment / Sanal ortamı aktif edin:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies / Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Application / Uygulamayı Çalıştırma

Start the FastAPI server / FastAPI sunucusunu başlatın:

```bash
uvicorn main:app --reload
```

The API will be available at / API şu adreste çalışacaktır:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation / FastAPI interaktif dokümantasyonu:

```text
http://127.0.0.1:8000/docs
```