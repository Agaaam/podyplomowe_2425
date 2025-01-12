import time
from gc import callbacks

from confluent_kafka import Producer
from datetime import datetime
import json
from pyexpat.errors import messages
import time



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

    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Błąd dostarczenia wiadomości: {err}")
        else:
            print(f"Wiadomość dostarczona do {msg.topic()}")

    def start_monitoring(self):
        while True:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            for station_id in self.monitored_stations:
                message = {
                    'station_id': station_id,
                    'timestamp': timestamp,
                    'action': 'fetch_weather'
                }

                self.producer.produce( #tutaj buforujemy dane, czekają na wysyłke
                    self.topic,
                    json.dumps(message).encode("utf-8"),
                    callback = self.delivery_report #odpowiedź wysyłki do kafki
                )

                print(f"Wysłano zadanie dla stacji: {station_id}")

            self.producer.flush() # Tu wysyłka do kafki następuje
            time.sleep(60)

if __name__ == "__main__":
    monitor = WeatherStationMonitor()
    monitor.add_station("STACJA001")
    monitor.add_station("STACJA002")

    monitor.start_monitoring()

#Weryfikacja czy widzimy to na kafce, sprawdzamy to w cmd wpisują to:
#docker ps - wyświelta listę dockerów
#docker exec -it 3f2f8b605d83 bash - wklejamy w miejsce 3f2f8b605d83 to co pokazało się w  docker ps
#kafka-topics.sh --bootstrap-server localhost:9092 --list
# kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic weather_data - opis topica
#kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic weather_data --sprawdzamy co się wrzuciło

