"""
Sample of Database model.
"""
from src.models import db


class Employee(db.Model):
    """
    Employee class
    """
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

    def __init__(self, name: str, age: int):
        """
        Constructor
        :param name: employee name
        :param age: employee age
        """
        self.name = name
        self.age = age

    def update(self, id: int=None, name: str=None, age: int=None):
        """
        Update employee profile
        :param id: employee id
        :param name: employee name
        :param age: employee age
        """
        if name:
            self.name = name
        if age:
            self.age = age

    def to_dict(self) -> dict:
        """
        Convert employee object to dict
        :return: employee
        """
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

    def __repr__(self):
        """
        Convert employee to string
        :return: employee
        """
        return '<Employee(id={id}, name={name}, age={age}>'.format(id=self.id, name=self.name, age=self.age)
