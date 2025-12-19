"""
Provide functions and classes for handling dates and times.

The classes implemented in this file are <Date>, <Time> and <Datetime>.
Since time is similar to angles (same string separators and base 60), the <Time> class uses angular
functions for internal conversions.

"""

from pyastra.core import angle

# Calendar types
GREGORIAN = 0
JULIAN = 1


# === Julian Day Number conversions === #

def date_jdn(year, month, day, calendar):
    """ Converts date to Julian Day Number. """
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    if calendar == GREGORIAN:
        return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083


def jdn_date(jdn):
    """ Converts Julian Day Number to Gregorian date. """
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    day = e + 1 - (153 * m + 2) // 5
    month = m + 3 - 12 * (m // 10)
    year = 100 * b + d - 4800 + m // 10
    return [year, month, day]


# ------------------ #
#     Date Class     #
# ------------------ #

class Date:
    """
    This class represents a calendar date. It is internally represented by a JDN integer.
    
    Objects of this class can be instantiated with dates of type string, list and int (jdn).
    String and date lists are like 'yyyy/mm/dd'.
    
    """

    # Calendar types
    GREGORIAN = GREGORIAN
    JULIAN = JULIAN

    def __init__(self, value, calendar=GREGORIAN):
        if isinstance(value, str):
            # Assume string date such as "2015/03/29"
            value = [int(v) for v in value.split('/')]
            value = date_jdn(value[0], value[1], value[2], calendar)
        elif isinstance(value, list):
            # Assume list date such as [2015,03,29]
            value = date_jdn(value[0], value[1], value[2], calendar)
        self.jdn = int(value)

    def dayofweek(self):
        """ Returns the day of week starting on Sunday as zero. """
        return (self.jdn + 1) % 7

    def date(self):
        """ Returns date as list [yyyy,mm,dd]. """
        return jdn_date(self.jdn)

    def to_list(self):
        """ Returns date as signed list. """
        date = self.date()
        sign = '+' if date[0] >= 0 else '-'
        date[0] = abs(date[0])
        return list(sign) + date

    def to_string(self):
        """ Returns date as string. """
        slist = self.to_list()
        sign = '' if slist[0] == '+' else '-'
        string = '/'.join(['%02d' % v for v in slist[1:]])
        return sign + string

    def __str__(self):
        return f'<{self.to_string()}>'


# ------------------ #
#     Time Class     #
# ------------------ #

class Time:
    """
    This class represents a time in the library.
    A time from this class can have negative values.

    Objects of this class can be instantiated with strings, signed lists or float values.
    String and time lists are like 'hh:mm:ss.'
    
    """

    def __init__(self, value):
        self.value = angle.to_float(value)

    def get_utc(self, utcoffset):
        """ Returns a new Time object set to UTC given an offset Time object. """
        new_time = (self.value - utcoffset.value) % 24
        return Time(new_time)

    def time(self):
        """ Returns time as list [hh,mm,ss]. """
        slist = self.to_list()
        if slist[0] == '-':
            slist[1] *= -1
            # We must do a trick if we want to make negative zeros explicit
            if slist[1] == -0:
                slist[1] = -0.0
        return slist[1:]

    def to_list(self):
        """ Returns time as signed list. """
        slist = angle.to_list(self.value)
        # Keep hours in 0..23
        slist[1] = slist[1] % 24
        return slist

    def to_string(self):
        """ Returns time as string. """
        slist = self.to_list()
        string = angle.slist_str(slist)
        return string if slist[0] == '-' else string[1:]

    def __str__(self):
        return f'<{self.to_string()}>'


# ------------------ #
#   Datetime Class   #
# ------------------ #

class Datetime:
    """
    This class represents a specific moment in time given by a date, a time and an UTC Offset.
    The UTC Offset is zero by default (UTC+0) although an offset can be given.
    
    """

    # Calendar types
    GREGORIAN = GREGORIAN
    JULIAN = JULIAN

    def __init__(self, date, time=0, utcoffset=0, calendar=GREGORIAN):
        # Prepare the variables
        if isinstance(date, Date):
            self.date = date
        else:
            self.date = Date(date, calendar)

        if isinstance(time, Time):
            self.time = time
        else:
            self.time = Time(time)

        if isinstance(utcoffset, Time):
            self.utcoffset = utcoffset
        else:
            self.utcoffset = Time(utcoffset)

        # Compute jd
        self.jd = self.date.jdn + self.time.value / 24.0 - self.utcoffset.value / 24.0 - 0.5

    @staticmethod
    def from_jd(jd, utcoffset):
        """ Builds a Datetime object given a jd and utc offset. """
        if not isinstance(utcoffset, Time):
            utcoffset = Time(utcoffset)
        local_jd = jd + utcoffset.value / 24.0
        date = Date(round(local_jd))
        time = Time((local_jd + 0.5 - date.jdn) * 24)
        return Datetime(date, time, utcoffset)

    def get_utc(self):
        """ Returns this Datetime localized for UTC. """
        time_utc = self.time.get_utc(self.utcoffset)
        date_utc = Date(round(self.jd))
        return Datetime(date_utc, time_utc)

    def __str__(self):
        return '<%s %s %s>' % (self.date.to_string(),
                               self.time.to_string(),
                               self.utcoffset.to_string())

    def __repr__(self):
        return self.__str__()
