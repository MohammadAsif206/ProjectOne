from typing import List
from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.manager import Manager


class EmployeeService(ABC):
    @abstractmethod
    def retrieve_all_employee(self):
        pass

    @abstractmethod
    def retrieve_employee_by_eid(self, employee_id: int):
        pass

    @abstractmethod
    def check_user_credential(self, first_name: str, last_name: str) -> Employee or Manager:
        pass
