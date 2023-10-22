from requests import request

class Binance:

    def __init__(self) -> None:
        self.url = "https://api.binance.com/api/v3"

    def call(self, method: str, path: str):
        return request(method=method, url=f"{self.url}{path}").json()
    
    def get_ticket(self, base="BTC", quote="BRL"):
        return self.call("GET", f"/ticker/price?symbol={base}{quote}")

    def get_ticker_24h(self, base="BTC", quote="BRL") -> dict:
        return self.call("GET", f"/ticker/24hr?symbol={base}{quote}")
