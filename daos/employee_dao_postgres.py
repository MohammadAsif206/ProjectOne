from typing import List
from entities.employee import Employee
from entities.manager import Manager
from abc import ABC, abstractmethod
from utils.connection_util import connection
from daos.employee_dao import EmployeeDAO
from exceptions.resource_not_found import ResourceNotFound
from exceptions.user_credential_failed import UserCredentialFailError


class EmployeeDaoPostgres(EmployeeDAO):

    def check_user_credential(self, first_name: str, last_name: str) -> Employee or Manager:
        # manager
        sql = """ select * from manager where first_name =%s and 
        last_name =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [first_name, last_name])
        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            manager = Manager(*record)
            return manager

        # employee
        sql = """ select * from employee where first_name = %s and 
                last_name= %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [first_name, last_name])
        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            employee = Employee(*record)
            return employee
        raise UserCredentialFailError

    def get_all_employees(self) -> list[Employee]:
        sql = """select * from employee """
        cursor = connection.cursor()
        cursor.execute(sql)
        all_employee = cursor.fetchall()
        if all_employee is None:
            raise ResourceNotFound
        employees = [Employee(*a_employee) for a_employee in all_employee]
        return employees

    def get_employee_by_eid(self, employee_id: int) -> Employee:
        sql = """select * from employee where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFound
        employee = Employee(*record)
        return employee
