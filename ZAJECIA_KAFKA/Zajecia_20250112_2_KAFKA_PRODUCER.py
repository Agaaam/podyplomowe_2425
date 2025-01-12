from confluent_kafka import Producer

class WeatherStationMonitor:
    def __init__(self):
        conf = {
            'bootstrap.servers':'localhost:9092'
        }
        self.producer = Producer(conf)
        self.topic = 'weather_data'
        self.monitored_stations = set()

    def add_station(self, station_id):
        self.monitored_stations.add(station_id)
        print(f"dodano stację: {station_id}")


if __name__ == "__main__":
    monitor = WeatherStationMonitor()
    monitor.add_station("STACJA001")
    monitor.add_station("STACJA002")

    #monitor.start_monitoring()