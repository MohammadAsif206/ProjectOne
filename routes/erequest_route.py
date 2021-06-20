from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from werkzeug.exceptions import abort
from exceptions.invalid_prameter import InvalidParameter
from exceptions.resource_not_found import ResourceNotFound
from exceptions.invalid_prameter import InvalidParameter

from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDaoPostgres
from services.employee_service import EmployeeService
from services.erequest_service_impl import ErequestServiceImpl

from entities.erequest import Erequest
from daos.erequest_dao import ErequestDAO
from daos.erequest_dao_postgres import ErequestDaoPostgres
from services.erequest_service import ErequestService
from services.erequest_service_impl import ErequestServiceImpl


erequest_dao: ErequestDAO = ErequestDaoPostgres()
erequest_service = ErequestServiceImpl(erequest_dao)


def create_erequest_route(app: Flask):
    CORS(app)

    @app.route("/requests/<employee_id>", methods=["GET"])
    def get_all_requests_by_eid(employee_id: str): # get all request for one particular employee
        try:
            if not employee_id.isnumeric():
                raise InvalidParameter
            records = erequest_service.get_all_requests_by_eid(employee_id)
            app.logger.info(f'Retrieve all requests related to the employee with ID: {employee_id}')
            return jsonify([r.as_json_dic() for r in records]), 200
        except ResourceNotFound as e:
            return str(e), 404
        except InvalidParameter as e:
            return str(e), 404

    @app.route("/requests", methods=["POST"])
    def post_request():
        try:
            erequest = Erequest.deserialize(request.json)

            erequest_service.create_request(erequest)
            app.logger.info(f'An expense request created with ID: {erequest.erequest_id}')
            return jsonify(erequest.as_json_dic()), 201
        except ResourceNotFound as  e:
            return str(e), 404

    # to render to html
    @app.route("/requests", methods=["GET"])
    def get_all_requests():
        try:
            erequests = erequest_service.get_all_requests()
            app.logger.info(f'A total of {len(erequests)} requested retrieved successfully')
            jsonized = [e.as_json_dic() for e in erequests]
            return jsonify(jsonized), 200
        except ResourceNotFound as e:
            return str(e), 404

    @app.route("/requests/id/<erequest_id>/status/<rstatus>/comment/<message>", methods=["PATCH"])
    def update_request(erequest_id: str, rstatus: str, message: str):
        try:
            if not erequest_id.isnumeric() or not rstatus:
                raise InvalidParameter
            erequest = erequest_service.update_request(int(erequest_id), rstatus, message)
            app.logger.info(f'Request with ID: {erequest_id} updated successfully')
            return jsonify(erequest.as_json_dic()), 200
        except ResourceNotFound as e:
            return str(e), 404
        except InvalidParameter as e:
            return str(e), 404

    # for statics
    @app.route("/reports", methods=["GET"])
    def get_reports_for_all():
        try:
            reports = erequest_service.get_report_for_all()
            app.logger.info(f'Get all expense {len(reports)} reimbursement requests')
            return jsonify(reports), 200
        except ResourceNotFound as  e:
            return str(e), 40


