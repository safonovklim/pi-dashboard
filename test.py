#!/usr/bin/env python

from dothat import backlight, lcd, touch
from time import sleep
from api import displayotronhat

SINGLE_LINE_LENGTH = 16


def get_new_index(default_position, offset):
    new_index = default_position + offset
    if new_index > 5:
        return new_index - 5
    return new_index


@touch.on(touch.BUTTON)
def handle_button_tap(ch, evt):
    displayotronhat.print_string('PARTY TIME!!1')


try:
    displayotronhat.print_string('11 Nov 2017')
    displayotronhat.print_string('Moscow +4 °C')
    displayotronhat.print_string('1 BTC = $ 1234')

    offset = 0
    while True:
        backlight.single_rgb(get_new_index(0, offset), 255, 0, 0)
        backlight.single_rgb(get_new_index(1, offset), 255, 255, 0)
        backlight.single_rgb(get_new_index(2, offset), 128, 255, 0)
        backlight.single_rgb(get_new_index(3, offset), 0, 128, 255)
        backlight.single_rgb(get_new_index(4, offset), 127, 0, 255)
        backlight.single_rgb(get_new_index(5, offset), 128, 128, 128)
        # backlight.set_graph(0.2 * offset)

        sleep(0.02)
        if offset == 5:
            offset = 0
        else:
            offset += 1

except KeyboardInterrupt:
    backlight.off()
    backlight.set_graph(0)
    lcd.clear()
