"""
PyAstra main package

"""

import os

# Library and resource paths
PATH_LIB = os.path.dirname(__file__) + os.sep
PATH_RES = PATH_LIB + 'resources' + os.sep

# Imports for easy access
from pyastra import const
from pyastra.core.chart import Chart
from pyastra.core.datetime import Datetime
from pyastra.core.geopos import GeoPos

# Available on "from pyastra import *"
__all__ = ['const', 'Chart', 'Datetime', 'GeoPos']
