import requests


class NetworkInterface:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, access_token, edge_device_id):
        final_url = "https://{0}/v1/edm/edge_devices/{1}/network_interfaces".format(self.base_url, edge_device_id)
        return requests.get(final_url,
                            headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + access_token})

    def post(self, access_token, edge_device_id, body):
        final_url = "https://{0}/v1/edm/edge_devices/{1}/network_interfaces".format(self.base_url, edge_device_id)
        return requests.post(final_url, body,
                             headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + access_token})

    def patch(self, access_token, edge_device_id, id, body):
        final_url = "https://{0}/v1/edm/edge_devices/{1}/network_interfaces/{2}".format(self.base_url, edge_device_id,
                                                                                        id)
        return requests.patch(final_url, body,
                              headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + access_token})

    def delete(self, access_token, edge_device_id, id):
        final_url = "https://{0}/v1/edm/edge_devices/{1}/network_interfaces/{2}".format(self.base_url, edge_device_id)
        return requests.delete(final_url,
                               headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + access_token})
