# Для работы программы:
# запустить программу и ввести город для просмотра в открывшееся поле.

# Импортируем необходимые библиотеки
import tkinter as tk
from tkinter import messagebox

# Импортируем библиотеку для работы с API
import requests


# Функция для получения погоды в указанном городе
def get_weather_info(city):
    # Ключ API для работы с OpenWeatherMap
    api_key = 'f0214cbb2b084cb2a1ab9a2d190d1884'
    # URL API для получения погоды
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    # Параметры запроса
    params = {
        'q': city,  # город для прогноза погоды
        'appid': api_key,  # ключ API
        'units': 'metric'  # единицы измерения температуры
    }
    # Отправляем запрос и получаем ответ
    response = requests.get(base_url, params=params)
    # Если статус ответа равен 200, значит запрос выполнен успешно
    if response.status_code == 200:
        # Преобразуем ответ в JSON-формат
        data = response.json()
        # Возвращаем данные о погоде
        return data
    else:
        # Если статус ответа не равен 200, возвращаем None
        return None


# Функция для отображения информации о погоде
def display_weather_info(data):
    # Если данные о погоде не None, отображаем информацию в окне сообщений
    if data is not None:
        # Получаем данные о городе, стране, температуре, описании погоды, влажности, скорости ветра и давлении
        city_name = data['name']
        country_code = data['sys']['country']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']

        # Отображаем информацию в окне сообщений
        messagebox.showinfo(
            'Weather Information',
            f'City: {city_name}, {country_code}\nTemperature: {temperature}°C\nDescription: '
            f'{description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nPressure: {pressure} hPa\nSunrise: '
            f'{sunrise}\nSunset: {sunset}'
        )
    else:
        # Если данные о погоде None, отображаем сообщение об ошибке
        messagebox.showerror('Error', 'Failed to fetch weather information. Please try again.')


# Главная функция программы
def main():
    # Создаем главное окно приложения
    root = tk.Tk()
    # Задаем заголовок окна
    root.title('Weather Information')

    # Создаем элемент интерфейса для ввода города
    city_label = tk.Label(root, text='Введите город')
    # Добавляем элемент интерфейса на экран
    city_label.pack()

    # Создаем элемент интерфейса для ввода города
    city_entry = tk.Entry(root, bg='black', fg='white')
    # Добавляем элемент интерфейса на экран
    city_entry.pack()

    # Создаем кнопку для получения погоды
    submit_button = tk.Button(root, text='Get Weather',
                              command=lambda: display_weather_info(get_weather_info(city_entry.get())))
    # Добавляем кнопку на экран
    submit_button.pack()

    # Запускаем главный цикл обработки событий
    root.mainloop()


# Запускаем программу
if __name__ == '__main__':
    main()
