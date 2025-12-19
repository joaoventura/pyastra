"""
This module implements the Temperament Traditional Protocol.

The Temperament protocol returns the temperament scores given the characteristics of the objects
and other things which affects the Asc, the Moon and the Sun Season.
    
"""

from pyastra import const
from pyastra.core import aspects, props
from pyastra.dignities import essential

# Temperament factors
ASC_SIGN = 'Asc Sign'
ASC_RULER = 'Asc Ruler'
ASC_RULER_SIGN = 'Asc Ruler Sign'
HOUSE1_PLANETS_IN = 'Planets in House1'
ASC_PLANETS_CONJ = 'Planets conj Asc'
ASC_PLANETS_ASP = 'Planets asp Asc'
MOON_SIGN = 'Moon Sign'
MOON_PHASE = 'Moon Phase'
MOON_DISPOSITOR_SIGN = 'Moon Dispositor Sign'
MOON_PLANETS_CONJ = 'Planets conj Moon'
MOON_PLANETS_ASP = 'Planets asp Moon'
SUN_SEASON = 'Sun season'

# Modifier factors
MOD_ASC = 'Asc'
MOD_ASC_RULER = 'Asc Ruler'
MOD_MOON = 'Moon'


# === Computation of factors === #

def single_factor(factors, chart, factor, obj, aspect=None):
    """" Single factor for the table. """
    obj_id = obj if isinstance(obj, str) else obj.id
    res = {
        'factor': factor,
        'objID': obj_id,
        'aspect': aspect
    }

    # For signs (obj as string) return sign element
    if isinstance(obj, str):
        res['element'] = props.sign.element[obj]

    # For Sun return sign and sunseason element
    elif obj_id == const.SUN:
        sunseason = props.sign.sunseason[obj.sign]
        res['sign'] = obj.sign
        res['sunseason'] = sunseason
        res['element'] = props.base.sunseasonElement[sunseason]

    # For Moon return phase and phase element
    elif obj_id == const.MOON:
        phase = chart.get_moon_phase()
        res['phase'] = phase
        res['element'] = props.base.moonphaseElement[phase]

    # For regular planets return element or sign/sign element if there's an aspect involved
    elif obj_id in const.LIST_SEVEN_PLANETS:
        if aspect:
            res['sign'] = obj.sign
            res['element'] = props.sign.element[obj.sign]
        else:
            res['element'] = obj.element()

    # If there's element, insert into list
    if 'element' in res.keys():
        factors.append(res)

    return res


def modifier_factor(factor, factor_obj, other_obj, asp_list):
    """ Computes a factor for a modifier. """
    asp = aspects.aspect_type(factor_obj, other_obj, asp_list)
    if asp != const.NO_ASPECT:
        return {
            'factor': factor,
            'aspect': asp,
            'objID': other_obj.id,
            'element': other_obj.element()
        }
    return None


# === Temperament factors and modifiers === #

