import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_info(city):
    api_key = 'f0214cbb2b084cb2a1ab9a2d190d1884'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather_info(data):
    if data is not None:
        city_name = data['name']
        country_code = data['sys']['country']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']

        messagebox.showinfo(
            'Weather Information',
            f'City: {city_name}, {country_code}\nTemperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nPressure: {pressure} hPa\nSunrise: {sunrise}\nSunset: {sunset}'
        )
    else:
        messagebox.showerror('Error', 'Failed to fetch weather information. Please try again.')

def main():
    root = tk.Tk()
    root.title('Weather Information')

    city_label = tk.Label(root, text='Введите город')
    city_label.pack()

    city_entry = tk.Entry(root, bg='black', fg='white')
    city_entry.pack()

    submit_button = tk.Button(root, text='Get Weather', command=lambda: display_weather_info(get_weather_info(city_entry.get())))
    submit_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()