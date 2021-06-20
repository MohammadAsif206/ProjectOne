class Erequest:
    def __init__(self, erequest_id: int = 0, amount: int = 0, reason: str = "", rstatus: str = " ", message: str = "",
                 employee_id: int = 0):
        self.erequest_id = erequest_id
        self.amount = amount
        self.reason = reason
        self.rstatus = rstatus
        self.message = message
        self.employee_id = employee_id

    def __str__(self):
        return f'Request ID: {self.erequest_id} Amount: {self.amount} Reason: {self.reason}' \
               f'Status: {self.rstatus} Comment: {self.message} Employee ID: {self.employee_id}'

    def as_json_dic(self):
        return {
            'erequestId': self.erequest_id,
            'amount': self.amount,
            'reason': self.reason,
            'rstatus': self.rstatus,
            'message': self.message,
            'employeeId': self.employee_id
        }

    def deserialize(as_json_dic):
        erequest = Erequest()
        erequest.erequest_id = as_json_dic["erequestId"]
        erequest.amount = as_json_dic["amount"]
        erequest.reason = as_json_dic["reason"]
        erequest.rstatus = as_json_dic["rstatus"]
        erequest.message = as_json_dic["message"]
        erequest.employee_id = as_json_dic["employeeId"]
        return erequest
