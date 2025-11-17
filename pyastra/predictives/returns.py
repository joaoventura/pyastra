"""
This module provides useful functions for handling solar and lunar returns.
It only handles solar returns for now.
    
"""
import dataclasses

from pyastra import const
from pyastra.ephem import ephem
from pyastra.chart import Chart


def _compute_chart(chart, date):
    """
    Internal function to return a new chart for a specific date using properties from old chart.
    
    """
    context = dataclasses.replace(chart.context, jd=date.jd)
    ids = [obj.id for obj in chart.objects]
    return Chart.from_context(context, ids)


def next_solar_return(chart, date):
    """ Returns the solar return of a Chart after a specific date. """
    sun = chart.get_object(const.SUN)
    context = dataclasses.replace(chart.context, jd=date.jd)
    sr_date = ephem.next_solar_return(sun.lon, context)
    return _compute_chart(chart, sr_date)


def prev_solar_return(chart, date):
    """ Returns the solar return of a Chart before a specific date. """
    sun = chart.get_object(const.SUN)
    context = dataclasses.replace(chart.context, jd=date.jd)
    sr_date = ephem.prev_solar_return(sun.lon, context)
    return _compute_chart(chart, sr_date)
