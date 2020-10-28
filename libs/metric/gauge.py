from libs.storage import mongodb
import time


def update(metric: dict) -> dict:

    db = mongodb.connect()
    current_time = int(time.time())

    saved_metric = db.mtrc.metrics.find_one({
        'type': 'gauge',
        'name': metric['name'],
        'labels': metric['labels'],
    })

    document = {
        'type': 'gauge',
        'name': metric['name'],
        'labels': metric['labels'],
        'value': float(metric['value']),
        'date': current_time,
    }

    if 'description' in metric:
        document['description'] = metric['description']

    if not saved_metric:
        db.mtrc.metrics.insert_one(document)
        return True

    db.mtrc.metrics.update_one({'_id': saved_metric['_id']}, {'$set': {
            'date': current_time,
            'value': float(metric['value']),
    }})
    return True


def remove(metric_name: str) -> bool:
    db = mongodb.connect()
    db.mtrc.metrics.remove({'type': 'gauge', 'name': metric['name']})
    return True
