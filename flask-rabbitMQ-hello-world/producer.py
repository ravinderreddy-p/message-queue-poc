from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")

topic = client.topics['test']

producer = topic.get_sync_producer()

# producer.produce('test message'.encode('ascii'))

count = 1
while True:
    message = ("hello-" + str(count)).encode('ascii')
    producer.produce(message)
    count += 1



