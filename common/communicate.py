# !/usr/bin/env python

# External Dependencies:
# 1) requests -> https://github.com/requests/requests/
# 2) websocket-client -> https://github.com/websocket-client/websocket-client

#
# Imports
#
try:
    import requests
    import ssl
    from  websocket import create_connection
    from common import view
except ImportError:
    raise ImportError("Import failed to load in communicate.py.")


#
# Create HTTP URL
#
def create_http_url(hostname, endpoint, endpoint_name, account_id, query):
    base_url = "https://" + hostname + "/v3/accounts/" + account_id
    if endpoint == "status":
        if endpoint_name == "get_service_status":
            return "http://" + hostname + "/api/v1/services/" + query
        else:
            raise ValueError("Endpoint name is not valid.")
    elif endpoint == "account":
        if endpoint_name == "get_account_summary":
            return base_url + "/summary"
        elif endpoint_name == "get_account_instruments":
            return base_url + "/instruments?instruments=" + query
        else:
            raise ValueError("Endpoint name is not valid.")
    elif endpoint == "order":
        if endpoint_name == "post_order":
            return base_url + "/orders"
        else:
            raise ValueError("Endpoint name is not valid.")
    elif endpoint == "position":
        if endpoint_name == "get_open_positions":
            return base_url + "/openPositions"
        else:
            raise ValueError("Endpoint name is not valid.")
    elif endpoint == "pricing":
        if endpoint_name == "get_pricing":
            return base_url + "/pricing?instruments=" + query
        else:
            raise ValueError("Endpoint name is not valid.")
    else:
        raise ValueError("Endpoint is not valid.")


#
# Create WS URL
#
def create_ws_url(hostname, endpoint, endpoint_name, query):
    base_url = "wss://" + hostname
    if endpoint == "logic":
        if endpoint_name == "get_historical_data":
            return base_url + query
        elif endpoint_name == "get_current_data":
            return base_url + query
        else:
            raise ValueError("Endpoint name is not valid.")
    else:
        raise ValueError("Endpoint is not valid.")


#
# Send HTTP Request
# https://github.com/requests/requests/
#
def send_http_request(http_type, url, headers, timeout, payload):
    if http_type == "get":
        response = requests.get(url, headers = headers, timeout = timeout)
    elif http_type == "post":
        response = requests.post(url, headers = headers, timeout = timeout, json = payload)
    else:
        raise ValueError("Request type is not valid.")
    if response.raise_for_status():
        raise ValueError("Send request failed.")
    return response


#
# Send WS Request
# https://github.com/websocket-client/websocket-client
# Use http://www.websocket.org/echo.html to validate!
#
def send_ws_request(url):
    wss = create_connection(url, sslopt = {"check_hostname": False,
                                           "ca_certs": ssl.get_default_verify_paths().cafile})
    response = wss.recv()
    wss.close()
    return response
