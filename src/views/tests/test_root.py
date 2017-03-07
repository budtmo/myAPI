from src.views.tests import BaseTest


class TestRoot(BaseTest):
    """Tests for root endpoint."""

    def test_root(self):
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)
