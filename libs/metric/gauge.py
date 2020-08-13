from libs.storage import redis
import json


def update(metric: dict) -> dict:
    r = redis.connect()
    metric['type'] = 'gauge'
    metric_name = f"{metric['name']}"
    r.set(metric_name, json.dumps(metric))
    return json.loads(r.get(metric_name))
