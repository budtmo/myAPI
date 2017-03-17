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
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name: str, active: bool):
        """
        Constructor
        :param name: employee name
        :param active: position status
        """
        self.name = name
        self.active = active

    def update(self, id: int=None, name: str=None, active: bool=None):
        """
        Update employee profile
        :param id: employee id
        :param name: employee name
        :param active: position status
        """
        if name:
            self.name = name
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
            'active': self.active
        }

    def __repr__(self):
        """
        Convert employee to string
        :return: employee
        """
        return '<Employee(id={id}, name={name}, active={atv}>'.format(
            id=self.id, name=self.name, atv=self.active)
