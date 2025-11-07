"""
This module implements the Almutem Traditional Protocol.
The Almutem protocol returns the Planet which scores higher in some hylegic points.
    
"""

from pyastra import const
from pyastra.tools import planetarytime
from pyastra.dignities import essential

# House scores
HOUSE_SCORES = {
    const.HOUSE1: 12,
    const.HOUSE2: 6,
    const.HOUSE3: 3,
    const.HOUSE4: 9,
    const.HOUSE5: 7,
    const.HOUSE6: 1,
    const.HOUSE7: 10,
    const.HOUSE8: 4,
    const.HOUSE9: 5,
    const.HOUSE10: 11,
    const.HOUSE11: 8,
    const.HOUSE12: 2
}

# List of dignities
DIGNITY_LIST = [
    'ruler',
    'exalt',
    'dayTrip',
    'nightTrip',
    'partTrip',
    'term',
    'face'
]

# List of objects
OBJECT_LIST = const.LIST_SEVEN_PLANETS


def new_row():
    """ Returns a new Almutem table row. """
    row = {}
    for obj in OBJECT_LIST:
        row[obj] = {
            'string': '',
            'score': 0
        }
    return row


def compute(chart):
    """ Computes the Almutem table. """
    almutems = {}

    # Hylegic points
    hylegic = [
        chart.get_object(const.SUN),
        chart.get_object(const.MOON),
        chart.get_angle(const.ASC),
        chart.get_object(const.PARS_FORTUNA),
        chart.get_object(const.SYZYGY)
    ]
    for hyleg in hylegic:
        row = new_row()
        dig_info = essential.get_info(hyleg.sign, hyleg.signlon)

        # Add the scores of each planet where hyleg has dignities
        for dignity in DIGNITY_LIST:
            obj_id = dig_info[dignity]
            if obj_id:
                score = essential.SCORES[dignity]
                row[obj_id]['string'] += f'+{score}'
                row[obj_id]['score'] += score

        almutems[hyleg.id] = row

    # House positions
    row = new_row()
    for obj_id in OBJECT_LIST:
        obj = chart.get_object(obj_id)
        house = chart.houses.get_object_house(obj)
        score = HOUSE_SCORES[house.id]
        row[obj_id]['string'] = f'+{score}'
        row[obj_id]['score'] = score
    almutems['Houses'] = row

    # Planetary time
    row = new_row()
    table = planetarytime.get_hour_table(chart.date, chart.pos)
    ruler = table.curr_ruler()
    hour_ruler = table.hour_ruler()
    row[ruler] = {
        'string': '+7',
        'score': 7
    }
    row[hour_ruler] = {
        'string': '+6',
        'score': 6
    }
    almutems['Rulers'] = row

    # Compute scores
    scores = new_row()
    for _property, _list in almutems.items():
        for obj_id, values in _list.items():
            scores[obj_id]['string'] += values['string']
            scores[obj_id]['score'] += values['score']
    almutems['Score'] = scores

    return almutems
