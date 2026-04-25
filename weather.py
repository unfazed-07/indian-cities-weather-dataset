import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"

indian_cities = {
    "Shimla": (31.1044, 77.1666),
    "Srinagar": (34.0857, 74.8055),
    "Hyderabad": (17.384,78.4564),
    "Bengaluru": (12.9719,77.5937),
    "Delhi": (28.6519,77.2315),
    "Jaipur": (26.9196, 75.7878),
    "Guwahati": (26.1844,91.7458),
    "Kolkata": (22.5626,88.363),
    "Chennai": (13.0878, 80.2785),
    "Mumbai": (19.0728,72.8826),
}

combined_data = []
for city, (lat, lng) in indian_cities.items():
    params = {
        "latitude": lat,
        "longitude": lng,
        "end_date": "2026-04-25",
        "start_date":"2024-04-25",
        "daily":"temperature_2m_max,temperature_2m_min,temperature_2m_mean,rain_sum,daylight_duration"
    }
    data = requests.get(url, params= params)
    data = data.json()
    print(data)

    df = pd.DataFrame({
        "city":city,
        "date": data["daily"]["time"],
        "max_temp": data["daily"]["temperature_2m_max"],
        "min_temp": data["daily"]["temperature_2m_min"],
        "mean_temp": data["daily"]["temperature_2m_mean"],
        "rainfall_mm": data["daily"]["rain_sum"],
        "daily_duration": data["daily"]["daylight_duration"],
    })
    combined_data.append(df)
final_df = pd.concat(combined_data, ignore_index=True)

# Convert date to datetime
final_df['date'] = pd.to_datetime(final_df['date'])

# Extract month and year
final_df['month'] = final_df['date'].dt.month
final_df['year'] = final_df['date'].dt.year

def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Winter'

final_df['season'] = final_df['month'].apply(get_season)

final_df['is_rainy'] = final_df['rainfall_mm'] > 1
final_df['temp_range'] = final_df['max_temp']-final_df['min_temp']

def categorize_temp(temp):
    if temp > 30:
        return 'Hot'
    elif temp > 20:
        return 'Warm'
    elif temp > 10:
        return 'Cool'
    else:
        return 'Cold'

final_df['temperature_category'] = final_df['mean_temp'].apply(categorize_temp)

# Reorder columns for better readability
final_df = final_df[['city','date','year','month','season','max_temp', 'min_temp', 
      'mean_temp', 'temperature_category', 'temp_range','rainfall_mm', 
      'is_rainy','daily_duration']]

print(final_df.head(10))
print(f"\nDataset shape: {final_df.shape}")
print(f"\nDataset info:")
print(final_df.info())

final_df.to_csv("weather_dataset.csv", index=False)