"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for handling the primary directions.

"""

from pyastra import const
from pyastra.chart import Chart
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.predictives import primarydirections


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# MC will be used for calculating arcs
mc = chart.get(const.MC)

# Get a promissor and significator
prom = chart.get(const.MARS)
sig = chart.get(const.MERCURY)

# Compute arc in zodiaco (zero_lat = True)
arc = primarydirections.get_arc(prom, sig, mc, pos, zero_lat=True)
print(arc)  # 56.17347

# Compute arc in mundo
arc = primarydirections.get_arc(prom, sig, mc, pos, zero_lat=False)
print(arc)  # 56.74266

# Create Primary Directions class
from pyastra.predictives.primarydirections import PrimaryDirections
pd = PrimaryDirections(chart)

# Get arcs
arc = pd.get_arc(pd.N(const.MARS), pd.N(const.MERCURY))
print(arc['arcm'])  # 56.74266 (arc in-mundo)
print(arc['arcz'])  # 56.17347 (arc in-zodiaco)

# Create Primary Directions table class
from pyastra.predictives.primarydirections import PDTable
pd = PDTable(chart, const.MAJOR_ASPECTS)
pd.filter_by(promissor=const.MARS)  # List all directions by promissor
pd.filter_by(significator=const.MERCURY)  # List all directions by significator
pd.filter_by(direction_type='Z', arc_min=20, arc_max=30)  # List all zodiacal directions in range
