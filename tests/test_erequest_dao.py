from daos.erequest_dao import ErequestDAO
from entities.erequest import Erequest
from exceptions.resource_not_found import ResourceNotFound
from daos.erequest_dao_postgres import ErequestDaoPostgres
from entities.erequest import Erequest


erequest_dao: ErequestDAO = ErequestDaoPostgres()

test_request = Erequest(0, 110, "Expense test", "pending", "nc", 1)
test_request2 = Erequest(0, 110, "Expense test", "pending", "nc", 100)
erequest_dao.create_request(test_request)


class TestErequestDao:

    def test_create_request(self):
        test = erequest_dao.create_request(test_request)
        assert test.erequest_id != 0

    def test_get_all_requests_by_eid(self) -> [Erequest]:  # eid= employee_id
        all_req = len(erequest_dao.get_all_requests_by_eid(1))
        erequest_dao.create_request(test_request)
        all_req_p1 = len(erequest_dao.get_all_requests_by_eid(1))
        assert (all_req_p1 - all_req) >= 1

    def test_get_reports_for_all(slef) -> [Erequest]:
        all_req = len(erequest_dao.get_all_requests())
        erequest_dao.create_request(test_request)
        all_req_p1 = len(erequest_dao.get_all_requests())
        assert (all_req_p1 - all_req) >= 1

    def test_get_request_by_rid(self) -> Erequest:
        test = erequest_dao.create_request(test_request)
        test1 = erequest_dao.get_request_by_rid(test.erequest_id)
        assert test1.erequest_id == test.erequest_id


    def test_update_request(self):
        test = erequest_dao.create_request(test_request)
        erequest_dao.update_request(test, "approved", "good job")
        assert test.rstatus == "approved" and test.message == "good job"
