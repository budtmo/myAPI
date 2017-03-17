"""
Employee endpoints.
"""
import logging

from connexion import NoContent

from flask import abort

from src import get_number_of_pages
from src.models import db
from src.models.employee import Employee
from src.msg import warning

logger = logging.getLogger('views.employee')


def get_all(page_number: int, page_size: int) -> dict:
    """
    Get all employees
    :param page_number: selected page number
    :param page_size: size of page
    :return: employees
    """
    logger.info('Page number: {num}, page size: {size}'.format(num=page_number, size=page_size))
    if not page_number or not page_size:
        logger.warning(warning.NO_PAGE)
        abort(404, {'message': warning.NO_PAGE})

    employee_query = Employee.query

    num_items = employee_query.count()
    logger.info('Number of items: {item}'.format(item=num_items))
    total_pages = 0
    if num_items > 0:
        total_pages = get_number_of_pages(num_items, page_size)
        logger.info('Total pages: {total}'.format(total=total_pages))
    else:
        logger.warning(warning.NO_DATA)
        abort(404, {'message': warning.NO_DATA})

    if page_number > total_pages:
        logger.warning(warning.INVALID_PAGE)
        abort(404, {'message': warning.INVALID_PAGE})

    employees = employee_query.order_by(Employee.id.asc()).paginate(page=page_number, per_page=page_size,
                                                                    error_out=True)
    logger.info('Employees: {employees}'.format(employees=employees.items))
    return {
        'page': page_number,
        'total_pages': total_pages,
        'employees': [employee.to_dict() for employee in employees.items]
    }


def insert(employee: dict) -> dict:
    """
    Insert a new employee profile
    :return: created employee profile
    """
    logger.info('New employee profile: {profile}'.format(profile=employee))
    if Employee.query.filter(Employee.name == employee.get('name')).first():
        logger.warning(warning.ALREADY_EXISTS)
        abort(400, {'message': warning.ALREADY_EXISTS})
    else:
        employee.pop('id', None)
        db.session.add(Employee(**employee))
        db.session.commit()
        logger.info('Profile saved!')
    return NoContent, 200


def get(employee_id: int):
    """
    Get employee profile by id
    :param employee_id: employee id
    """
    return Employee.query.filter(Employee.id == employee_id).first_or_404().to_dict()


def update(employee_id: int, employee: dict) -> dict:
    """
    Update employee profile by id
    :param employee_id: employee id
    :param employee: employee profile
    :return: updated employee profile
    """
    logger.info('Employee id that want to be updated: {id}'.format(id=employee_id))
    selected_employee = Employee.query.filter(Employee.id == employee_id).first_or_404()
    selected_employee.update(**employee)
    db.session.commit()
    logger.info('Updated!')
    return NoContent, 201


def delete(employee_id: int):
    """
    Delete employee profile by id
    :param employee_id: employee id
    """
    employee = Employee.query.filter(Employee.id == employee_id).first_or_404()
    db.session.delete(employee)
    db.session.commit()
    logger.info('Employee with id \"{id}\" is successfully deleted!'.format(id=employee_id))
    return NoContent, 204
