import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is missing!")
        return

    url = f"http: //api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        weather = data["current"]
        print(
            f"Paris, {data["location"]["country"]} - "
            f"{data["location"]["localtime"]}")
        print(
            f"Weather: {weather["temp_c"]}°C, {weather["condition"]["text"]}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
