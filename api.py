import requests

class MemeEconomy(object):
	def __init__(self, apikey):
		self.apikey = apikey
	def _checkResponse(self, resp):
		if resp.status_code != 200:
			print("ERROR {} :: {}".format(resp.status_code, 
				resp.text))
		return resp.json()

	def getStocks(self):
		req = requests.get("http://memetrades.com/api/stocks")
		return self._checkResponse(req)
	def buy(self, meme):
		req = requests.get("http://memetrades.com/api/buy",
			params={"api_key":self.apikey, "meme":meme}
		      )
		return self._checkResponse(req)
	def sell(self, meme):
		req = requests.get("http://memetrades.com/api/sell",
                        params={"api_key":self.apikey, "meme":meme}
                      )
		return self._checkResponse(req)
	def me(self):
		req = requests.get("http://memetrades.com/api/me",
			params={"api_key":self.apikey}
			)
		return self._checkResponse(req)
	def priceHistory(self, meme):
		req = requests.get("http://memetrades.com/api/history",
                        params={"meme":meme}
                      )
		return self._checkResponse(req)
