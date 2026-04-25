# Indian Cities Weather Dataset (2024–2026)

This repository contains a multi-city daily weather dataset for major Indian cities, covering a wide range of climatic conditions across the country.

The dataset spans **2 years (April 2024 to April 2026)** and includes both raw weather data and engineered features, making it suitable for data analysis and machine learning tasks.

---

## 🌍 Cities Covered

The dataset includes 10 cities selected to represent diverse climatic regions of India:

- Shimla (Cold, Himalayan region)
- Srinagar (Cold, Northern region)
- Delhi (North, continental climate)
- Jaipur (Hot, semi-arid)
- Mumbai (Coastal, humid)
- Chennai (Coastal, tropical)
- Bengaluru (Moderate, plateau)
- Hyderabad (Warm, inland)
- Kolkata (Humid, eastern region)
- Guwahati (North-East, high rainfall)

This selection ensures a **balanced representation of climates**, from cold mountainous regions to hot inland cities and humid coastal areas.

---

## 📅 Time Range

- Start Date: **2024-04-25**
- End Date: **2026-04-25**
- Frequency: **Daily**

---

## 📊 Dataset Features

The dataset contains the following columns:

### 🧾 Basic Information
- `city`: Name of the city
- `date`: Date of observation (YYYY-MM-DD)
- `year`: Year extracted from date
- `month`: Month extracted from date

### 🌦️ Weather Metrics
- `max_temp`: Maximum daily temperature (°C)
- `min_temp`: Minimum daily temperature (°C)
- `mean_temp`: Average daily temperature (°C)
- `rainfall_mm`: Total daily rainfall (mm)
- `daily_duration`: Daylight duration (seconds)

### 🧠 Engineered Features
- `season`: Season category derived from month
- `temperature_category`: Categorized temperature (Cold, Cool, Warm)
- `temp_range`: Difference between max and min temperature
- `is_rainy`: Boolean indicator (True if rainfall > 0)

---

## ⚙️ Data Source

- Data collected using the **Open-Meteo API**
- URL: https://open-meteo.com/

---

## 🧠 Use Cases

This dataset can be used for:

- Time-series analysis  
- Weather trend analysis  
- Seasonal pattern comparison  
- Rain prediction models  
- Machine learning (classification & regression)  
- Forecasting tasks  

---

## 🔗 Kaggle Dataset

You can access and download the dataset from Kaggle:

👉 [https://www.kaggle.com/datasets/unfazed007/indian-cities-weather-dataset-20242026]

---

## ⚠️ Notes

- Dataset is preprocessed and includes feature engineering  
- Suitable for beginners and intermediate data science projects  
- Covers multiple climate zones for better generalization  

---

## 📜 License

This dataset is released under **CC BY 4.0 (Attribution License)**.
