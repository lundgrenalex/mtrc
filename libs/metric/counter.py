from prometheus_client import (Counter, CollectorRegistry,)


def update(metric_data: dict) -> bool:
    # https://github.com/prometheus/client_python#counter
    # calc counter metric
    registry = CollectorRegistry()
    labels_list = metric_data['labels'].keys()
    metric = Counter(
        metric_data['name'],
        metric_data['description'],
        labels_list,
        registry=registry)
    return metric.labels(**metric_data['labels']).inc(metric_data['value'])
