# !/usr/bin/env python

#
# Imports
#
try:
    import json
    from oanda_ep import account
    from oanda_ep import pricing
    from common import format
    from common import communicate
except ImportError:
    raise ImportError("Import failed to load in order.py.")


#
# Order Class
#
class Order:
    def __init__(self):
        self.bounds = None

        self.syntax = None

        self._url = None
        self.response = None

    #
    # Set Bounds
    # http://developer.oanda.com/rest-live-v20/order-ep/
    #
    def set_bounds(self, hostname, account_id, headers, timeout, query, is_buy, pip_range):
        p = pricing.Pricing()
        p.get_pricing(hostname, account_id, headers, timeout, query)
        p.set_pricing(query)

        a = account.Account()
        a.get_account_instruments(hostname, account_id, headers, timeout, query)
        a.set_account_instruments()
        pip_location = a.pip_location
        precision = a.display_precision

        if is_buy:
            rate = p.asks_price
            self.bounds = format.format_precision(rate + (pip_range * format.format_pips(pip_location)), precision)
        else:
            rate = p.bids_price
            self.bounds = format.format_precision(rate - (pip_range * format.format_pips(pip_location)), precision)
        print("set_bounds completed")

    #
    # Set Order Syntax
    # http://developer.oanda.com/rest-live-v20/order-ep/
    #
    def set_order_syntax(self, order_type, instrument, units, tif, price_bound, position_fill, ext_comment,
                         ext_tag, ext_id):
        self.syntax = {"order": {
            "type": order_type,
            "instrument": instrument,
            "units": units,
            "timeInForce": tif,
            "priceBound": price_bound,
            "positionFill": position_fill,
            "clientExtensions": {
                "comment": ext_comment,
                "tag": ext_tag,
                "id": ext_id}},
            "takeProfitOnFill": {
                "price": None,
                "timeInForce": None,
                "gtdTime": None,
                "clientExtensions": {
                    "comment": None,
                    "tag": None,
                    "id": None}},
            "stopLossOnFill": {
                "price": None,
                "timeInForce": None,
                "gtdTime": None,
                "clientExtensions": {
                    "comment": None,
                    "tag": None,
                    "id": None}},
            "trailingStopLossOnFill": {
                "distance": None,
                "timeInForce": None,
                "gtdTime": None,
                "clientExtensions": {
                    "comment": None,
                    "tag": None,
                    "id": None}},
            "tradeClientExtensions": {
                "Comment": None,
                "tag": None,
                "id": None}}
        print("set_order_syntax completed")

    #
    # Post Order
    # http://developer.oanda.com/rest-live-v20/order-ep/
    #
    def post_order(self, hostname, account_id, headers, timeout, payload):
        self._url = communicate.create_http_url(hostname, "order", "post_order", account_id, None)
        self.response = communicate.send_http_request("post", self._url, headers, timeout, payload).json()
        print("post_order completed")

    #
    # Validate Post Order
    # http://developer.oanda.com/rest-live-v20/order-ep/
    #
    def validate_post_order(self):
        #
        # TODO (Support different HTTP 201 replies)
        #
        print("validate_post_order completed")
