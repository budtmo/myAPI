import json

from src.views.tests import BaseTest


class TestInsertEmployee(BaseTest):
    """Tests to create employee profile."""

    def setUp(self):
        super().setUp()
        self.headers = {'Content-Type': 'application/json'}
        self.payload = {'name': 'budi', 'active': True}

    def test_insert_employee(self):
        res = self.test_app.post('/employee', headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 200)

        res = self.test_app.post('/employee', headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 400)
