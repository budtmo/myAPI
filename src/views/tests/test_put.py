import json

from src.views.tests import BaseTest


class TestUpdateEmployeeProfile(BaseTest):
    """Tests to update employee profile."""

    def setUp(self):
        super().setUp()
        self.headers = {'Content-Type': 'application/json'}
        self.url = '/employee/{id}'.format(id=1)
        self.payload = {'name': 'utomo', 'gender': 'female', 'active': False}

    def test_update_employee(self):
        res = self.test_app.put(self.url, headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 404)

        self.insert_employee()
        res = self.test_app.put(self.url, headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 201)

    def test_invalid_date(self):
        self.insert_employee()
        payload = {'birthdate': 'test'}
        res = self.test_app.put(self.url, headers=self.headers, data=json.dumps(payload))
        self.assertEqual(res.status_code, 400)
        from sqlalchemy.exc import DataError
        self.assertRaises(DataError)
