# !/usr/bin/env python

#
# Imports
#
try:
    from oanda_ep import account
    from oanda_ep import order
    from oanda_ep import position
    from oanda_ep import pricing
    from oanda_ep import status
    from common import configure
    from common import format
    from common import notify
except ImportError:
    raise ImportError("Import failed to load in test-oanda_ep.py")


#
# Variables
# All variables below would typically be created "in code" and thus in order
# to perform a quick test these can be set as desired.
#
_CONFIG_FILENAME = "config.txt"
_RUN_STATUS_TEST = False

_SYMBOL = "EUR_USD"
_ORDER_IS_BUY = True
_ORDER_BOUNDS = 5
_ORDER_TYPE = "MARKET"
_ORDER_UNITS = 1000
_ORDER_TIF = "FOK"
_ORDER_POSITION_FILL = "REDUCE_FIRST"
_ORDER_COMMENT = "Test Comment"
_ORDER_TAG = "Test Tag"
_ORDER_ID = "Test ID"

_EMAIL_BODY = "Test Body"
_EMAIL_SUBJECT = "Test Subject"


#
# Configuration
#
c = configure.Configuration()
c.get_config(_CONFIG_FILENAME)
c.set_config()
c.validate_config()


#
# Status
# Note this endpoint is often inaccessible for extended periods
# and thus unless explicitly requested (_RUN_STATUS = True) won't be tested.
#
if _RUN_STATUS_TEST:
    s = status.ServiceStatus()
    s.get_service_status(c.status_hostname,
                         c.account_id,
                         c.request_headers,
                         c.timeout,
                         c.status_id)
    s.store_service_status()
    s.validate_service_status()


#
# Account
#
a = account.Account()
a.get_account_summary(c.trading_hostname,
                      c.account_id,
                      c.request_headers,
                      c.timeout)
a.set_account_summary()
a.validate_account_summary()
a.get_account_instruments(c.trading_hostname,
                          c.account_id,
                          c.request_headers,
                          c.timeout,
                          format.format_instrument_oanda(_SYMBOL))
a.set_account_instruments()
a.validate_account_instruments()

#
# Position
#
po = position.Position()
po.get_open_positions(c.trading_hostname,
                      c.account_id,
                      c.request_headers,
                      c.timeout)
po.set_open_positions(format.format_instrument_oanda(_SYMBOL))
po.validate_open_positions()


#
# Pricing
#
pr = pricing.Pricing()
pr.get_pricing(c.trading_hostname,
               c.account_id,
               c.request_headers,
               c.timeout,
               format.format_instrument_oanda(_SYMBOL))
pr.set_pricing(format.format_instrument_oanda(_SYMBOL))
pr.validate_pricing()


#
# Order
#
o = order.Order()
o.set_bounds(c.trading_hostname,
             c.account_id,
             c.request_headers,
             c.timeout,
             format.format_instrument_oanda(_SYMBOL),
             _ORDER_IS_BUY,
             _ORDER_BOUNDS)
o.set_order_syntax(_ORDER_TYPE,
                   format.format_instrument_oanda(_SYMBOL),
                   _ORDER_UNITS,
                   _ORDER_TIF,
                   o.bounds,
                   _ORDER_POSITION_FILL,
                   _ORDER_COMMENT,
                   _ORDER_TAG,
                   _ORDER_ID)
o.post_order(c.trading_hostname,
             c.account_id,
             c.request_headers,
             c.timeout,
             o.syntax)


#
# Notify
#
n = notify.Notify()
n.compose_email(c.email_sender, c.email_recipient, _EMAIL_SUBJECT, _EMAIL_BODY)
n.send_email(c.email_password, c.email_smtp_address, c.email_smtp_port)
