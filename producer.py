from kafka import KafkaProducer
import numpy as np
import json
import sys

def send_signal():
    print(sys.argv[1])
    print(sys.argv[2])
    producer = KafkaProducer(bootstrap_servers=sys.argv[1])
    arr = np.random.rand(800)
    a = arr.tolist() 
    json_object = json.dumps(a) 
    # print(json_object)
    res = producer.send(sys.argv[2], bytes(json_object, 'utf-8'))
    print(res)
    print("sucess")
    
if __name__ == '__main__':
    send_signal()