"""
    This file is part of pyastra - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This subpackage implements a simple Ephemeris using 
    the Python port of the Swiss Ephemeris (Pyswisseph).
    
    The pyswisseph library must be already installed and
    accessible.
  
"""

import pyastra
from . import swe

# Set default swefile path
swe.set_path(pyastra.PATH_RES + 'swefiles')


def set_path(path):
    """ Sets the path for the ephemeris files. """
    swe.set_path(path)
