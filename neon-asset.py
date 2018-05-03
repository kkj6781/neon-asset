import requests

class NeonAsset(object):
    """docstring for NeonAsset"""
    def __init__(self):
        super(NeonAsset, self).__init__()
        self.btcusdt = self.get_btc_price_from_binance()

    def get_btc_price_from_binance(self):
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url) 
        return float(response.json()["price"])

    def btc_to_usdt(self, value_in_btc):
        return round(float(value_in_btc) * self.btcusdt, 2)

    def get_alts_from_binance(self, name, amount):
        url = "https://api.binance.com/api/v3/ticker/price?symbol={}BTC".format(name)
        response = requests.get(url).json()["price"]
        alt_usdt = self.btc_to_usdt(response)
        print ("\t{}: ${} x {}".format(name, alt_usdt, amount))
        return float(alt_usdt)

    def get_asset(self, wallet):
        asset = 0
        for key, value in wallet.items():
            asset += self.get_alts_from_binance(key, value) * value
        print ("-------------------")
        print ("Total NEON Assets in USD")
        return round(asset, 2)

    def main(self):
        # Neon
        print("Current Market Prices")
        wallet = { "NEO": xx, "GAS": xx, "RPX": xx, "ONT": xx }
        print ("\t${}".format(self.get_asset(wallet)))

if __name__ == "__main__":
    neon = NeonAsset()
    neon.main() 