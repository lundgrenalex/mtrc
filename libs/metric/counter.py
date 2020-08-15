from libs.storage import redis
import json


def update(metric: dict) -> dict:
    r = redis.connect()
    metric['type'] = 'counter'
    metric_name = f"{metric['name']}_total"
    stored_metric = r.get(metric_name)
    if not stored_metric:
        r.set(metric_name, json.dumps(metric))
    else:
        metric['value'] += json.loads(stored_metric)['value']
        r.set(metric_name, json.dumps(metric))
    return json.loads(r.get(metric_name))


def remove(metric_name: str) -> bool:
    r = redis.connect()
    return r.delete(metric_name)
