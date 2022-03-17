from time import sleep
from json import dumps
from kafka import KafkaProducer 

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x:dumps(x).encode('utf-8'))


def prod(value):
    producer.send('kafka-test', value=value)
    # sleep(30)

def prod_2(value):
    producer.send('get_hist', value=value)
    # sleep(30)