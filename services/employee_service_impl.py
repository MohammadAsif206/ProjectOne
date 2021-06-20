from entities.employee import Employee
from daos.employee_dao import EmployeeDAO
from services.employee_service import EmployeeService


class EmployeeServiceImpl(EmployeeService):

    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    def check_user_credential(self, first_name: str,  last_name: str) -> Employee or Manager:
        return self.employee_dao.check_user_credential(first_name, last_name)

    def retrieve_all_employee(self):
        return self.employee_dao.get_all_employees()

    def retrieve_employee_by_eid(self, employee_id: int):
        return self.employee_dao.get_employee_by_eid(employee_id)
