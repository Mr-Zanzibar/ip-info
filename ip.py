import requests
from pyfiglet import Figlet
import folium
import time

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            'IP': response.get('query'),
            'Internet Provider': response.get('isp'),
            'Organization': response.get('org'),
            'Country': response.get('country'),
            'Country Code': response.get('countryCode'),
            'Region Name': response.get('regionName'),
            'City': response.get('city'),
            'ZIP Code': response.get('zip'),
            'Latitude': response.get('lat'),
            'Longitude': response.get('lon'),
            'Time Zone': response.get('timezone'),
            'Language': response.get('as'),
            'AS Number': response.get('as'),
            'AS Name': response.get('asname'),
            'Continent Code': response.get('continent'),
            'Country ISO Code': response.get('countryCode')
        }

        for k, v in data.items():
            print(f'{k}: {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        folium.Marker([response.get('lat'), response.get('lon')], popup=f'{response.get("city")}, {response.get("country")}').add_to(area)
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('A connection error occurred!')
        print('Please check')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred during the request: {e}')

def main():
    f = Figlet(font='slant')
    print(f.renderText('IP Info'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
    time.sleep(100)
