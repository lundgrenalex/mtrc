from libs.storage import mongo

'''
FORMAT
metric_name [
  "{" label_name "=" `"` label_value `"` { "," label_name "=" `"` label_value `"` } [ "," ] "}"
] value [ timestamp ]
'''

def get_labels_string(labels: dict) -> str:
    '''making prometheus format for labels'''
    result =''
    for key, value in labels.items():
        result += f'{key}="{value}", '
    result = '{' + result + '}'
    return result.replace(', }', '}')

def get_metrics() -> str:
    '''get metrics for prometheus'''
    db = mongo.connect()
    result = ''
    metrics = [metric for metric in db.mrtc.metrics.find({}, {'_id': False})]
    for metric in metrics:
        metric_string = f"{metric['name']}{get_labels_string(metric['labels'])} {metric['value']}\n"
        result += metric_string
    return result
