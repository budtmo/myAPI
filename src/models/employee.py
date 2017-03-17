"""
Sample of Database model.
"""
from src.models import db


class Employee(db.Model):
    """
    Employee class
    """

    class Gender(object):
        MALE = 'male'
        FEMALE = 'female'

    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.Enum(Gender.MALE, Gender.FEMALE, name='gender'), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name: str, gender: str, active: bool):
        """
        Constructor
        :param name: employee name
        :param gender: employee gender
        :param active: position status
        """
        self.name = name
        self.gender = gender
        self.active = active

    def update(self, id: int=None, name: str=None, gender: str=None, active: bool=None):
        """
        Update employee profile
        :param id: employee id
        :param name: employee name
        :param gender: employee gender
        :param active: position status
        """
        if name:
            self.name = name
        if gender:
            self.gender = gender
        if active is not None:
            self.active = active

    def to_dict(self) -> dict:
        """
        Convert employee object to dict
        :return: employee
        """
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'active': self.active
        }

    def __repr__(self):
        """
        Convert employee to string
        :return: employee
        """
        return '<Employee(id={id}, name={name}, gender={gender}, active={atv}>'.format(
            id=self.id, name=self.name, gender=self.gender, atv=self.active)
