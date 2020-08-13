# MTRC is a metric exporter for your applications

This exporter read incoming metrics in JSON format and push them to the local database.

**Now available:**
* Counter (total) this metric make increment every execution by your value
  * `http://appdomain/handler/counter`
* Gauge (simple metric) store your metric on every push
  * `http://appdomain/handler/gauge`
* Average value over 30, 60, 120, 180 or 300 seconds
  * `http://appdomain/handler/average`
  * Set up your average time in store-request at field `average` with given options and follow your metric at exporter page

## How to run this exporter:
```bash
docker-copmose build;
docker-compose up -d;
```

## Configs
```python
# config.py

flask = {
    'host': '127.0.0.1',
    'port': '8087',
    'debug': True,
    'sentry_dsn': None,
}

mrtc = {
    'exporter': {
        'basic_auth_security': {
            'disabled': True,
            'users': {
                'user1': generate_password_hash(''),
            }
        },
    }
}
```

## How to store (httpie):
```bash
http POST http://localhost:8087/handler/counter < tests/metric.json
HTTP/1.0 200 OK
Content-Length: 188
Content-Type: application/json
Date: Thu, 13 Aug 2020 04:27:33 GMT
Server: Werkzeug/0.16.0 Python/3.8.2

{
    "date": 1234567891,
    "description": "Test Metric",
    "labels": {
        "label1": "232",
        "label2": "dsds"
    },
    "name": "supermetric",
    "type": "counter",
    "value": 283.5
}
```

## How to handle metric by your Prometheus from this app:
### Httpie example
```bash
http http://127.0.0.1:8087/metrics/                                
HTTP/1.0 200 OK
Content-Length: 226
Content-Type: text
Date: Thu, 13 Aug 2020 04:29:09 GMT
Server: Werkzeug/0.16.0 Python/3.8.2

# HELP supermetric Test Metric
# TYPE supermetric gauge
supermetric{label1="232", label2="dsds"} 47.25
# HELP supermetric_total Test Metric
# TYPE supermetric_total counter
supermetric_total{label1="232", label2="dsds"} 283.5
```
