"""
    This file is part of pyastra - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module implements the Behavior Traditional 
    Protocol.
    
"""

from pyastra import const
from pyastra import aspects
from pyastra.dignities import essential


def _merge(listA, listB):
    """ Merges two list of objects removing
    repetitions. 
    
    """
    listA = [x.id for x in listA]
    listB = [x.id for x in listB]
    listA.extend(listB)
    set_ = set(listA)
    return list(set_)


def compute(chart):
    """ Computes the behavior. """

    factors = []

    # Planets in House1 or Conjunct Asc
    house1 = chart.get_house(const.HOUSE1)
    planetsHouse1 = chart.objects.get_objects_in_house(house1)
    asc = chart.get_angle(const.ASC)
    planetsConjAsc = chart.objects.get_objects_aspecting(asc, [0])

    _set = _merge(planetsHouse1, planetsConjAsc)
    factors.append(['Planets in House1 or Conj Asc', _set])

    # Planets conjunct Moon or Mercury
    moon = chart.get(const.MOON)
    mercury = chart.get(const.MERCURY)
    planetsConjMoon = chart.objects.get_objects_aspecting(moon, [0])
    planetsConjMercury = chart.objects.get_objects_aspecting(mercury, [0])

    _set = _merge(planetsConjMoon, planetsConjMercury)
    factors.append(['Planets Conj Moon or Mercury', _set])

    # Asc ruler if aspected by disposer
    ascRulerID = essential.ruler(asc.sign)
    ascRuler = chart.get_object(ascRulerID)
    disposerID = essential.ruler(ascRuler.sign)
    disposer = chart.get_object(disposerID)

    _set = []
    if aspects.is_aspecting(disposer, ascRuler, const.MAJOR_ASPECTS):
        _set = [ascRuler.id]
    factors.append(['Asc Ruler if aspected by its disposer', _set]);

    # Planets aspecting Moon or Mercury
    aspMoon = chart.objects.get_objects_aspecting(moon, [60, 90, 120, 180])
    aspMercury = chart.objects.get_objects_aspecting(mercury, [60, 90, 120, 180])

    _set = _merge(aspMoon, aspMercury)
    factors.append(['Planets Asp Moon or Mercury', _set])

    return factors
