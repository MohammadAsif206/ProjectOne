from daos.erequest_dao import ErequestDAOf
from entities.erequest import Erequest
from exceptions.resource_not_found import ResourceNotFound


class ErequestDaoLocal(ErequestDAOf):
    id_maker = 0
    erequest_table = {}

    def create_request(self, erequest: Erequest) -> Erequest:
        ErequestDaoLocal.id_maker += 1
        erequest.employee_id = ErequestDaoLocal.id_maker
        ErequestDaoLocal.erequest_table[erequest.employee_id] = erequest
        return erequest

    def get_all_requests(self) -> List[Erequest]:
        pass

    def get_request_by_eid(self, employee_id: int) -> Erequest:
        pass

    def update_request(self, erequest: Erequest, employee_id: int, erequest_id: int) -> Erequest:
        pass

    def delete_request(self, erequest_id: int) -> bool:
        pass
