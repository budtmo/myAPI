from unittest import TestCase


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        from src.app import application
        from src.models import db
        from src import settings
        application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{0:s}:{1:s}@{2:s}:{3:d}/{4:s}'.format(
            settings.DB_USER, settings.DB_PASS, settings.DB_HOST, settings.DB_PORT, settings.DB_NAME)
        application.config['TESTING'] = True

        db.init_app(application)
        db.create_all(app=application)

        cls.test_app = application.test_client()
        cls.db = db
        cls.application = application

    def setUp(self):
        self.db.create_all(app=self.application)

    def tearDown(self):
        self.db.drop_all(app=self.application)

    def get_response_msg(self, res):
        import json
        content = json.loads(res.data.decode())
        msg = content.get('detail').get('message')
        return msg

    def insert_employee(self):
        with self.application.app_context():
            from src.models.employee import Employee
            new_employee = Employee(name='budi', age=27)
            self.db.session.add(new_employee)
            self.db.session.commit()
