
class Employee():
    def __init__(self, employee_id: int=0, first_name: str=null, last_name: str=null, email: str=null):
        self.employee_id = employee_id
        self. first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f'EID: {self.employee_id} First Name: {self.first_name} ' \
               f'Last Name: {self.last_name} Email: { self.email}'

    def as_json_dic(self):
        return {
            'employeeId': self.employee_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email
        }

    def deserialize(as_json_dic):
        employee = Employee(0, '', '', '')
        employee.employee_id = as_json_d["employeeId"]
        employee.first_name = as_json_dic["first_name"]
        employee.last_name = as_json_dic["lastName"]
        employee.email = as_json_dic["email"]

        return employee

