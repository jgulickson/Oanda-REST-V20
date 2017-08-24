# !/usr/bin/env python

#
# Imports
#
try:
    import json
    from common import communicate
except ImportError:
    raise ImportError("Import failed to load in account.py.")


#
# Account Class
#
class Account:
    def __init__(self):
        self._url = None
        self._response_summary = None
        self._response_instruments = None

        self.alias = None
        self.margin_rate = None
        self.hedging_enabled = None
        self.balance = None
        self.open_trade_count = None
        self.open_position_count = None
        self.pending_order_count = None
        self.pl = None
        self.resettable_pl = None
        self.financing = None
        self.commission = None
        self.unrealized_pl = None
        self.nav = None
        self.margin_used = None
        self.margin_available = None
        self.position_value = None

        self.name = None
        self.display_name = None
        self.pip_location = None
        self.display_precision = None
        self.trade_units_precision = None
        self.minimum_trade_size = None
        self.maximum_position_size = None
        self.maximum_order_units = None

    #
    # Get Account Summary
    # http://developer.oanda.com/rest-live-v20/account-ep/
    #
    def get_account_summary(self, hostname, account_id, headers, timeout):
        self._url = communicate.create_http_url(hostname, "account", "get_account_summary", account_id, None)
        self._response_summary = communicate.send_http_request("get", self._url, headers, timeout, None).json()
        print("get_account_summary completed")

    #
    # Set Account Summary
    # http://developer.oanda.com/rest-live-v20/account-ep/
    #
    def set_account_summary(self):
        try:
            self.alias = str(self._response_summary["account"]["alias"]).strip()
            self.margin_rate = str(self._response_summary["account"]["marginRate"]).strip()
            self.hedging_enabled = str(self._response_summary["account"]["hedgingEnabled"]).strip()
            self.balance = float(self._response_summary["account"]["balance"])
            self.open_trade_count = int(self._response_summary["account"]["openTradeCount"])
            self.open_position_count = int(self._response_summary["account"]["openPositionCount"])
            self.pending_order_count = int(self._response_summary["account"]["pendingOrderCount"])
            self.pl = float(self._response_summary["account"]["pl"])
            self.resettable_pl = float(self._response_summary["account"]["resettablePL"])
            self.financing = float(self._response_summary["account"]["financing"])
            self.commission = float(self._response_summary["account"]["commission"])
            self.unrealized_pl = float(self._response_summary["account"]["unrealizedPL"])
            self.nav = float(self._response_summary["account"]["NAV"])
            self.margin_used = float(self._response_summary["account"]["marginUsed"])
            self.margin_available = float(self._response_summary["account"]["marginAvailable"])
            self.position_value = float(self._response_summary["account"]["positionValue"])
        except KeyError:
            raise KeyError("Specified key does not exist in account summary _response.")
        except ValueError:
            raise ValueError("Account summary _response is not valid.")
        print("set_account_summary completed")

    #
    # Validate Account Summary
    # http://developer.oanda.com/rest-live-v20/account-ep/
    #
    def validate_account_summary(self):
        #
        # TODO (Improve validation logic)
        #
        assert (self.alias is not None), "Alias is not valid."
        assert (self.margin_rate is not None), "Margin rate is not valid."
        assert (self.hedging_enabled is not None), "Hedging enabled is not valid."
        assert (self.balance is not None), "Balance is not valid."
        assert (self.open_trade_count >= 0), "Open trade count is not valid."
        assert (self.open_position_count >= 0), "Open position count is not valid."
        assert (self.pending_order_count >= 0), "Pending Order count is not valid."
        assert (self.pl is not None), "PL is not valid."
        assert (self.resettable_pl is not None), "Resettable PL is not valid."
        assert (self.financing is not None), "Financing is not valid."
        assert (self.commission is not None), "Commission is not valid."
        assert (self.unrealized_pl is not None), "Unrealized PL is not valid."
        assert (self.nav is not None), "NAV is not valid."
        assert (self.margin_used is not None), "Margin used is not valid."
        assert (self.margin_available is not None), "Margin available is not valid."
        assert (self.position_value is not None), "Position value is not valid."
        print("validate_account_summary completed")

    #
    # Get Account Instruments
    # http://developer.oanda.com/rest-live-v20/account-ep/
    #
    def get_account_instruments(self, hostname, account_id, headers, timeout, query):
        self._url = communicate.create_http_url(hostname, "account", "get_account_instruments", account_id, query)
        self._response_instruments = communicate.send_http_request("get", self._url, headers, timeout, None).json()
        print("get_account_instruments completed")

    #
    # Set Account Instruments
    # http://developer.oanda.com/rest-live-v20/account-ep/
    #
    def set_account_instruments(self):
        try:
            self.name = str(self._response_instruments["instruments"][0]["name"]).strip().upper()
            self.display_name = str(self._response_instruments["instruments"][0]["displayName"]).strip().upper()
            self.pip_location = int(self._response_instruments["instruments"][0]["pipLocation"])
            self.display_precision = int(self._response_instruments["instruments"][0]["displayPrecision"])
            self.trade_units_precision = float(self._response_instruments["instruments"][0]["tradeUnitsPrecision"])
            self.minimum_trade_size = float(self._response_instruments["instruments"][0]["minimumTradeSize"])
            self.maximum_position_size = float(self._response_instruments["instruments"][0]["maximumPositionSize"])
            self.maximum_order_units = float(self._response_instruments["instruments"][0]["maximumOrderUnits"])
        except KeyError:
            raise KeyError("Specified key does not exist in account instruments _response.")
        except ValueError:
            raise ValueError("Account instruments _response is not valid.")
        print("set_account_instruments completed")

    #
    # Validate Account Instruments
    # http://developer.oanda.com/rest-live-v20/account-ep/
    #
    def validate_account_instruments(self):
        #
        # TODO (Improve validation logic)
        #
        assert (self.name is not None), "Name is not valid."
        assert (self.display_name is not None), "Display name is not valid."
        assert (self.pip_location is not None), "Pip location is not valid."
        assert (self.display_precision is not None), "Display precision is not valid."
        assert (self.trade_units_precision is not None), "Trade units precision is not valid."
        assert (self.minimum_trade_size is not None), "Minimum trade size is not valid."
        assert (self.maximum_position_size is not None), "Maximum position size is not valid."
        assert (self.maximum_order_units is not None), "Maximum order units is not valid."
        print("validate_account_instruments completed")
