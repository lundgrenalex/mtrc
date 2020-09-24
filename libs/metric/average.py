from libs.storage import mongodb
import json
import time


def update(metric: dict) -> bool:

    db = mongodb.connect()
    current_time = int(time.time())

    saved_metric = db.mtrc.metrics.find_one({
        'type': 'average',
        'name': metric['name'],
        'labels': metric['labels'],
        'average': metric['average'],
    })

    if not saved_metric:
        db.mtrc.metrics.insert_one({
            'type': 'average',
            'name': metric['name'],
            'labels': metric['labels'],
            'average': int(metric['average']),
            'description': metric['description'],
            'values': [{
                'date': int(metric['date']),
                'value': float(metric['value']),
            }],
            'value': float(metric['value']),
            'date': current_time,
        })
        return True

    # update range
    saved_metric['values'].append({
        'value': metric['value'],
        'date': metric['date'],
    })

    # remove old
    # filter range by average timeshist
    new_values = []
    for i in range(len(saved_metric['values'])):
        if saved_metric['values'][i]['date'] + saved_metric['average'] > current_time:
            new_values.append(saved_metric['values'][i])
    saved_metric['values'] = new_values

    # count average value and actual range
    saved_metric['value'] = sum([
        v['value'] for v in saved_metric['values']
    ]) / len(saved_metric['values'])

    # touch date
    saved_metric['date'] = current_time

    # store new data
    db.mtrc.metrics.update_one({'_id': saved_metric['_id']}, {
        '$set': saved_metric
    })

    return True


def remove(metric_name: str) -> bool:
    db = mongodb.connect()
    db.mtrc.metrics.remove({'type': 'average', 'name': metric['name']})
    return True
