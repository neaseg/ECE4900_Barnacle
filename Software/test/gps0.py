import requests
import re
import uuid

class WigleAgent():

    def __init__(self, username, password):
        self.agent(username, password)
        self.mac_address()

    def get_lat_lng(self):
        if mac_address == None:
            mac_address = self.mac_address
        if '-' in mac_address:
            mac_address = mac_address.replace('-', ':')
        try:
            self.query_response = self.send_query(mac_address)
            response = self.parse_response()
        except IndexError:
            response = 'MAC location not known'
        return response

    def agent(self, username, password):
        self.agent = requests.Session()
        self.agent.post('https://wigle.net//gps/gps/main/login',
                   data={'credential_0': username,
                         'credential_1': password,
                         'destination': '/gps/gps/main'})

    def mac_address(self):
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
        self.mac_address = mac


    def send_query(self, mac_address):
        response = self.agent.post(url='https://wigle.net/gps/gps/main/confirmlocquery',
                       data={'netid': mac_address,
                             'Query': 'Query'})
        return response.text

    def parse_response(self):
        lat = self.get_lat()
        lng = self.get_lng()
        return lat, lng

    def get_lat(self):
        resp_lat = re.findall(r'maplat=.*\&', self.query_response)
        lat = resp_lat[0].split('&')[0].split('=')[1]
        return float(lat)

    def get_lng(self):
        resp_lng = re.findall(r'maplon=.*\&', self.query_response)
        lng = resp_lng[0].split('&')[0].split('=')[1]
        return float(lng)


if __name__ == '__main__':
    # mac_locater = WigleAgent(, )
    mac_locater = WigleAgent(username="ulneverknow",password="naruto01")
    print mac_locater.get_lat_lng()
