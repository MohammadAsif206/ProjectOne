from abc import ABC, abstractmethod
from entities.erequest import Erequest
from entities.employee import Employee
from entities.manager import Manager


class ErequestService(ABC):

    @abstractmethod
    def get_all_requests_by_eid(self, employee_id: int) -> [Erequest]:
        pass

    @abstractmethod
    def create_request(self, erequest: Erequest) -> Erequest:
        pass

    @abstractmethod
    def get_all_requests(self) -> [Erequest]:
        pass

    @abstractmethod
    def update_request(self, erequest_id: int, rstatus: str, message: str) -> Erequest:
        pass

    @abstractmethod
    def get_report_for_all(self) -> [dict]:
        pass
