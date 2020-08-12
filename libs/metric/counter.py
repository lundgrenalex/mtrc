from libs.storage import mongo


def update(metric: dict):
    # https://github.com/prometheus/client_python#counter
    # calc counter metric
    db = mongo.connect()
    result = db.mrtc.metrics.update_one({
        'name': metric['name'],  # must be indexed
        'type': 'counter',       # must be indexed
    }, {
        '$set': {
            'labels': metric['labels'],
            'date': metric['date'],
            'description': metric['description'],
        },
        '$inc': {
            'value': metric['value'],
        }
    }, upsert=True)
    print(result)
