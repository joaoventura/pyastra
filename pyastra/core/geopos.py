"""
Provides functions and a class for handling geographic positions.
Each latitude/longitude is an angle represented by a <float> value.

"""

from pyastra.core import angle

# Modes
LAT = 0
LON = 1

# Mappings
SIGN = {'N': '+', 'S': '-', 'E': '+', 'W': '-'}
CHAR = {
    LAT: {'+': 'N', '-': 'S'},
    LON: {'+': 'E', '-': 'W'},
}


# === Conversions === #

def to_float(value):
    """
    Converts angle representation to float.
    Accepts angles and strings such as "12W30:00".
    
    """
    if isinstance(value, str):
        # Find lat/lon char in string and insert angle sign
        value = value.upper()
        for char in ['N', 'S', 'E', 'W']:
            if char in value:
                value = SIGN[char] + value.replace(char, ':')
                break
    return angle.to_float(value)


def to_list(value):
    """ Converts angle float to signed list. """
    return angle.to_list(value)


def to_string(value, mode):
    """
    Converts angle float to string.
    Mode refers to LAT/LON.
    
    """
    string = angle.to_string(value)
    sign = string[0]
    separator = CHAR[mode][sign]
    string = string.replace(':', separator, 1)
    return string[1:]


# ------------------ #
#    GeoPos Class    #
# ------------------ #

class GeoPos:
    """
    This class represents a geographic position on the planet specified by a given lat and lon.

    Objects of this class can be instantiated with GeoPos("45N32", "128W45") or another angle type
    such as strings, signed lists or floats. 
    
    """

    def __init__(self, lat, lon):
        self.lat = to_float(lat)
        self.lon = to_float(lon)

    def slists(self):
        """ Return lat/lon as signed lists. """
        return [
            to_list(self.lat),
            to_list(self.lon)
        ]

    def strings(self):
        """ Return lat/lon as strings. """
        return [
            to_string(self.lat, LAT),
            to_string(self.lon, LON)
        ]

    def __str__(self):
        strings = self.strings()
        return f'<{strings[0]} {strings[1]}>'

    def __repr__(self):
        return self.__str__()
