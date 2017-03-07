from src.msg import warning
from src.views.tests import BaseTest


class TestGetEmployees(BaseTest):
    """Tests for getting all employee profiles."""

    def setUp(self):
        super().setUp()
        self.url = '/employees?page_number={0}&page_size={1}'

    def test_get_employees(self):
        res = self.test_app.get(self.url.format(1, 2))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(self.get_response_msg(res), warning.NO_DATA)

        self.insert_employee()
        res = self.test_app.get(self.url.format(1, 2))
        self.assertEqual(res.status_code, 200)

    def test_no_page_number(self):
        res = self.test_app.get(self.url.format(0, 2))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(self.get_response_msg(res), warning.NO_PAGE)

    def test_invalid_page_number(self):
        self.insert_employee()
        res = self.test_app.get(self.url.format(5, 2))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(self.get_response_msg(res), warning.INVALID_PAGE)


class TestGetEmployee(BaseTest):
    """Tests for getting specific employee profile."""

    def test_get_employee(self):
        self.insert_employee()
        res = self.test_app.get('/employee/{id}'.format(id=1))
        self.assertEqual(res.status_code, 200)
