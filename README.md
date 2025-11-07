# PyAstra

PyAstra is a python library for Traditional Astrology. 
This project is the official successor of flatlib (https://github.com/flatangle/flatlib/).

```python

>>> date = Datetime('2015/03/13', '17:00', '+00:00')
>>> pos = GeoPos('38n32', '8w54')
>>> chart = Chart(date, pos)

>>> sun = chart.get(const.SUN)
>>> print(sun)
<Sun Pisces +22:47:25 +00:59:51>

```

## Documentation

PyAstra's documentation is still not available, as this library is currently being updated.
Flatlib's documentation is still available at [http://flatlib.readthedocs.org/](http://flatlib.readthedocs.org/).


## Installation

PyAstra is a Python 3 package, make sure you have Python 3 installed on your system.
To use the latest version of PyAstra from the repository, you can download a zip file,
install pyswisseph (version 2.10.3.2), and copy the pyastra package to your own project.

You can still install the previous flatlib with `pip3 install flatlib` or download the 
latest stable version from [https://pypi.python.org/pypi/flatlib](https://pypi.python.org/pypi/flatlib) and install it with 
`python3 setup.py install`. 


## Development

You can clone this repository or download a zip file using the right side buttons. 