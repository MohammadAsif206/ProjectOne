

from exceptions.resource_not_found import ResourceNotFound

from entities.erequest import Erequest
from daos.erequest_dao import ErequestDAO
from services.erequest_service import ErequestService

from entities.manager import Manager

from entities.employee import Employee
from daos.employee_dao import EmployeeDAO
from services.employee_service import EmployeeService


class ErequestServiceImpl(ErequestService):

    def __init__(self, erequest_dao: ErequestDAO):
        self.erequest_dao = erequest_dao

    def get_all_requests_by_eid(self, employee_id: int) -> [Erequest]:
        return self.erequest_dao.get_all_requests_by_eid(employee_id)

    def create_request(self, erequest: Erequest) -> Erequest:
        return self.erequest_dao.create_request(erequest)

    def get_all_requests(self) -> [Erequest]:
        return self.erequest_dao.get_all_requests()

    def update_request(self, erequest_id: int, rstatus: str, message: str) -> Erequest:
        erequest = self.erequest_dao.get_request_by_rid(erequest_id)
        return self.erequest_dao.update_request(erequest, rstatus, message)

    # for statistics
    def get_report_for_all(self) -> [dict]:
        return self.erequest_dao.get_report_for_all()