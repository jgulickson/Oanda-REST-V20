# !/usr/bin/env python

#
# Imports
#
try:
    import json
    from common import communicate
except ImportError:
    raise ImportError("Import failed to load in position.py")


#
# Position Class
#
class Position:
    def __init__(self):
        self._url = None
        self._response = None

        self.positions = False
        self.instrument = None
        self.long = None
        self.long_units = 0
        self.long_average_price = None
        self.long_pl = None
        self.long_resettable_pl = None
        self.long_financing = None
        self.long_trade_ids = None
        self.long_unrealized_pl = None
        self.short = None
        self.long = None
        self.short_units = 0
        self.short_average_price = None
        self.short_pl = None
        self.short_resettable_pl = None
        self.short_financing = None
        self.short_trade_ids = None
        self.short_unrealized_pl = None
        self.pl = None
        self.resettable_pl = None
        self.financing = None
        self.commission = None
        self.unrealized_pl = None

    #
    # Get Open Positions
    # http://developer.oanda.com/rest-live-v20/position-ep/
    #
    def get_open_positions(self, hostname, account_id, headers, timeout):
        self._url = communicate.create_http_url(hostname, "position", "get_open_positions", account_id, None)
        self._response = communicate.send_http_request("get", self._url, headers, timeout, None).json()
        print("get_open_positions completed")

    #
    # Set Open Positions
    # http://developer.oanda.com/rest-live-v20/position-ep/
    #
    def set_open_positions(self, instrument):
        i = 0
        while i < len(self._response["positions"]):
            if self._response["positions"][i]["instrument"] == instrument:
                self.positions = True
                try:
                    self.instrument = str(self._response["positions"][i]["instrument"]).strip().upper()
                    self.long = self._response["positions"][i]["long"]
                    self.long_units = int(self._response["positions"][i]["long"]["units"])
                    self.long_pl = float(self._response["positions"][i]["long"]["pl"])
                    self.long_resettable_pl = float(self._response["positions"][i]["long"]["resettablePL"])
                    self.long_financing = float(self._response["positions"][i]["long"]["financing"])
                    if self.long_units > 0:
                        self.long_average_price = float(self._response["positions"][i]["long"]["averagePrice"])
                        self.long_trade_ids = self._response["positions"][i]["long"]["tradeIDs"]
                    self.long_unrealized_pl = float(self._response["positions"][i]["long"]["unrealizedPL"])
                    self.short = self._response["positions"][i]["short"]
                    self.short_units = int(self._response["positions"][i]["short"]["units"])
                    self.short_pl = float(self._response["positions"][i]["short"]["pl"])
                    self.short_resettable_pl = float(self._response["positions"][i]["short"]["resettablePL"])
                    self.short_financing = float(self._response["positions"][i]["short"]["financing"])
                    if self.short_units > 0:
                        self.short_average_price = float(self._response["positions"][i]["short"]["averagePrice"])
                        self.short_trade_ids = self._response["positions"][i]["short"]["tradeIDs"]
                    self.short_unrealized_pl = float(self._response["positions"][i]["short"]["unrealizedPL"])
                    self.pl = float(self._response["positions"][i]["pl"])
                    self.resettable_pl = float(self._response["positions"][i]["resettablePL"])
                    self.financing = float(self._response["positions"][i]["financing"])
                    self.commission = float(self._response["positions"][i]["commission"])
                    self.unrealized_pl = float(self._response["positions"][i]["unrealizedPL"])
                except KeyError:
                    raise KeyError("Specified key does not exist")
                except ValueError:
                    raise ValueError("Position response is not valid")
                break
            i += 1
        print("set_account_summary completed")

    #
    # Validate Open Positions
    # http://developer.oanda.com/rest-live-v20/position-ep/
    #
    def validate_open_positions(self):
        #
        # TODO (Improve validation logic)
        #
        if self.positions:
            assert (self.instrument is not None), "Instrument is not valid"
            assert (self.long is not None), "Long is not valid"
            assert (self.long_units is not None), "Long units is not valid"
            assert (self.long_pl is not None), "Long PL is not valid"
            assert (self.long_resettable_pl is not None), "Long resettable PL is not valid"
            assert (self.long_financing is not None), "Long financing is not valid"
            if self.long_units > 0:
                assert (self.long_average_price is not None), "Long average price is not valid"
                assert (self.long_trade_ids is not None), "Long trade IDs is not valid"
            assert (self.long_unrealized_pl is not None), "Long unrealized PL is not valid"
            assert (self.short is not None), "Short is not valid"
            assert (self.short_units is not None), "Short units is not valid"
            assert (self.short_pl is not None), "Short PL is not valid"
            assert (self.short_resettable_pl is not None), "Short resettable PL is not valid"
            assert (self.short_financing is not None), "Short financing is not valid"
            if self.short_units > 0:
                assert (self.short_average_price is not None), "Short average price is not valid"
                assert (self.short_trade_ids is not None), "Short trade IDs is not valid"
            assert (self.short_unrealized_pl is not None), "Short unrealized PL is not valid"
            assert (self.pl is not None), "PL is not valid"
            assert (self.resettable_pl is not None), "Resettable PL is not valid"
            assert (self.financing is not None), "Financing is not valid"
            assert (self.commission is not None), "Commission is not valid"
            assert (self.unrealized_pl is not None), "Unrealized PL is not valid"
            print("validate_open_positions completed")
