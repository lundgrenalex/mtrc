# Average

Set up your average time in store-request at field `average` with given options and follow your metric at exporter page

## Methods

| method | pathname                        | description    |
| ------ | ------------------------------- | -------------- |
| POST   | /handler/average/               | update average |
| DELETE | /handler/average/{metric_name}/ | delete average |

### Update metric

POST `/handler/average/`

#### Metric fieldset format for request

| filed name  | required | type                    | example         |
| ----------- | -------- | ----------------------- | --------------- |
| name        | yes      | string `^/(a-z_)/*`     | my_metric       |
| value       | yes      | number                  | 12210912        |
| average     | yes      | enum[30,60,120,180,300] | 60              |
| description | no       | text                    | My first metric |
| date        | yes      | timestamp               | 1597462667      |
| labels      | no       | object                  | object          |

#### Labels format

```json
"labels": {
    "your_label_name": "your text value",
},
```

## httpie examples (UPDATE METRIC)

### Requet

```bash
http POST http://localhost:8087/handler/average/ \
    name='supermetric' \
    value:=345 \
    average:=30 \
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
    "average": 30,
    "date": 1234567891,
    "description": "Supermetric",
    "labels": {
        "tool": "HTTPie"
    },
    "name": "supermetric",
    "type": "average",
    "value": 411.6666666666667
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
# HELP supermetric_avg_30 Supermetric
# TYPE supermetric_avg_30 average
supermetric_avg_30{tool="HTTPie"} 411.6666666666667
# HELP example_avg_60 test average data
# TYPE example_avg_60 average
example_avg_60{label1="232", label2="dsds"} 22.0
```
