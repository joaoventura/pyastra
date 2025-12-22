"""
This module provides functionalities for generating natural text from a chart, to be used on
LLM (Large-Language Models) prompts.

"""

from pyastra import const
from pyastra.core import aspects, angle
from pyastra.dignities import essential, accidental
from pyastra.predictives.primarydirections import PrimaryDirections


NATAL_CHART_PROMPT_TEMPLATE = """
Role: You are an expert Traditional Astrologer.
Your analysis relies on concrete astronomical conditions, Essential Dignities, and the specific 
rules of the tradition.

Workflow:
1. I will provide you with the raw text description of a Natal Chart (planets, houses, aspects, 
dignities, etc.).
2. Do not interpret the chart immediately. Simply acknowledge that you have received the data and 
state that you are ready.
3. Wait for my specific question regarding a House, a Planet, or a specific area of life.

Style Guidelines:
1. Tone: Professional and insightful.
2. Format: Provide a fluid, narrative interpretation. However, you must include sufficient 
technical details (e.g., "because Mars is in its Exaltation," or "due to the square from Saturn", 
etc) to justify your conclusions mathematically and astrologically.

Analysis Protocols:
1. When you interpret a HOUSE:
- Briefly state the areas of life associated with that house (e.g., 2nd House: Resources, 
movable possessions).
- The Sign: Interpret the nature of the Sign on the cusp of the house.
- The Ruler (Lord of the House): Analyze the ruling planet of that sign (its position, condition, 
influence, essential and accidental dignities).
- Planets in the House: Analyze any planets physically located in the house.
- Aspects: Analyze the aspects made to the Ruler of the house and to the planets within the house.

2. When you interpret a PLANET, by itself, or by being a ruler, etc.:
- Condition: Always evaluate Essential Dignities/Debilities (Rulership, Exaltation, Term, 
Triplicity, Detriment, Fall) and Accidental conditions (Retrograde, Combustion, House placement, 
Speed, etc.).
- Aspects & Dynamics: Analyze the aspects the planets do and receive. Also, identify which houses 
the aspecting planets rule and explain how those areas of life impact the planets you are analyzing.
"""

PRIMARY_DIRECTIONS_PROMPT_TEMPLATE = """
Role: You are also a master of Predictive Astrology, specializing in Primary Directions (using the 
semi-arc method). You understand that Primary Directions represent the "unfolding of destiny" and 
the structural timing of a life, often indicating major, concrete events rather than fleeting moods.

Workflow:
1. I will provide you with a list of calculated Primary Directions. 
Each entry includes the Arc (degrees), the Promissor, the Significator, and the Type of Direction
(Mundane or Zodiacal).
2. Do not interpret the list immediately. Acknowledge receipt of the data.
3. Wait for me to ask about a specific age, a specific period of life, or a specific area 
(e.g., "What happens around age 30?" or "Are there indications for career changes?").

Methodology for Interpretation:
When interpreting a direction, consider the following logic:
1. The Significator (The Receiver): Identify what part of the native's life is being affected.
- Ascendant: Life force, physical body, health, personal agency.
- Midheaven (MC): Career, public standing, actions, mother.
- Sun: Vitality, spirit, father, honor, general fortune (especially in day charts).
- Moon:: Body, emotions, fortune, mother, general fluctuations (especially in night charts).
- Etc..

2. The Promissor (The Actor): Identify what is happening or who is acting upon the significator.
- Planets: Bring their specific nature (e.g., Mars brings heat, severance, or action; 
Jupiter brings expansion or relief) and the areas of life the signify in the Natal Chart.
- Terms (Bounds): If the direction involves a change of Terms (e.g., "Ascendant enters Term of 
Mars"), interpret this as a background shift. The native enters a period governed by the rules 
and nature of that planet.
- Aspects: The nature of the event (Square = struggle/action; Trine = flow/ease; Conjunction = 
merger/intensity).

Crucial Rule - Natal Root:
You must always assume I have provided the Natal Chart context previously. 
An event in directions cannot happen if it is not promised in the Natal Chart. 
If a planet is dignified in the natal chart, its direction will be more constructive; 
if debilitated, more difficult.

"""


def describe_planets(chart):
    """ Returns the chart objects as text. """
    text = ""
    for obj in chart.objects:
        house = chart.houses.get_object_house(obj)
        text += f"{obj.id} is at {angle.to_string(obj.signlon)} of {obj.sign} in {house.id}.\n"

    return text


def describe_houses(chart):
    """ Returns the chart houses as text. """
    text = ""
    for house in chart.houses:
        text += f"{house.id} is at {angle.to_string(house.signlon)} of {house.sign} "

        # House ruler
        ruler_id = essential.ruler(house.sign)
        ruler = chart.get(ruler_id)
        text += f"and is ruled by {ruler.id}.\n"

    return text


def describe_essential_dignities(chart):
    """ Return the essential dignities of the chart objects as text. """
    text = ""
    for obj in chart.objects:
        info = essential.EssentialInfo(obj)
        dignities = info.get_dignities()
        if dignities:
            text += f"{obj.id} has the following essential dignities: "
            text += ', '.join(dignities) + ", "
        else:
            text += f"{obj.id} has no essential dignities, "
        text += f"with a total essential dignity score of {info.score}. \n"

    return text


def describe_accidental_dignities(chart):
    """ Returns the accidental dignities of the chart objects as text. """
    text = ""
    for obj in chart.objects:
        dig = accidental.AccidentalDignity(obj, chart)
        try:
            dig.score()
            rows = []
            for key, value in dig.score_properties.items():
                if value != 0:
                    rows.append((key, value))
            text += f"{obj.id} has the following list of accidental dignities, with their scores: "
            for (d, score) in rows:
                text += f"{d} ({score}), "
            text += f"with a total accidental dignity score of {dig.score()}.\n"
        except ValueError:
            pass

    return text


def describe_aspects(chart, asp_list=const.MAJOR_ASPECTS):
    """ Returns the aspects of the chart as text. """
    lines = []
    for obj1 in chart.objects:
        for obj2 in chart.objects:
            # Ignore same object
            if obj1 == obj2:
                continue

            aspect = aspects.get_aspect(obj1, obj2, asp_list)
            if not aspect or aspect.type == const.NO_ASPECT:
                continue

            string = (f"{aspect.active.id} is on a {aspect.active.movement} "
                      f"{const.ASPECT_NAMES[aspect.type]} to {aspect.passive.id} with a orb of "
                      f"{angle.to_string(aspect.orb)}.")
            lines.append(string)

    # Return
    return "\n".join(sorted(set(lines), key=lambda s: const.LIST_OBJECTS.index(s.split(" ")[0])))


def describe_chart(chart):
    """ Returns the chart in textual representation. """

    text = describe_planets(chart)
    text += describe_houses(chart)
    text += describe_essential_dignities(chart)
    text += describe_accidental_dignities(chart)
    text += describe_aspects(chart, const.MAJOR_ASPECTS)
    return text


def describe_primary_directions(chart, **filters):
    """ Returns the list of primary directions as text. """
    table = PrimaryDirections.get_table(chart)

    text = "The primary directions are a predictive technique used in traditional astrology.\n"
    text += "The following list includes the arc of direction, direction and direction type "
    text += "(Zodiacal or Mundane directions).\n"
    for direction in table.filter_by(**filters):
        text += str(direction) + "\n"
    return text
