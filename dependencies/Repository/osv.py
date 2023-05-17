import requests, json

class Osv():
    def __init__(self) -> None:
        self.url = "https://api.osv.dev/v1/"

    def getUrl(self) -> str:
        return self.url
    
class OsvQuery(Osv):
    def __init__(self, data) -> None:
        super().__init__()
        self.route = "query"
        self.method = "POST"
        self.payload = {data}

    def send_query(self) -> requests:
        return requests.request(method=self.method, url=self.url+self.route, data=self.payload)

class OsvQueryBatch(Osv):
    def __init__(self, payload) -> None:
        super().__init__()
        self.route = "querybatch/"
        self.method = "POST"
        self.payload = { "queries" : payload }

    def get_query_batch(self):
        return self.payload
     
    def send_query(self) -> requests:
        return requests.request(method=self.method, url=self.url+self.route, data=json.dumps(self.payload))

