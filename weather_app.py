import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io
from datetime import datetime


class WeatherPro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌦️ Weather Pro")
        self.root.geometry("950x800")
        self.root.configure(bg='#e8f4f8')

        # ✅ YOUR API KEY
        self.API_KEY = "6f3e274cc352d6a7a766ad0cb5412e09"
        self.weather_data = {}
        self.is_metric = True

        self.build_interface()

    def build_interface(self):
        # Header
        header = tk.Frame(self.root, bg='#2563eb', height=100)
        header.pack(fill='x', padx=5, pady=(5, 15))
        header.pack_propagate(False)

        tk.Label(header, text="🌦️ WEATHER APP - WORKS EVERYWHERE",
                 font=('Arial', 28, 'bold'), bg='#2563eb', fg='white').pack(expand=True)

        # Search - FIXED
        search_frame = tk.Frame(self.root, bg='#e8f4f8')
        search_frame.pack(pady=20)

        tk.Label(search_frame, text="🔍 Enter ANY City:", font=('Arial', 14, 'bold'),
                 bg='#e8f4f8').pack()

        entry_frame = tk.Frame(search_frame, bg='#e8f4f8')
        entry_frame.pack(pady=10)

        self.city_entry = tk.Entry(entry_frame, font=('Arial', 16), width=20)
        self.city_entry.pack(side='left', padx=(0, 10))
        self.city_entry.insert(0, "Bengaluru")  # Default

        # ✅ FIXED: Proper command binding
        self.search_btn = tk.Button(entry_frame, text="🔍 GET WEATHER",
                                    bg='#059669', fg='white', font=('Arial', 14, 'bold'),
                                    command=self.get_weather, relief='flat', padx=30, pady=10)
        self.search_btn.pack(side='left')

        # Unit toggle
        self.unit_btn = tk.Button(search_frame, text="°F", bg='#ef4444', fg='white',
                                  font=('Arial', 12, 'bold'), command=self.toggle_units)
        self.unit_btn.pack(pady=10)

        # Results area
        self.result_frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
        self.result_frame.pack(fill='both', expand=True, padx=30, pady=20)

        # Debug console
        self.debug_label = tk.Label(self.result_frame, text="👆 Click GET WEATHER for any city!",
                                    font=('Arial', 16), bg='white')
        self.debug_label.pack(expand=True)

    def get_weather(self):
        """✅ FIXED - Works for ALL cities"""
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("⚠️", "Enter a city name!")
            return

        self.debug_label.config(text=f"🔄 Fetching weather for '{city}'...")
        self.root.update()

        try:
            # ✅ YOUR API KEY WORKING
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': city,
                'appid': self.API_KEY,
                'units': 'metric' if self.is_metric else 'imperial'
            }

            print(f"🌐 API Call: {url} | City: {city}")  # Debug
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            print(f"📡 Response: {response.status_code}")  # Debug
            print(f"📄 Data: {data}")  # Debug

            if response.status_code == 200:
                self.display_weather(data, city)
            else:
                error_msg = data.get('message', 'Unknown error')
                self.debug_label.config(text=f"❌ '{city}' not found!\nError: {error_msg}")
                print(f"❌ API Error: {error_msg}")

        except requests.exceptions.RequestException as e:
            self.debug_label.config(text=f"❌ Network error: {str(e)}")
            print(f"🌐 Network Error: {e}")
        except Exception as e:
            self.debug_label.config(text=f"❌ Error: {str(e)}")
            print(f"💥 Unexpected Error: {e}")

    def display_weather(self, data, city):
        """Display weather data"""
        # Clear previous
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Icon
        try:
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
            img_data = requests.get(icon_url).content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            icon_label = tk.Label(self.result_frame, image=photo, bg='white')
            icon_label.image = photo
            icon_label.pack(pady=20)
        except:
            icon_label = tk.Label(self.result_frame, text="🌤️", font=('Arial', 100), bg='white')
            icon_label.pack(pady=20)

        # City & Time
        city_text = f"{data['name']}, {data['sys']['country']}"
        tk.Label(self.result_frame, text=city_text, font=('Arial', 32, 'bold'),
                 bg='white').pack(pady=10)

        time_text = datetime.now().strftime("%I:%M %p | %A, %d %B %Y")
        tk.Label(self.result_frame, text=time_text, font=('Arial', 16),
                 bg='white').pack()

        # Temperature
        temp = data['main']['temp']
        unit = "°C" if self.is_metric else "°F"
        tk.Label(self.result_frame, text=f"{temp:.1f}{unit}",
                 font=('Arial', 72, 'bold'), bg='white', fg='#059669').pack(pady=20)

        # Description
        desc = data['weather'][0]['description'].title()
        tk.Label(self.result_frame, text=desc, font=('Arial', 24, 'bold'),
                 bg='white').pack(pady=(0, 30))

        # Stats grid
        stats_frame = tk.Frame(self.result_frame, bg='white')
        stats_frame.pack()

        stats = [
            (f"💧 Humidity: {data['main']['humidity']}%", 3),
            (f"💨 Wind: {data['wind']['speed']:.1f} m/s", 3),
            (f"📊 Pressure: {data['main']['pressure']} hPa", 3)
        ]

        for text, pady in stats:
            tk.Label(stats_frame, text=text, font=('Arial', 16, 'bold'),
                     bg='white').pack(pady=pady)

        self.debug_label = tk.Label(self.result_frame, text=f"✅ Weather loaded for {city}!",
                                    font=('Arial', 14), fg='green', bg='white')
        self.debug_label.pack(pady=20)

    def toggle_units(self):
        self.is_metric = not self.is_metric
        unit_text = "°C" if not self.is_metric else "°F"
        self.unit_btn.config(text=unit_text)
        city = self.city_entry.get().strip()
        if city:
            self.get_weather()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = WeatherPro()
    app.run()
