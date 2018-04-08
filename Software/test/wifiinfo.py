"""
Sniff local WiFi networks in order to look them up on WiGLE.

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from platform import system
import re
import subprocess
import time

import requests

from pygle import network


scan_cmd = {'windows': 'netsh wlan show networks mode=Bssid',
            'linux': 'nmcli -t -f bssid dev wifi list',  # untested
            'osx': '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s',  # untested
            }


def local_bssids():
    """Get a list of available wireless access points.
    """
    res = subprocess.check_output(scan_cmd[system().lower()],universal_newlines=True)
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    bssids = pattern.findall(res)
    return set(bssids)


def geolocate():
    """Locate a device using locally available wireless access points.
    """
    lats = []
    longs = []
    for bssid in local_bssids():
        print("BSSID:", bssid)
        lat, lng = geolocate_wigle(bssid)  # can be replaced with other geocoding sources
        if lat and lng:
            lats.append(lat)
            longs.append(lng)
        time.sleep(0.1)
    if lats and longs:
        lat = sum(lats) / len(lats)
        lng = sum(longs) / len(longs)
        return lat, lng
    else:
        return "No geolocation possible"


def geolocate_wigle(bssid):
    """Search WiGLE for a BSSID and return lat/lng.
    """
    res = network.search(netid=bssid)
    if res['success'] and res['resultCount']:
        lat = res['results'][0]['trilat']
        lng = res['results'][0]['trilong']
    else:
        print(res)
        lat, lng = None, None
    return lat, lng


if __name__ == "__main__":
    print("WiGLE")
    print(geolocate())
