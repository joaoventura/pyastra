"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for handling accidental dignities.

"""

from pyastra import const
from pyastra.chart import Chart
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos

from pyastra.dignities import accidental
from pyastra.dignities.accidental import AccidentalDignity


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Get some objects
obj = chart.get(const.VENUS)
sun = chart.get(const.SUN)

# Sun relation
relation = accidental.sun_relation(obj, sun)
print(relation)

# Augmenting or Diminishing light
light = accidental.light(obj, sun)
print(light)

# Orientality
orientality = accidental.orientality(obj, sun)
print(orientality)

# Haiz
haiz = accidental.haiz(obj, chart)
print(haiz)

# Build AccidentalDignity class
aDign = AccidentalDignity(obj, chart)

# Check for haiz
haiz = aDign.haiz()
print(haiz)

# List good aspects to benefics
asp = aDign.aspect_benefics()
print(asp)

# Get the accidental dignity score properties and its sum
scoreP = aDign.get_score_properties()
score = aDign.score()
print(scoreP)
print(score)
