# avenieca-python
Python SDK for publishing state signals to the AveniECA suite.

## Usage

### Stream continuously to a topic
```python
import os
import numpy as np
from avenieca.utils import Config
from avenieca.utils import Signal
from avenieca.producers import Stream

# Define a handler that returns a signal dict like  
# the sample in avenieca.utils.signal

def handler():
    Signal["valence"] = 10
    Signal["state"] = np.array([0.2, 0.3, 0.8])
    return Signal

# Initialize Kafka configuration for the Stream
Config["bootstrap_servers"] = os.environ["KAFKA_URL"]
Config["topic"] = "left_wheel" #digital twin subscriber-topic

#Initialize the Stream object with a sync_rate 
# (the rate at which to publish signals).
stream = Stream(config=Config, sync_rate=1)
stream.publish(handler)
```

### Publish one signal as an event
```python
import os
import numpy as np
from avenieca.utils import Config
from avenieca.utils import Signal
from avenieca.producers import Event

# Initialize Kafka configuration for the Event
Config["bootstrap_servers"] = os.environ["KAFKA_URL"]
Config["topic"] = "left_wheel" #digital twin subscriber-topic

# Define the signal
Signal["valence"] = 9
Signal["state"] = np.array([0.2, 0.3, 0.8])

event = Event(config=Config)
event.publish(Signal)
```

### Consume from kafka topic
```python
import os
import numpy as np
from avenieca.utils import Config
from avenieca.utils.signal import get_state_as_list, get_state_as_array
from avenieca.consumer import Consumer

# Initialize Kafka configuration for the Event
Config["bootstrap_servers"] = os.environ["KAFKA_URL"]
Config["topic"] = "left_wheel" #digital twin subscriber-topic

# Define a handler to process incoming messages
def handler(data):
    valence = data["valence"]
    state = data["state"]
    assert valence == 10
    assert state == "[0.2, 0.3, 0.8]"

client = Consumer(config=Config)
client.consume(handler, True) # pass in handler

# You can use util functions in your handler to 
# convert the state signal from byte string to 
# np.ndarray or python list
def handler(data):
    assert data["valence"] == 10
    assert data["state"] == "[0.2, 0.3, 0.8]"
    get_state_as_list(data)
    assert data["state"] == [0.2, 0.3, 0.8]

def handler(data):
    assert data["valence"] == 10
    assert data["state"] == "[0.2, 0.3, 0.8]"
    get_state_as_array(data)
    assert True, np.array_equal(data["state"], np.array([0.2, 0.3, 0.8]))
```

## Tests
```bash
python -m pytest test/
```

