from abc import ABC, abstractmethod
from entities.erequest import Erequest
from entities.manager import Manager
from entities.employee import Employee


class ErequestDAO(ABC):

    @abstractmethod
    def create_request(self, erequest: Erequest) -> Erequest:
        pass

    @abstractmethod
    def get_all_requests_by_eid(self, employee_id) -> [Erequest]: #by FK
        pass

    @abstractmethod
    def get_all_requests(self) -> [Erequest]:
        pass


    @abstractmethod
    def update_request(self, erequest: Erequest, rstatus: str, message: str) -> Erequest:
        pass

    @abstractmethod
    def get_request_by_rid(self, erequest_id: int) -> Erequest:
        pass

    # for statistics
    @abstractmethod
    def get_report_for_all(self) -> [dict]:
        pass



