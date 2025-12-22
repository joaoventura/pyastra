"""
Author: João Ventura <joaojonesventura@gmail.com>
This recipe shows sample code for generating text from a chart to use as prompts for large-language
models.

"""

from pyastra import *
from pyastra.integrations import llm


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Generate prompt for the natal chart and describe the natal chart as JSON
print(llm.NATAL_CHART_PROMPT_TEMPLATE)
print(llm.describe_chart_as_json(chart))

# Generate text for Traditional Astrology Protocols
print(llm.PROTOCOLS_PROMPT_TEMPLATE)
print(llm.describe_almutem(chart))
print(llm.describe_behavior(chart))
print(llm.describe_temperament(chart))

# Generate prompt for primary directions and describe the directions as text
print(llm.PRIMARY_DIRECTIONS_PROMPT_TEMPLATE)
print(llm.describe_primary_directions(
    chart, direction_type=const.PD_TYPE_ZODIACAL, min_arc=0, max_arc=100))

# Copy and paste it to an LLM and ask it questions
