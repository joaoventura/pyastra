"""
This module provides useful functions for handling planetary times.
    
The most import element is the HourTable class which handles all queries to the planetary rulers
and hour rulers, including the start and ending datetimes of each hour ruler.
  
"""

from pyastra import const
from pyastra.ephem import ephem
from pyastra.datetime import Datetime

# Planetary rulers starting at Sunday
DAY_RULERS = [
    const.SUN,
    const.MOON,
    const.MARS,
    const.MERCURY,
    const.JUPITER,
    const.VENUS,
    const.SATURN
]

NIGHT_RULERS = [
    const.JUPITER,
    const.VENUS,
    const.SATURN,
    const.SUN,
    const.MOON,
    const.MARS,
    const.MERCURY
]

# Planetary hours round list starting at Sunday's sunrise
ROUND_LIST = [
    const.SUN,
    const.VENUS,
    const.MERCURY,
    const.MOON,
    const.SATURN,
    const.JUPITER,
    const.MARS
]


# === Private functions === #

def nth_ruler(n, dow):
    """
    Returns the n-th hour ruler since last sunrise by day of week.
    Both arguments are zero based.
    
    """
    index = (dow * 24 + n) % 7
    return ROUND_LIST[index]


def hour_table(date, pos):
    """
    Creates the planetary hour table for a date and position.
    
    The table includes both diurnal and nocturnal hour sequences and each of the 24 entries (12 * 2)
    are like (startJD, endJD, ruler).
    
    """

    last_sunrise = ephem.last_sunrise(date, pos)
    middle_sunset = ephem.next_sunset(last_sunrise, pos)
    next_sunrise = ephem.next_sunrise(date, pos)
    table = []

    # Create diurnal hour sequence
    length = (middle_sunset.jd - last_sunrise.jd) / 12.0
    for i in range(12):
        start = last_sunrise.jd + i * length
        end = start + length
        ruler = nth_ruler(i, last_sunrise.date.dayofweek())
        table.append([start, end, ruler])

    # Create nocturnal hour sequence
    length = (next_sunrise.jd - middle_sunset.jd) / 12.0
    for i in range(12):
        start = middle_sunset.jd + i * length
        end = start + length
        ruler = nth_ruler(i + 12, last_sunrise.date.dayofweek())
        table.append([start, end, ruler])

    return table


def get_hour_table(date, pos):
    """ Returns an HourTable object. """
    table = hour_table(date, pos)
    return HourTable(table, date)


# ------------------- #
#   HourTable Class   #
# ------------------- #

class HourTable:
    """
    This class represents a Planetary Hour Table and includes methods to access its properties.
    
    """

    def __init__(self, table, date):
        self.table = table
        self.date = date
        self.currIndex = self.index(date)

    def index(self, date):
        """ Returns the index of a date in the table. """
        for (i, (start, end, _)) in enumerate(self.table):
            if start <= date.jd <= end:
                return i
        return None

    # === Properties === #

    def day_ruler(self):
        """ Returns the current day ruler. """
        return self.table[0][2]

    def night_ruler(self):
        """ Returns the current night ruler. """
        return self.table[12][2]

    def curr_ruler(self):
        """ Returns the current day or night ruler considering if it's day or night. """
        if self.currIndex < 12:
            return self.day_ruler()
        return self.night_ruler()

    def hour_ruler(self):
        """ Returns the current hour ruler. """
        return self.table[self.currIndex][2]

    def curr_info(self):
        """ Returns information about the current planetary time. """
        return self.index_info(self.currIndex)

    def index_info(self, index):
        """ Returns information about a specific planetary time. """
        entry = self.table[index]
        info = {
            # Default is diurnal
            'mode': 'Day',
            'ruler': self.day_ruler(),
            'dayRuler': self.day_ruler(),
            'nightRuler': self.night_ruler(),
            'hourRuler': entry[2],
            'hourNumber': index + 1,
            'tableIndex': index,
            'start': Datetime.from_jd(entry[0], self.date.utcoffset),
            'end': Datetime.from_jd(entry[1], self.date.utcoffset)
        }
        if index >= 12:
            # Set information as nocturnal
            info.update({
                'mode': 'Night',
                'ruler': info['nightRuler'],
                'hourNumber': index + 1 - 12
            })
        return info
