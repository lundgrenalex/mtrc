from prometheus_client import (Gauge, CollectorRegistry,)


def update(metric_data: dict) -> bool:
    # https://github.com/prometheus/client_python#gauge
    # calc counter metric
    registry = CollectorRegistry()
    labels_list = metric_data['labels'].keys()
    metric = Gauge(
        metric_data['name'],
        metric_data['description'],
        labels_list,
        registry=registry,
        multiprocess_mode='livesum') # hack w pids
    return metric.labels(**metric_data['labels']).set(metric_data['value'])


def count_rps(metric_data: dict, butch_time: int) -> bool:
    # Howto: (typical)
    # get current timestamp
    # marker_ts exists:
    # - no
    # set marker_ts for metric with this ts
    # inc++ event for gauge
    # - yes
    # get current timestamp >= marker_ts + butch_stime
    # - yes
    # Dump gauge metric to Collector
    # - no
    # inc++ event for gauge
    pass
