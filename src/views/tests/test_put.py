import json

from src.views.tests import BaseTest


class TestUpdateEmployeeProfile(BaseTest):
    """Tests to update employee profile."""

    def setUp(self):
        super().setUp()
        self.headers = {'Content-Type': 'application/json'}
        self.url = '/employee/{id}'.format(id=1)
        self.payload = {'name': 'utomo'}

    def test_update_employee(self):
        res = self.test_app.put(self.url, headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 404)

        self.insert_employee()
        res = self.test_app.put(self.url, headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 201)
