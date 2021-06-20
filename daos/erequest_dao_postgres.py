from daos.erequest_dao import ErequestDAO
from exceptions.resource_not_found import ResourceNotFound
from utils.connection_util import connection
from typing import List
from abc import ABC
from entities.erequest import Erequest


class ErequestDaoPostgres(ErequestDAO):

    def get_all_requests_by_eid(self, employee_id: int) -> [Erequest]:  # employee_id is referencing employee table
        sql = """ select * from erequest where employee_id =%s order by rstatus"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        erequest = [Erequest(*record) for record in records]
        if len(erequest) == 0:
            raise ResourceNotFound
        return erequest

    def create_request(self, erequest: Erequest) -> Erequest:
        sql = """insert into erequest (amount, reason, rstatus, message, employee_id)
                 values(%s, %s, %s,%s, %s) returning erequest_id"""
        cursor = connection.cursor()
        cursor.execute(sql, [erequest.amount, erequest.reason, erequest.rstatus,
                             erequest.message, erequest.employee_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFound
        erequest.erequest_id = record[0]
        return erequest

    def get_all_requests(self) -> [Erequest]:
        sql = """select * from erequest order by erequest_id"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        if len(records) == 0:
            raise ResourceNotFound
        erequest = [Erequest(*record) for record in records]
        return erequest

    def update_request(self, erequest: Erequest, rstatus: str, message: str) -> Erequest:
        sql = """update erequest set rstatus =%s, message =%s where erequest_id =%s returning rstatus , message"""
        cursor = connection.cursor()
        cursor.execute(sql, [rstatus, message, erequest.erequest_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFound
        erequest.rstatus = record[0]  # 0
        erequest.message = record[1]  # 1
        return erequest

    def get_request_by_rid(self, erequest_id: int) -> Erequest:
        sql = """select * from erequest where erequest_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [erequest_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFound
        erequest = Erequest(*record)
        return erequest

    # for statistics
    def get_report_for_all(self) -> [dict]:
        sql = """select employee.employee_id , employee.first_name , SUM(erequest.amount) as tex_pemp,
                (select sum(erequest.amount) from erequest)as total_sum, 
                (select count(erequest.erequest_id) from erequest where erequest.employee_id = employee.employee_id ) as total_request,
                (select count(erequest_id) from erequest) as total_request
                from employee
                inner join erequest
                on employee.employee_id = erequest.employee_id 
                group by employee.employee_id, employee.first_name"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        if records is None:
            raise ResourceNotFound
        reports = []
        for record in records:
            percentage = round(((record[2] / record[3]) * 100), 2)
            report = {"employeeId": record[0], "firstName": record[1], "amount": record[2], "totalSum": record[3],
                      "percentage": percentage, "trPere": record[4], "tRequest": record[5]}
            reports.append(report)

        return reports
