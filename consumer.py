from kafka import KafkaConsumer
import numpy
import json
import sys 
    
if __name__ == '__main__':
    consumer = KafkaConsumer(sys.argv[2], bootstrap_servers=sys.argv[1])
    print("listening...")
    for msg in consumer:
        b_val = msg.value
        data = json.loads(b_val)
        myArray = numpy.array(data)
        print(myArray) # float64
