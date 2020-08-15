import json
import unittest
from application import app


class TestingExporter(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_exporter(self):
        '''testing counter metric'''
        response = self.app.get('/metrics', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_remove_all_metrics(self):
        '''testing average metric'''
        response = self.app.delete('/metrics/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
