from redis import Redis
from rq import Queue

class WeatherStationMonitor:
    def __init__(self):
        self.redis_conn = Redis() #łączymy z redisem
        self.queue = Queue('weather_station', connection=self.redis_conn) #tworzymy kolejkę
        self.monitored_stations = set() #tworzymy listę stacji monitorujących

    def add_station(self, station_id):
        self.monitored_stations.add(station_id)
        print(f"dodano stację: {station_id}")


if __name__ == "__main__":
    monitor = WeatherStationMonitor()
    monitor.add_station("STACJA001")

