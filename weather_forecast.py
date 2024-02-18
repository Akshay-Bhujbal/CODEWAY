import requests


def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] != 200:
        print("Error:",data["message"])
    else:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        print(f"Weather in {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind_speed: {wind_speed} m/s")
        print(f"Descripttion: {description.capitalize()}")

def main():
    api_key = "5ed7ff7c61fa2596e0cc5c28f372c3f4"
    city = input("Enter City Name: ")
    weather_data = get_weather(api_key,city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()