def get_factors(chart):
    """ Returns the factors for the temperament. """
    factors = []

    # Asc sign
    asc = chart.get_angle(const.ASC)
    single_factor(factors, chart, ASC_SIGN, asc.sign)

    # Asc ruler
    asc_ruler_id = essential.ruler(asc.sign)
    asc_ruler = chart.get_object(asc_ruler_id)
    single_factor(factors, chart, ASC_RULER, asc_ruler)
    single_factor(factors, chart, ASC_RULER_SIGN, asc_ruler.sign)

    # Planets in House 1
    house1 = chart.get_house(const.HOUSE1)
    planets_house1 = chart.objects.get_objects_in_house(house1)
    for obj in planets_house1:
        single_factor(factors, chart, HOUSE1_PLANETS_IN, obj)

    # Planets conjunct Asc
    planets_conj_asc = chart.objects.get_objects_aspecting(asc, [0])
    for obj in planets_conj_asc:
        # Ignore planets already in house 1
        if obj not in planets_house1:
            single_factor(factors, chart, ASC_PLANETS_CONJ, obj)

    # Planets aspecting Asc cusp
    asp_list = [60, 90, 120, 180]
    planets_asp_asc = chart.objects.get_objects_aspecting(asc, asp_list)
    for obj in planets_asp_asc:
        aspect = aspects.aspect_type(obj, asc, asp_list)
        single_factor(factors, chart, ASC_PLANETS_ASP, obj, aspect)

    # Moon sign and phase
    moon = chart.get_object(const.MOON)
    single_factor(factors, chart, MOON_SIGN, moon.sign)
    single_factor(factors, chart, MOON_PHASE, moon)

    # Moon dispositor
    moon_ruler_id = essential.ruler(moon.sign)
    moon_ruler = chart.get_object(moon_ruler_id)
    moon_factor = single_factor(factors, chart, MOON_DISPOSITOR_SIGN, moon_ruler.sign)
    moon_factor['planetID'] = moon_ruler_id  # Append moon dispositor ID

    # Planets conjunct Moon
    planets_conj_moon = chart.objects.get_objects_aspecting(moon, [0])
    for obj in planets_conj_moon:
        single_factor(factors, chart, MOON_PLANETS_CONJ, obj)

    # Planets aspecting Moon
    asp_list = [60, 90, 120, 180]
    planets_asp_moon = chart.objects.get_objects_aspecting(moon, asp_list)
    for obj in planets_asp_moon:
        aspect = aspects.aspect_type(obj, moon, asp_list)
        single_factor(factors, chart, MOON_PLANETS_ASP, obj, aspect)

    # Sun season
    sun = chart.get_object(const.SUN)
    single_factor(factors, chart, SUN_SEASON, sun)

    return factors


def get_modifiers(chart):
    """ Returns the factors of the temperament modifiers. """
    modifiers = []

    # Factors which can be affected
    asc = chart.get_angle(const.ASC)
    asc_ruler_id = essential.ruler(asc.sign)
    asc_ruler = chart.get_object(asc_ruler_id)
    moon = chart.get_object(const.MOON)
    factors = [
        [MOD_ASC, asc],
        [MOD_ASC_RULER, asc_ruler],
        [MOD_MOON, moon]
    ]

    # Factors of affliction
    mars = chart.get_object(const.MARS)
    saturn = chart.get_object(const.SATURN)
    sun = chart.get_object(const.SUN)
    affect = [
        [mars, [0, 90, 180]],
        [saturn, [0, 90, 180]],
        [sun, [0]]
    ]

    # Do calculations of afflictions
    for affecting_obj, affecting_asps in affect:
        for factor, affected_obj in factors:
            modf = modifier_factor(factor, affected_obj, affecting_obj, affecting_asps)
            if modf:
                modifiers.append(modf)

    return modifiers


def scores(factors):
    """ Computes the score of temperaments and elements. """
    temperaments = {
        const.CHOLERIC: 0,
        const.MELANCHOLIC: 0,
        const.SANGUINE: 0,
        const.PHLEGMATIC: 0
    }

    qualities = {
        const.HOT: 0,
        const.COLD: 0,
        const.DRY: 0,
        const.HUMID: 0
    }

    for factor in factors:
        element = factor['element']

        # Score temperament
        temperament = props.base.elementTemperament[element]
        temperaments[temperament] += 1

        # Score qualities
        tqualities = props.base.temperamentQuality[temperament]
        qualities[tqualities[0]] += 1
        qualities[tqualities[1]] += 1

    return {
        'temperaments': temperaments,
        'qualities': qualities
    }


# --------------------- #
#   Temperament Class   #
# --------------------- #

class Temperament:
    """ This class represents the calculation of the temperament of a chart. """

    def __init__(self, chart):
        self.chart = chart

    def get_factors(self):
        """ Returns the list of temperament factors. """
        return get_factors(self.chart)

    def get_modifiers(self):
        """ Returns the list of temperament modifiers. """
        return get_modifiers(self.chart)

    def get_score(self):
        """ Returns the temperament and qualitiy scores. """
        return scores(self.get_factors())
