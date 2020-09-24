# Gauge

Gauge (simple metric) store your metric on every push

## Methods

| method | pathname                      | description   |
| ------ | ----------------------------- | ------------- |
| POST   | /handler/gauge/               | update metric |
| DELETE | /handler/gauge/{metric_name}/ | delete metric |

### Update metric

POST `/handler/gauge/`

#### Metric fieldset format for request

| filed name  | required | type                | example         |
| ----------- | -------- | ------------------- | --------------- |
| name        | yes      | string `^/(a-z_)/*` | my_metric       |
| value       | yes      | number              | 12210912        |
| description | no       | text                | My first metric |
| date        | yes      | timestamp           | 1597462667      |
| labels      | no       | object              | object          |

#### Labels format

```json
"labels": {
    "your_label_name": "your text value",
},
```

## httpie examples (UPDATE METRIC)

### Requet

```bash
http POST http://localhost:8087/handler/gauge/ \
    name='supermetric' \
    value:=345 \
    labels:='{"tool": "HTTPie"}' \
    date:=1234567891 \
    description='Supermetric'
```

### Response

```bash
HTTP/1.0 200 OK
Content-Length: 196
Content-Type: application/json
Date: Wed, 19 Aug 2020 05:24:28 GMT
Server: Werkzeug/0.16.0 Python/3.8.2
```

```json
{
    "date": 1234567891,
    "description": "Supermetric",
    "labels": {
        "tool": "HTTPie"
    },
    "name": "supermetric",
    "type": "gauge",
    "value": 1289
}
```

### Exporter page

```bash
http GET http://127.0.0.1:8087/metrics/
HTTP/1.0 200 OK
Content-Length: 329
Content-Type: text
Date: Wed, 19 Aug 2020 05:30:40 GMT
Server: Werkzeug/0.16.0 Python/3.8.2

# HELP example test data
# TYPE example gauge
example{label1="232", label2="dsds"} 74
# HELP supermetric Supermetric
# TYPE supermetric gauge
supermetric{tool="HTTPie"} 1289
```
