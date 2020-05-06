import board
from adafruit_clue import clue
import displayio
import time
from gauge import Gauge

display = board.DISPLAY
  

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
