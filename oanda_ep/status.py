# !/usr/bin/env python

#
# Imports
#
try:
    import json
    from common import communicate
except ImportError:
    raise ImportError("Import failed to load in status.py.")


#
# Status Class
#
class ServiceStatus:
    def __init__(self):
        self._url = None
        self._response = None

        self.description = None
        self.level = None
        self.status = None
        self.id = None

    #
    # Get Service Status
    # http://developer.oanda.com/rest-live-v20/health/
    #
    def get_service_status(self, hostname, account_id, headers, timeout, query):
        self._url = communicate.create_http_url(hostname, "status", "get_service_status", account_id, query)
        self._response = communicate.send_http_request("get", self._url, headers, timeout, None).json()
        print("get_service_status completed")

    #
    # Store Service Status
    # http://developer.oanda.com/rest-live-v20/health/
    #
    def store_service_status(self):
        try:
            self.description = str(self._response["current-event"]["status"]["description"]).strip()
            self.level = str(self._response["current-event"]["status"]["level"]).strip().upper()
            self.status = str(self._response["current-event"]["status"]["id"]).strip().lower()
            self.id = str(self._response["id"]).strip().lower()
        except KeyError:
            raise KeyError("Specified key does not exist in service status _response.")
        except ValueError:
            raise ValueError("Service status _response is not valid.")
        print("store_service_status completed")

    #
    # Validate Service Status
    # http://developer.oanda.com/rest-live-v20/health/
    #
    def validate_service_status(self):
        #
        # TODO (Improve validation logic)
        #
        assert (self.description is not None), "Description is not valid."
        assert (self.level is not None), "Level is not valid."
        assert (self.status == "up" and "down"), "Status is not valid."
        assert (self.id == "fxtrade-practice-rest-api" and "fxtrade-rest-api"), "Service ID is not valid."
        print("validate_service_status completed")
