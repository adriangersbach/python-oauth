import Settings

from NetworkInterface import NetworkInterface
from OAuthInterface import OAuthInterface

import sys
import requests


def get_edge_device(base_url, access_token, serial_number):
    final_url = "https://{0}/v1/edm/edge_devices".format(base_url)
    return requests.get(final_url, params={'serial_number': serial_number},
                        headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + access_token})


def main():
    oauth_interface = OAuthInterface(Settings.const_base_url, Settings.const_api_key, Settings.const_api_secret,
                                     Settings.const_username, Settings.const_password)

    oauth_interface.request_access_token()

    response = get_edge_device(Settings.const_base_url, oauth_interface.access_token, Settings.const_serial_number)
    print(response.url)
    print(response.status_code)
    json = response.json()
    print(json)

    network_interface = NetworkInterface(Settings.const_base_url)

    response = network_interface.get(oauth_interface.access_token, json['edge_devices'][0]['id'])
    print(response.url)
    print(response.status_code)
    json = response.json()
    print(json)

    oauth_interface.refresh_access_token(oauth_interface.refresh_token)

    response = oauth_interface.revoke_access_token(oauth_interface.access_token)
    print(response.url)
    print(response.status_code)
    json = response.json()
    print(json)


if __name__ == "__main__":
    try:
        main()
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("Crtl+C Pressed. Shutting down.")
        sys.exit(0)
