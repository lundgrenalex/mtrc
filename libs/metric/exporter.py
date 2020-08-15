from libs.storage import redis
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
    r = redis.connect()
    result = ''
    for metric_name in r.keys("*"):
        metric = json.loads(r.get(metric_name))
        metric_string = f"{metric_name}{get_labels_string(metric['labels'])} {metric['value']}\n"
        if metric['description']:
            result += f"# HELP {metric_name} {metric['description']}\n"
        result += f"# TYPE {metric_name} {metric['type']}\n"
        result += metric_string
    return result


def drop_all_metrics() -> bool:
    '''drop all metrics'''
    import redis
    r = redis.Redis()
    return r.flushall()
