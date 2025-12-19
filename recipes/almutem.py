"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for computing the almutem protocol.

"""

from pyastra.core.chart import Chart
from pyastra.core.datetime import Datetime
from pyastra.core.geopos import GeoPos
from pyastra.protocols import almutem


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Print almutem scores
alm = almutem.compute(chart)
for k, v in alm['Score'].items():
    print(k, v)  # Mercury scores 40
