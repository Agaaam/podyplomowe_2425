import requests
from redis import Redis

def fetch_weather_data(station_id, red=True):

    try:
        print(f"Pobieranie danych dla stacji {station_id}...")

        response = requests.get(f"http://127.0.0.1:8000/weather/{station_id}")

        if response.status_code == 200:
            data = response.json()
            temp = float(data["temperature"])

            if temp > 30:
                print(f"Wysoka temperatura {temp}'C na stacji {station_id}")

            if red:
                redis_conn = Redis()
                redis_conn.lpush(f"temps:{station_id}", temp)
                redis_conn.ltrim(f"temps:{station_id}",0,99) #komenda mówi o tym jak dużo danych przetrzymuje

            return data


        else:
            print(f"Błąd API, kod odpowiedzi: {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        print(f"nie można połączyć się z API dla stacji {station_id}")
        return None

    except Exception as e:
        pritn(f"Błąd dla stacji {station_id} {e}")
        return None

if  __name__ == "__main__":
    print(fetch_weather_data("STACJA_TESTOWA"))