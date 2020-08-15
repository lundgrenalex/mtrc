from libs.storage import redis
from redis import exceptions as redis_exceptions
import json


def update(metric: dict) -> dict:
    r = redis.connect()
    metric['type'] = 'average'
    metric_name = f"{metric['name']}_avg_{metric['average']}"
    metric['value'] = push_and_count(
        metric_name, metric['value'], metric['average'])
    r.set(metric_name, json.dumps(metric))
    return json.loads(r.get(metric_name))


def push_and_count(metric_name: str, value: float, average: int) -> float:
    r = redis.connect(db=1)
    r.expire(metric_name, average)
    r.lpush(metric_name, value)
    elements = [float(item) for item in (r.lrange(metric_name, 0, -1))]
    return sum(elements)/len(elements)


def remove(metric_name: str) -> bool:
    r = redis.connect()
    r.delete(metric_name)
    r = redis.connect(db=1)
    return r.delete(metric_name)
