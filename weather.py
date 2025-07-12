import requests

def get_weather(city, api_key):
    city_name = city.lower()
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        description = data['current']['condition']['text']
        temp = data['current']['temp_c']
        wind = data['current']['wind_kph']

        print(f'Weather in {city.title()}:')
        print(f'Tempereture: {temp} °C')
        print(f'Wind Speed: {wind} Km/hr')
        print(f'Condition: {description}')

    else: 
        print(f'{city_name} Not Found')

def main():
    city = input('Enter City Name: ')
    api_key = '2d3853592cee4f5c8e6214149250107'

    get_weather(city, api_key)

if __name__ == '__main__':
    main()
