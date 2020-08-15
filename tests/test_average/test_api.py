import json
import unittest
import requests
import time
from random import randrange
from application import app


class TestingAverage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.fixture = json.dumps({
            "name": "example",
            "average": 60,
            "labels":{
                "label1": "232",
                "label2": "dsds"
            },
            "value": randrange(0, 101, 2),
            "date": int(time.time()),
            "description": "test average data",
        })

    def test_average_update(self):
        '''testing average metric'''
        response = self.app.post(
            '/handler/average',
            follow_redirects=True,
            data=self.fixture,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_average_remove(self):
        '''testing average metric'''
        response = self.app.delete(
            '/handler/average/test_metric/',
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
