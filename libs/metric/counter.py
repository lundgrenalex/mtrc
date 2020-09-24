from libs.storage import mongodb
import time


def update(metric: dict) -> dict:

    db = mongodb.connect()
    current_time = int(time.time())

    saved_metric = db.mtrc.metrics.find_one({
        'type': 'counter',
        'name': metric['name'],
        'labels': metric['labels'],
        'average': metric['average'],
    })

    if not saved_metric:
        db.mtrc.metrics.insert_one({
            'type': 'counter',
            'name': metric['name'],
            'labels': metric['labels'],
            'average': int(metric['average']),
            'description': metric['description'],
            'value': float(metric['value']),
            'date': current_time,
        })
        return True

    db.mtrc.metrics.update_one({'_id': saved_metric['_id']}, {
        '$set': {'date': current_time},
        '$inc': {'value': float(metric['value'])},
    })
    return True


def remove(metric_name: str) -> bool:
    db = mongodb.connect()
    db.mtrc.metrics.remove({'type': 'counter', 'name': metric['name']})
    return True
