
class Erequest():
    def __init__(self, erequest_id: int=0, amount: int=0, reason: str=null, rstatus: str=null):
        self.erequest_id = erequest_id
        self.amount = amount
        self.reason = reason
        self.rstatus = rstatus

    def __str__(self):
        return f'Request ID: {self.erequest_id} Amount: {self.amount} Reason: {self.reason}' \
               f'Status: {self.rstatus}'
