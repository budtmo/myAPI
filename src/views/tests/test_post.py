import json
from datetime import date

from src.models.employee import Employee

from src.views.tests import BaseTest


class TestInsertEmployee(BaseTest):
    """Tests to create employee profile."""

    def setUp(self):
        super().setUp()
        self.headers = {'Content-Type': 'application/json'}
        self.payload = {'name': 'budi', 'gender': Employee.Gender.MALE,
                        'birthdate': date.today().strftime("%B %d, %Y"), 'active': True}

    def test_insert_employee(self):
        res = self.test_app.post('/employee', headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 200)

        res = self.test_app.post('/employee', headers=self.headers, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 400)

    def test_invalid_date(self):
        payload = {'name': 'budi2', 'gender': Employee.Gender.MALE,
                   'birthdate': 'test', 'active': True}
        res = self.test_app.post('/employee', headers=self.headers, data=json.dumps(payload))
        self.assertEqual(res.status_code, 400)
        from sqlalchemy.exc import DataError
        self.assertRaises(DataError)
