import logging


def get_metric(metric_name: str, raw_metrics: str):
    """Grab selected metric from statsd list of metrcs"""

    def __get_labels(raw_metrics):
        # get labels: cut {, then }
        try:
            labels = {}
            raw_labels = raw_metric.split('{')[-1:][0]
            raw_labels = raw_labels.split('}')[0].split(',')
            for rl in raw_labels:
                parsed_rl = rl.split('=')
                labels[parsed_rl[0]] = parsed_rl[1].replace('"', '')
            return labels
        except Exception as e:
            logging.error(e)
            return {}

    # make rows
    metrics_in_rows = raw_metrics.split('\n')

    # Get raw metric
    raw_metric = [metric for metric in metrics_in_rows if not metric.find(metric_name)][0]

    # get value of metric
    value = raw_metric.split()[-1:][0]

    return {'value': value, 'labels': __get_labels(raw_metrics)}
