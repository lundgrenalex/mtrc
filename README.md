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

## API methods

| method | pathname                        | description       | httpie examples                  |
| ------ | ------------------------------- | ----------------- | -------------------------------- |
| POST   | /handler/counter/               | update counter    | [read](/docs/httpie/counter.md)  |
| DELETE | /handler/counter/{metric_name}/ | delete counter    | [read](/docs/httpie/counter.md)  |
| POST   | /handler/gauge/                 | update gauge      | [read](/docs/httpie/gauge.md)    |
| DELETE | /handler/gauge/{metric_name}/   | delete gauge      | [read](/docs/httpie/gauge.md)    |
| POST   | /handler/average/               | update average    | [read](/docs/httpie/average.md)  |
| DELETE | /handler/average/{metric_name}/ | delete average    | [read](/docs/httpie/average.md)  |
| GET    | /metrics/                       | get all metrics   | [read](/docs/httpie/exporter.md) |
| DELETE | /metrics/                       | flush all metrics | [read](/docs/httpie/exporter.md) |
