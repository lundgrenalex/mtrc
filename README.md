# MTRC is a metric exporter for your applications

This exporter read incoming metrics in JSON format and push them to the local database.

**Now available only two ways:**
* Counter (total) this metric make increment every execution by your value
  * `http://appdomain/handler/counter`
* Gauge (simple metric) store your metric on every push
  * `http://appdomain/handler/gauge`

## How to run this exporter:
```bash
make create_venv;
make install_requirements;
. ./setenv.sh;
python3 application.py;

* Serving Flask app "libs.routes" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
2020-08-08 08:35:52,849 INFO     werkzeug:  * Running on http://127.0.0.1:8087/ (Press CTRL+C to quit)
2020-08-08 08:35:52,850 INFO     werkzeug:  * Restarting with stat
2020-08-08 08:35:53,093 WARNING  werkzeug:  * Debugger is active!
2020-08-08 08:35:53,094 INFO     werkzeug:  * Debugger PIN: 130-633-358
```

## Configs
```python
# config.py

flask = {
    'host': '127.0.0.1',
    'port': '8087',
    'debug': True,
}

prometheus = {
    'db_pathname': './tmp',
    'remove_database': True,
}
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

## Features for the future
* aggregation metrics support
* production-ready Environment
* gunicorn support
* full test coverage
* logging
* Sentry support
* Logstash support
* in-memory driver for high load installation
* charts for k8s
* basic security
* nginx config for reverse proxy
* udp support
* vault support
