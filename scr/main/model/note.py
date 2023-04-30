class Note:
    def __init__(self, id, header, body, create_date):
        self.__id = id
        self.__header = header
        self.__body = body
        self.__create_date = create_date

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header):
        self.__header = header

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def create_date(self):
        return self.__create_date

    @create_date.setter
    def create_date(self, create_date):
        self.__create_date = create_date

    def __str__(self):
        return f'{self.id};{self.header};{self.body};{self.create_date}'

