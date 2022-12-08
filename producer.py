from kafka import KafkaProducer
import numpy as np
import json
import sys
import time

def send_signal():
    print(sys.argv[1])
    print(sys.argv[2])
    producer = KafkaProducer(bootstrap_servers=sys.argv[1])
    ess_list = []
    with open(sys.argv[3]) as f:
        lines = [line.rstrip('\n') for line in f]
    for line in lines:
        ess = []
        values = line.split(',')
        ess.append(float(values[0]))
        ess.append(float(values[1]))
        ess_list.append(ess)

    for ess in ess_list: 
        json_state = json.dumps(ess)
        data = {
            "valence":None,
            "score": None,
            "state": json_state
        } 
        print(json_state)
        json_object = json.dumps(data).encode("utf-8")
        res = producer.send(sys.argv[2], json_object)
        time.sleep(1)
    
if __name__ == '__main__':
    send_signal()






    
