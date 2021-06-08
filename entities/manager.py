class Manager():
    def __init__(self, manager_id: int = 0, first_name: str = null, last_name: str = null, email: str = null):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f'EID: {self.manager_id} First Name: {self.first_name} ' \
               f'Last Name: {self.last_name} Email: {self.email}'

    def as_json_dic(self):
        return {
            'managerId': self.manager_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email
        }

    def deserialize(as_json_dic):
        manager = Manager(0, '', '', '')
        manager.manager_id = as_json_d["managerId"]
        manager.first_name = as_json_dic["firstName"]
        manager.last_name = as_json_dic["lastName"]
        manager.email = as_json_dic["email"]

        return manager
