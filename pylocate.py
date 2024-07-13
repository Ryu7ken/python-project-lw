"""This module can be used to get Geo-Location including Latitude and Longitude for the IP Address when provided."""

import geocoder

def geo(ip_address):
    """This function takes IP Address as argument."""
    g = geocoder.ip(ip_address)
    print("Location: ", g)
    print("Latitude and Longitude:", g.latlng)