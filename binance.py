from requests import request

class Binance:

    def __init__(self) -> None:
        self.url = "https://api.binance.com"
    
    def call(self, method: str, path: str):
        return request(method=method, url=f"{self.url}{path}").json()
    
    def get_price(self, base="BTC", quote="BRL"):
        return self.call("GET", f"/api/v3/ticker/price?symbol={base}{quote}")