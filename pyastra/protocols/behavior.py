"""
This module implements the Behavior Traditional Protocol.
    
"""

from pyastra import const
from pyastra import aspects
from pyastra.dignities import essential


def _merge(list_a, list_b):
    """ Merges two list of objects removing repetitions. """
    list_a = [x.id for x in list_a]
    list_b = [x.id for x in list_b]
    list_a.extend(list_b)
    set_ = set(list_a)
    return list(set_)


def compute(chart):
    """ Computes the behavior. """
    factors = []

    # Planets in House1 or Conjunct Asc
    house1 = chart.get_house(const.HOUSE1)
    planets_house1 = chart.objects.get_objects_in_house(house1)
    asc = chart.get_angle(const.ASC)
    planets_conj_asc = chart.objects.get_objects_aspecting(asc, [0])

    _set = _merge(planets_house1, planets_conj_asc)
    factors.append(['Planets in House1 or Conj Asc', _set])

    # Planets conjunct Moon or Mercury
    moon = chart.get(const.MOON)
    mercury = chart.get(const.MERCURY)
    planets_conj_moon = chart.objects.get_objects_aspecting(moon, [0])
    planets_conj_mercury = chart.objects.get_objects_aspecting(mercury, [0])

    _set = _merge(planets_conj_moon, planets_conj_mercury)
    factors.append(['Planets Conj Moon or Mercury', _set])

    # Asc ruler if aspected by disposer
    asc_ruler_id = essential.ruler(asc.sign)
    asc_ruler = chart.get_object(asc_ruler_id)
    disposer_id = essential.ruler(asc_ruler.sign)
    disposer = chart.get_object(disposer_id)

    _set = []
    if aspects.is_aspecting(disposer, asc_ruler, const.MAJOR_ASPECTS):
        _set = [asc_ruler.id]
    factors.append(['Asc Ruler if aspected by its disposer', _set])

    # Planets aspecting Moon or Mercury
    asp_moon = chart.objects.get_objects_aspecting(moon, [60, 90, 120, 180])
    asp_mercury = chart.objects.get_objects_aspecting(mercury, [60, 90, 120, 180])

    _set = _merge(asp_moon, asp_mercury)
    factors.append(['Planets Asp Moon or Mercury', _set])

    return factors
