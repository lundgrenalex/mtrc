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
