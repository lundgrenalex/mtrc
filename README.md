# MTRC is metric exporter for your applications

This exporter read incoming metrics in JSON format and push them to local database.

**Now available only two ways:**
* Counter (total) this metric make increment every execution by your value
* Gauge (simple metric) store your metric on every push

## How to run this exporter:
```bash
make create_venv;
make install_requirements;
. ./setenv.sh;
python3 application.py;
```

## How to store in python:
```python
import json
import requests

metric = {
    "name": "example",
    "labels":{
        "method": "post",
        "endpoint": "/api/cats/",
        "http_code": "200"
    },
    "value": 1,
    "date": 1234567891,  # unix timestamp
    "description": "Your discription!",
}

response = requests.post('http://appdomain/handler/counter', data=json.dumps(metric))
```

## How to handle metric by your Prometheus from this app:
``` bash
curl http://appdomain/metrics

# HELP supermetric_total Multiprocess metric
# TYPE supermetric_total counter
supermetric_total{label1="232",label2="dsds"} 34324.0
```
