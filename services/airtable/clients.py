from .operations import Operations

class ClientTable(Operations):
    table_name = 'Client'

    def __init__(self, base):
        super().__init__(base)
