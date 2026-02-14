# OIBSIP_Task2
# 🌦️ Weather Pro - Python Weather Application

A modern **Tkinter-based Weather Application** that fetches real-time weather data for ANY city using the OpenWeatherMap API.

---

## 🚀 Features

- 🔍 Search weather for ANY city worldwide
- 🌡️ Toggle between Celsius (°C) and Fahrenheit (°F)
- 🌤️ Weather icons display
- 💧 Humidity information
- 💨 Wind speed details
- 📊 Atmospheric pressure
- 🕒 Current date & time display
- 🎨 Modern and clean GUI design

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- Requests (API calls)
- Pillow (Image handling)
- OpenWeatherMap API
- Datetime module

---

## 📂 Project Structure

```
Weather-Pro/
│
├── weather_app.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Weather-Pro.git
cd Weather-Pro
```

### 2️⃣ Install Required Libraries

```bash
pip install requests pillow
```

### 3️⃣ Add Your API Key

Inside the Python file, replace:

```python
self.API_KEY = "YOUR_API_KEY"
```

Get a free API key from:
https://openweathermap.org/api

### 4️⃣ Run the Application

```bash
python weather_app.py
```

---

## 🌍 How It Works

1. Enter any city name.
2. Click **GET WEATHER**.
3. Weather data is fetched from OpenWeatherMap API.
4. Results display temperature, humidity, wind, pressure, and icon.
5. Toggle between °C and °F anytime.

---

## 📡 API Used

OpenWeatherMap Current Weather API:

```
http://api.openweathermap.org/data/2.5/weather
```

---

## 🔮 Future Improvements

- 5-day weather forecast
- Background image based on weather
- Dark mode
- Auto-location detection
- Weather history tracking

---

## 👩‍💻 Author

Deekshitha 

---

## 📜 License

This project is licensed under the MIT License.
