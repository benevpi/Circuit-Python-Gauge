import board
from adafruit_clue import clue
import displayio
import time
from gauge import Gauge

display = board.DISPLAY

#basics working.
#TodDo -- graphical niceties
### Add a circle at the bottom
### Add a text number display
### Maybe some options for coloured backgrounds
### Maybe a warning threshold?
# speed optimisations
#flip it the right way up!
#always have it from 45 deg to 45 deg. Everything is a lot easier then.

#test at different sizes
## current fps @ 240x240 circa 6

#Do an arc-style one

#problem -- aliasing gives is a dip in the middle. Not too sure what I can do about this.
# not too sure about  the best thing here. Could detect this and boost the length at exactly the mid point
#Outline fixes this, but at the expense of about doubling the refresh rate
  

colour_fade=[
    0x00FF00,
    0x00FF00,
    0x00FF00,
    0xFFFF00,
    0xFFFF00,
    0xFFFF00,
    0xFFFF00,
    0xFF0000,
    0xFF0000,
    0xFF0000]
gauge = Gauge(-10,10, 120, 120, value_label="x:")
y_gauge = Gauge(-10,10, 120, 120, value_label="y:", arc_colour=colour_fade, colour_fade=True)

y_gauge.x = 120


group = displayio.Group(scale=1)

group.append(gauge)
group.append(y_gauge)

display.show(group)
board.DISPLAY.auto_refresh = True
while True:
    x, y, _ = clue.acceleration
    start = time.monotonic()
    gauge.update(x)
    y_gauge.update(y)
    print(time.monotonic()-start)
