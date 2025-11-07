"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    planetary times.

"""

from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.tools import planetarytime


# Build a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')

# Get the planetary hour table
hourTable = planetarytime.get_hour_table(date, pos)
print(hourTable.day_ruler())    # Venus
print(hourTable.night_ruler())  # Mars
print(hourTable.hour_ruler())   # Saturn

# Use the info Dict to print hour number information
info = hourTable.curr_info()
print(info['hourNumber'])  # 11
print(info['start'])       # <2015/03/13 16:42:10 00:00:00>
print(info['end'])         # <2015/03/13 17:41:20 00:00:00>