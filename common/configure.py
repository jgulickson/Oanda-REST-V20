# !/usr/bin/env python

#
# Configuration Class
#
class Configuration:
    def __init__(self):
        self._content = None

        self.account_id = None
        self._api_token = None
        self.trading_hostname = None
        self.status_hostname = None
        self.status_id = None
        self.timeout = None
        self.email_sender = None
        self.email_recipient = None
        self.email_password = None
        self.email_smtp_address = None
        self.email_smtp_port = None
        self._request_datetime_format = None
        self.request_headers = None
        self.data_hostname = None

    #
    # Get Configuration
    #
    def get_config(self, filename):
        try:
            with open(filename, "r") as file:
                self._content = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError("No file named: \"" + filename + "\" in current directory.")
        except PermissionError:
            raise PermissionError("Insufficient permissions for file \"" + filename + "\" in current directory.")
        print("get_config completed")

    #
    # Store Configuration
    #
    def set_config(self):
        try:
            self.account_id = str(self._content[0]).strip()
            self._api_token = str(self._content[1]).strip()
            self.trading_hostname = str(self._content[2]).strip().lower()
            self.status_hostname = str(self._content[3]).strip().lower()
            self.status_id = str(self._content[4]).strip().lower()
            self.timeout = int(self._content[5])
            self.email_sender = str(self._content[6]).strip().lower()
            self.email_recipient = str(self._content[7]).strip().lower()
            self.email_password = str(self._content[8]).strip()
            self.email_smtp_address = str(self._content[9]).strip().lower()
            self.email_smtp_port = int(self._content[10])
            self._request_datetime_format = str(self._content[11]).strip().upper()
            self.request_headers = {"Authorization": "Bearer " + self._api_token,
                                    "Content_Type": "application/json",
                                    "Accept-Datetime-Format": self._request_datetime_format}
            self.data_hostname = str(self._content[12]).strip().lower()
        except ValueError:
            raise ValueError("Configuration file is not valid.")
        print("set_config completed")

    #
    # Validate Configuration
    #
    def validate_config(self):
        #
        # TODO (Improve validation logic)
        #
        assert (self.account_id is not None), "Account ID is not valid."
        assert (self._api_token is not None), "API token is not valid."
        assert (self.trading_hostname == "api-fxpractice.oanda_ep.com" and "api-fxtrade.oanda_ep.com"), \
            "Trading hostname is not valid."
        assert (self.status_hostname is not "api-status.oanda_ep.com"), "Status hostname is not valid."
        assert (self.status_id == "fxtrade-practice-rest-api" and "fxtrade-rest-api"), "Status ID is not valid."
        assert (self.timeout is not None), "Timeout is not valid."
        assert ("@" in self.email_sender), "Email sender is not valid."
        assert ("@" in self.email_recipient), "Email recipient is not valid."
        assert (self.email_password is not None), "Email password is not valid."
        assert (self.email_smtp_address is not None), "Email SMTP address is not valid."
        assert (self.email_smtp_port is not None), "Email SMTP port is not valid."
        assert (self._request_datetime_format == "RFC3339" and "UNIX"), "DateTime format is not valid."
        assert (self.request_headers is not None), "Headers are not valid."
        assert (self.data_hostname is not None), "Data hostname is not valid."
        print("validate_config completed")
