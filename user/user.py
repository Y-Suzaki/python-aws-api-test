class User:
    def __init__(self):
        self.content = {}

    def __str__(self):
        return str(self.content)

    @property
    def email(self):
        return self.content['email']
