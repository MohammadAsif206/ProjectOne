from flask import Flask, request, jsonify
from werkzeug.exceptions import abort
from flask_cors import CORS
from exceptions.invalid_prameter import InvalidParameter
from exceptions.resource_not_found import ResourceNotFound
from exceptions.user_credential_failed import UserCredentialFailError

from entities.employee import Employee
from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDaoPostgres
from services.employee_service_impl import EmployeeServiceImpl

employee_dao = EmployeeDaoPostgres()
employee_service = EmployeeServiceImpl(employee_dao)


def create_employee_route(app: Flask):
    CORS(app)

    # log in route to both users: employee and manager
    @app.route("/login/userId/<first_name>/password/<last_name>", methods=["GET"])
    def login(first_name: str, last_name):
        try:
            data = employee_service.check_user_credential(first_name, last_name)
            app.logger.info(f'logged in successfully')
            return jsonify(data.as_json_dic()), 200
        except UserCredentialFailError as  e:
            return str(e), 400

    @app.route("/employee", methods=["GET"])
    def get_all_employee():
        try:
            employees = employee_service.retrieve_all_employee()
            if employees is not None:
                jsonized_employee = [e.as_json_dic() for e in employees]
                return jsonify(jsonized_employee), 200
        except ResourceNotFound as  e:
            return str(e), 404

    @app.route("/employee/<employee_id>", methods=["GET"])
    def get_employee_by_eid(employee_id: str):
        if not employee_id.isalnum():
            raise InvalidParameter
        else:
            try:
                employee = employee_service.retrieve_employee_by_eid(int(employee_id))
                return jsonify(employee.as_json_dic()), 200
            except ResourceNotFound as e:
                return str(e), 404
            except InvalidParameter as e:
                return str(e), 404
