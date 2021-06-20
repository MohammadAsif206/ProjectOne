from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.manager import Manager
from entities.erequest import Erequest


class EmployeeDAO(ABC):
    @abstractmethod
    def get_all_employees(self) -> list[Employee]:
        pass

    @abstractmethod
    def get_employee_by_eid(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def check_user_credential(self, first_name: str, last_name) -> Employee or Manager:
        pass
