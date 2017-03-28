"""
Sample of Database model.
"""
from datetime import date, datetime

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
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Enum(Gender.MALE, Gender.FEMALE, name='gender'), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    registered = db.Column(db.DateTime(timezone=True), nullable=False)

    def __init__(self, name: str, gender: str, birthdate: date, active: bool, registered: datetime):
        """
        Constructor
        :param name: employee name
        :param gender: employee gender
        :param birthdate: employee birth date
        :param active: position status
        :param registered: datetime when employee is registered in DB
        """
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.active = active
        self.registered = registered

    def update(self, id: int=None, name: str=None, gender: str=None, birthdate: date=None, active: bool=None,
               registered: datetime=None):
        """
        Update employee profile
        :param id: employee id
        :param name: employee name
        :param gender: employee gender
        :param birthdate: employee birth date
        :param active: position status
        :param registered: datetime when employee is registered in DB
        """
        if name:
            self.name = name
        if gender:
            self.gender = gender
        if birthdate:
            self.birthdate = birthdate
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
            'birthdate': self.birthdate,
            'active': self.active,
            'registered': self.registered
        }

    def __repr__(self):
        """
        Convert employee to string
        :return: employee
        """
        return '<Employee(id={id}, name={name}, gender={gender}, birthdate={birthdate}, active={atv}, ' \
               'registered={registered}>'.format(id=self.id, name=self.name, gender=self.gender,
                                                 birthdate=self.birthdate, atv=self.active, registered=self.registered)
