"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for computing arabic parts.

"""

from pyastra.core.chart import Chart
from pyastra.core.datetime import Datetime
from pyastra.core.geopos import GeoPos
from pyastra.tools import arabicparts


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Retrieve the Pars Spirit
parsSpirit = arabicparts.get_part(arabicparts.PARS_SPIRIT, chart)
print(parsSpirit)    # <Pars Spirit Sagittarius +03:52:01>
