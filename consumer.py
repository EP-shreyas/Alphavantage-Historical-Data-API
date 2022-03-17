from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'kafka-test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer_2 = KafkaConsumer(
    'get_hist',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

def cons():    
    for message in consumer:
        message = message.value
        print(message)
        break

def cons_2():    
    for message in consumer_2:
        message = message.value
        print(message)
        break