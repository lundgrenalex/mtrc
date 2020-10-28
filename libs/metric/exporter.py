from libs.storage import mongodb
import json

'''
FORMAT: https://prometheus.io/docs/instrumenting/exposition_formats/#basic-info
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
    db = mongodb.connect()
    result = ''
    metrics = [metric for metric in db.mtrc.metrics.find()]
    for metric in metrics:
        if 'description' in metric:
            result += f"# HELP {metric['name']} {metric['description']}\n"
            result += f"# TYPE {metric['name']} {metric['type']}\n"
        result += f"{metric['name']}_{metric['type']}{get_labels_string(metric['labels'])} {metric['value']}\n"
    return result


def drop_all_metrics() -> bool:
    '''drop all metrics'''
    db = mongodb.connect()
    return db.drop_database('mtrc')
