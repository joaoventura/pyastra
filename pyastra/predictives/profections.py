"""
This module provides useful functions for handling profections.
    
"""

import math
from pyastra import const
from pyastra.ephem import ephem


def compute(chart, date, fixed_objects=False):
    """
    Returns a profection chart for a given date.
    Receives argument 'fixed_objects' to fix chart objects in their natal locations.
    
    """

    sun = chart.get_object(const.SUN)
    prev_sr = ephem.prev_solar_return(date, sun.lon)
    next_sr = ephem.next_solar_return(date, sun.lon)

    # In one year, rotate chart 30º
    rotation = 30 * (date.jd - prev_sr.jd) / (next_sr.jd - prev_sr.jd)

    # Include 30º for each previous year
    age = math.floor((date.jd - chart.date.jd) / 365.25)
    rotation = 30 * age + rotation

    # Create a copy of the chart and rotate content
    p_chart = chart.copy()
    for obj in p_chart.objects:
        if not fixed_objects:
            obj.relocate(obj.lon + rotation)
    for house in p_chart.houses:
        house.relocate(house.lon + rotation)
    for angle in p_chart.angles:
        angle.relocate(angle.lon + rotation)

    return p_chart
