from src.views.tests import BaseTest


class TestDeleteEmployeeProfile(BaseTest):
    """Tests to delete employee profile."""

    def test_delete_employee(self):
        self.insert_employee()
        res = self.test_app.delete('/employee/{id}'.format(id=1))
        self.assertEqual(res.status_code, 204)
