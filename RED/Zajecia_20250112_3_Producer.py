#Ten kod tworzy nam joby i kolejkuje je. Odpytuje stacje, robi zadanie
import time

from redis import Redis
from rq import Queue
from win32ctypes.pywin32.pywintypes import datetime
from datetime import datetime
from Zajecia_20250112_2_tasks import fetch_weather_data
import time

class WeatherStationMonitor:
    def __init__(self):
        self.redis_conn = Redis() #łączymy z redisem
        self.queue = Queue('weather_station', connection=self.redis_conn) #tworzymy kolejkę
        self.monitored_stations = set() #tworzymy listę stacji monitorujących

    def add_station(self, station_id):
        self.monitored_stations.add(station_id)
        print(f"dodano stację: {station_id}")

    def start_monitoring(self):
        while True:
                timpestamp = datetime.now().strftime("%Y%m%d%H%M%S")

                for station_id in self.monitored_stations:
                    job = self.queue.enqueue(
                        fetch_weather_data,
                        station_id,
                        job_id=f"weather_{station_id}_{timpestamp}",
                        job_timeout = "5m"
                    )
                    print(F"Dodano zadanie: {job.id}")

                time.sleep(60)


if __name__ == "__main__":
    monitor = WeatherStationMonitor()
    monitor.add_station("STACJA001")
    monitor.add_station("STACJA002")

    monitor.start_monitoring()

