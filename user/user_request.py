class UserRequest:
    def __init__(self):
        self.content = {}

    @property
    def name(self):
        return self.content['name']

    @property
    def email(self):
        return self.content['email']

    @property
    def remarks(self):
        return self.content['remarks']
