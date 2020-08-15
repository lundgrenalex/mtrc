# MTRC is a metric exporter for your applications

This exporter read incoming metrics in JSON format and push them to the local database.

**Now available:**

-   Counter (total) this metric make increment every execution by your value
    -   `http://appdomain/handler/counter`
-   Gauge (simple metric) store your metric on every push
    -   `http://appdomain/handler/gauge`
-   Average value over 30, 60, 120, 180 or 300 seconds
    -   `http://appdomain/handler/average`
    -   Set up your average time in store-request at field `average` with given options and follow your metric at exporter page

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
```

## HOWTO store your data

-   [Python Examples](https://github.com/lundgrenalex/mtrc/wiki/Metrics-primitives-in-MRTC)

## Methods map

| method | pathname                        | description           |
| ------ | ------------------------------- | --------------------- |
| POST   | /handler/counter/               | update counter metric |
| DELETE | /handler/counter/{metric_name}/ | delete counter metric |
| POST   | /handler/gauge/                 | update gauge metric   |
| DELETE | /handler/gauge/{metric_name}/   | delete gauge metric   |
| POST   | /handler/average/               | update average metric |
| DELETE | /handler/average/{metric_name}/ | delete average metric |
| GET    | /metrics/                       | get all metrics       |
| DELETE | /metrics/                       | delete all metrics    |

## HOWTO handle your metrics from Prometheus:

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
