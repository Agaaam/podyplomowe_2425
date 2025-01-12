"""
# Pobierz i uruchom Zookeepera
docker pull wurstmeister/zookeeper
docker run -d --name zookeeper -p 2181:2181 wurstmeister/zookeeper

# Pobierz i uruchom Kafkę
docker pull wurstmeister/kafka
docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=localhost -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 --link zookeeper:zookeeper wurstmeister/kafka

# Utwórz temat
docker exec kafka kafka-topics.sh --create --topic weather_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

"""