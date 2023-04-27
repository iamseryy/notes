class Note:
    def __init__(self, id, header, body, create_date):
        self.id = id
        self.header = header
        self.body = body
        self.create_date = create_date

    def __str__(self):
        return f'{self.id};{self.header};{self.body};{self.create_date}'

