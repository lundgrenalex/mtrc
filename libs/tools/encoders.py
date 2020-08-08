import json
import datetime
import decimal


class FlaskEncoder(json.JSONEncoder):
    '''Феншуйное преобразование обьектов в JSON'''
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
