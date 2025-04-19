from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
TYPE_HOST = Gauge('type_host', 'Determining the server host type', ['type_host'])

def is_container():
    """Checks if the server is running in the container."""
    try:
        with open('/proc/1/cgroup', 'r') as f:
            return 'docker' in f.read()
    except FileNotFoundError:
        return False

def is_virtual_machine():
    """Check if the script is running on a virtual machine."""
    try:
        with open('/proc/cpuinfo', 'r') as f:
            cpuinfo = f.read()
            if 'hypervisor' in cpuinfo.lower():
                return True
    except FileNotFoundError:
        return False
    
def detect_type_host():
    """Detect the type of host."""
    if is_container():
        return 'container'
    elif is_virtual_machine():
        return 'virtual_machine'
    else:
        return 'physical_machine'

def update_metrics():
    """Update the metrics."""
    type_host = detect_type_host()
    TYPE_HOST.clear()
    TYPE_HOST.labels(type_host=type_host).set(1)

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    update_metrics()

    # Generate some requests.
    while True:
        process_request(random.random())