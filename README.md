# PyAstra

PyAstra is a Python library for Traditional Astrology.

It is the successor of flatlib (https://github.com/flatangle/flatlib/) and it is currently under
heavy development and rewrite. 

```python

>>> date = Datetime('2015/03/13', '17:00', '+00:00')
>>> pos = GeoPos('38n32', '8w54')
>>> chart = Chart(date, pos)

>>> sun = chart.get(const.SUN)
>>> print(sun)
<Sun Pisces +22:47:25 +00:59:51>

```

This project is currently for personal research only, therefore Pull Requests will be closed without review. 
Thank you for understanding.

It can be installed with `pip install git+https://github.com/joaoventura/pyastra.git`.

**Notes**: Python >= 3.10.
