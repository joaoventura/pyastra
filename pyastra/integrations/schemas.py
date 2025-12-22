"""
This module generates python dictionaries with information from PyAstra objects.

"""

from pyastra import const
from pyastra.core import aspects
from pyastra.dignities import essential, accidental


def planet_snapshot_schema(obj):
    """ Returns a lighter planet schema to be embedded in other schemas. """
    essential_info = obj.essential_dignities()
    accidental_dignities = obj.accidental_dignities()
    try:
        accidental_dignities_score = accidental_dignities.score()
    except ValueError:
        accidental_dignities_score = 0
    return {
        'Planet': obj.id,
        'Sign': obj.sign,
        'House': obj.house().num(),
        'Retrograde': obj.is_retrograde(),
        'Combust': accidental_dignities.is_combust(),
        'Essential Dignity Score': essential_info.score,
        'Accidental Dignity Score': accidental_dignities_score,
    }


def planet_complete_schema(obj, chart, asp_list=const.MAJOR_ASPECTS):
    """ Returns the complete schema for a planet. """
    res = {
        'Planet': obj.id,
        'Position': {
            'Sign': obj.sign,
            'Longitude in sign': obj.signlon,
            'Longitude in zodiac': obj.lon,
            'Speed': obj.lon_speed,
            'House': obj.house().num(),
            'Movement': obj.movement(),
        }
    }
    # Essential dignities
    info = obj.essential_dignities()
    dignities = info.get_dignities()
    res['Essential Dignities'] = {
        'Total Score': info.score,
        'Factors': dignities
    }
    # Accidental dignities
    dig = obj.accidental_dignities()
    try:
        res['Accidental Dignities'] = {
            'Total Score': dig.score(),
            'Factors': []
        }
        for key, value in dig.score_properties.items():
            if value != 0:
                res['Accidental Dignities']['Factors'].append({
                    'Type': key,
                    'Score': value,
                    'Description': accidental.SCORE_TABLE_DESCRIPTION[key]
                })
    except ValueError:
        pass
    # Aspects
    res['Aspects'] = []
    for obj2 in chart.objects:
        # Ignore same object
        if obj == obj2:
            continue

        aspect = obj.get_aspect(obj2, asp_list)
        if not aspect or aspect.type == const.NO_ASPECT:
            continue

        if aspect.active.id == obj.id:
            res['Aspects'].append({
                'Type': const.ASPECT_NAMES[aspect.type],
                'Movement': aspect.active.movement,
                'Passive': aspect.passive.id,
                'Orb': aspect.orb,
            })

    return res


def house_schema(house, chart):
    """ Returns the schema of an house. """
    res = {
        'House': house.num(),
        'House Condition': house.condition,
        'Position': {
            'Sign': house.sign,
            'Longitude in sign': house.signlon,
            'Longitude in zodiac': house.lon,
        }
    }
    # House Ruler
    ruler_id = house.sign.ruler
    ruler = chart.get(ruler_id)
    res['Ruler'] = planet_snapshot_schema(ruler)
    # House tenants
    res['Tenants'] = []
    for obj in chart.objects:
        if house.has_object(obj):
            res['Tenants'].append(planet_snapshot_schema(obj))

    return res


def chart_complete_schema(chart, asp_list=const.MAJOR_ASPECTS):
    """ Returns the complete schema for a chart. """
    return {
        'Planets': [planet_complete_schema(obj, chart, asp_list) for obj in chart.objects],
        'Houses': [house_schema(house, chart) for house in chart.houses],
    }
