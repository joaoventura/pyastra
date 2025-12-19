"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for computing the temperament protocol.

"""

from pyastra.core.chart import Chart
from pyastra.core.datetime import Datetime
from pyastra.core.geopos import GeoPos
from pyastra.protocols.temperament import Temperament


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Temperament
temperament = Temperament(chart)

# Print temperament factors
factors = temperament.get_factors()
for factor in factors:
    print(factor)

# Print temperament modifiers
modifiers = temperament.get_modifiers()
for modifier in modifiers:
    print(modifier)

# Print temperament scores
score = temperament.get_score()
print(score)
