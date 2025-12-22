"""
Author: João Ventura <joaojonesventura@gmail.com>
A tropical solar year is the length from spring equinox to the following spring equinox.
    
This recipe was implemented to reply to a topic opened at
http://skyscript.co.uk/forums/viewtopic.php?t=8563 and shows that the solar year has an amplitude
of more than 25 minutes, considering the average year of 365.2425 days.
    
To plot the graphics you must have matplotlib installed.

"""

from pyastra.core.datetime import Datetime
from pyastra.ephem import ephem


def plot(hdiff, title):
    """ Plots the tropical solar length by year. """
    import matplotlib.pyplot as plt
    years = [elem[0] for elem in hdiff]
    diffs = [elem[1] for elem in hdiff]
    plt.plot(years, diffs)
    plt.ylabel('Distance in minutes')
    plt.xlabel('Year')
    plt.title(title)
    plt.axhline(y=0, c='red')
    plt.show()


# Set the starting year
sYear = 1980

# Get successive spring equinox dates
equinoxes = []
span = 100
for year in range(sYear, sYear + span):
    # Get the spring equinox date for the year
    dt = Datetime(f'{year}/01/01', '00:00')
    sr = ephem.next_solar_return(dt, 0.00)
    equinoxes.append([year, sr.jd])

# Compute successive differences
diffs = []
for i in range(len(equinoxes) - 1):
    year1, jd1 = equinoxes[i]
    year2, jd2 = equinoxes[i+1]
    diffs.append([year1, (jd2 - jd1 - 365.2425) * 24 * 60])

print(diffs)
title = f'Solar year length from {sYear} to {sYear + span}\n'
title+= '(Compared to average year of 365.2425)'
plot(diffs, title)
