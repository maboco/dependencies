class Query:
    def __init__(self):
        self.queries = []
    
    def set_package(self, package):
        self.queries.append(package)

    def get_query(self):
        return self.queries
    