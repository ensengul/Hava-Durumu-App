import tkinter as tk
from tkinter import ttk, messagebox
import requests


API_KEY = "c803fb31269c5e89f40a957471618a5b"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Hata", "Lütfen bir şehir adı girin!")
        return
    
    try:
     
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "tr"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Hata", data.get("message", "Bilinmeyen bir hata oluştu"))
            return
        
    
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        
       
        result_label.config(
            text=f"📍 Şehir: {city_name}\n🌡️ Sıcaklık: {temperature}°C\n☁️ Durum: {weather_description.capitalize()}"
        )
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


window = tk.Tk()
window.title("🌤️ Hava Durumu Uygulaması")
window.geometry("400x300")
window.resizable(False, False)


style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12), padding=5)


title_label = ttk.Label(window, text="Hava Durumu Uygulaması", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


city_frame = ttk.Frame(window)
city_frame.pack(pady=10)

city_label = ttk.Label(city_frame, text="Şehir Adı:")
city_label.grid(row=0, column=0, padx=5)

city_entry = ttk.Entry(city_frame, width=30)
city_entry.grid(row=0, column=1, padx=5)


search_button = ttk.Button(window, text="Hava Durumunu Getir", command=get_weather)
search_button.pack(pady=10)


result_label = ttk.Label(window, text="", font=("Arial", 12), justify="left", background="lightblue", anchor="center")
result_label.pack(pady=20, padx=10, fill="both", expand=True)


window.mainloop()
