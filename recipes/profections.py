"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for handling profections.

"""

from pyastra import const
from pyastra.chart import Chart
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.predictives import profections


# Build a chart for a date and location
date = Datetime('2011/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Get the profection Chart for a date
today = Datetime('2015/04/06', '10:40', '+01:00')
pChart = profections.compute(chart, today)

# Print the Asc
asc = pChart.get(const.ASC)
print(asc)  #  <Asc Capricorn +05:23:06>
