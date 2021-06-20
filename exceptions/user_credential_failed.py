class UserCredentialFailError(Exception):
    description: str = "Occurs when a either user id or password does not match or both"

    def __str__(self):
        return "Either user id or password, or both do not match the recorded ones"