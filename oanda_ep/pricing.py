# !/usr/bin/env python

#
# Imports
#
try:
    import json
    from common import communicate
except ImportError:
    raise ImportError("Import failed to load in pricing.py")


#
# Pricing Class
#
class Pricing:
    def __init__(self):
        self._url = None
        self._response = None

        self.time = None
        self.bids = None
        self.bids_price = None
        self.bids_liquidity = None
        self.asks = None
        self.asks_price = None
        self.asks_liquidity = None
        self.closeout_bid = None
        self.closeout_ask = None
        self.status = None
        self.tradeable = None
        self.instrument = None

    #
    # Get Pricing
    # http://developer.oanda.com/rest-live-v20/pricing-ep/
    #
    def get_pricing(self, hostname, account_id, headers, timeout, query):
        self._url = communicate.create_http_url(hostname, "pricing", "get_pricing", account_id, query)
        self._response = communicate.send_http_request("get", self._url, headers, timeout, None).json()
        print("get_pricing completed")

    #
    # Set Pricing
    # http://developer.oanda.com/rest-live-v20/pricing-ep/
    #
    def set_pricing(self, instrument):
        i = 0
        while i < len(self._response["prices"]):
            if self._response["prices"][i]["instrument"] == instrument:
                try:
                    self.time = str(self._response["prices"][i]["instrument"]).strip()
                    self.bids = self._response["prices"][i]["bids"]
                    self.bids_price = float(self._response["prices"][i]["bids"][0]["price"])
                    self.bids_liquidity = float(self._response["prices"][i]["bids"][0]["liquidity"])
                    self.asks = self._response["prices"][i]["asks"]
                    self.asks_price = float(self._response["prices"][i]["asks"][0]["price"])
                    self.asks_liquidity = float(self._response["prices"][i]["asks"][0]["liquidity"])
                    self.closeout_bid = float(self._response["prices"][i]["closeoutBid"])
                    self.closeout_ask = float(self._response["prices"][i]["closeoutAsk"])
                    self.status = str(self._response["prices"][i]["status"]).strip()
                    self.tradeable = str(self._response["prices"][i]["tradeable"]).strip()
                    self.instrument = str(self._response["prices"][i]["instrument"]).strip().upper()
                except KeyError:
                    raise KeyError("Specified key does not exist")
                except ValueError:
                    raise ValueError("Response is not valid")
                break
            i += 1
        print("set_account_summary completed")

    #
    # Validate Pricing
    # http://developer.oanda.com/rest-live-v20/pricing-ep/
    #
    def validate_pricing(self):
        #
        # TODO (Improve validation logic)
        #
        assert (self.time is not None), "Time is not valid"
        assert (self.bids is not None), "Bids is not valid"
        assert (self.bids_price is not None), "Bids price is not valid"
        assert (self.bids_liquidity is not None), "Bids liquidity is not valid"
        assert (self.asks is not None), "Asks is not valid"
        assert (self.asks_price is not None), "Asks price is not valid"
        assert (self.asks_liquidity is not None), "Asks liquidity is not valid"
        assert (self.closeout_bid is not None), "Closeout Bid not valid"
        assert (self.closeout_ask is not None), "Closeout Ask is not valid"
        assert (self.status is not None), "Status is not valid"
        assert (self.tradeable is not None), "Tradeable is not valid"
        assert (self.instrument is not None), "Instrument is not valid"
        print("validate_pricing completed")
