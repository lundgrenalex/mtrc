import json
import unittest
import requests
import time
from random import randrange
from application import app


class TestingCounter(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.fixture = json.dumps({
            "name": "example",
            "labels":{
                "label1": "232",
                "label2": "dsds"
            },
            "value": randrange(0, 101, 2),
            "date": int(time.time()),
            "description": "test data",
        })

    def test_counter(self):
        '''testing counter metric'''
        response = self.app.post(
            '/handler/counter',
            follow_redirects=True,
            data=self.fixture,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
