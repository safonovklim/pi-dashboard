from dothat import backlight, lcd
import time

SINGLE_LINE_LENGTH = 16


def clear_text():
    lcd.clear()


def turn_off():
    backlight.off()
    backlight.set_graph(0)
    clear_text()


def wait(seconds):
    time.sleep(seconds)


def print_string(text):
    chars_on_line_used = len(text) % SINGLE_LINE_LENGTH
    if chars_on_line_used > 0:
        lcd.write(text + ((SINGLE_LINE_LENGTH - chars_on_line_used) * ' '))
    else:
        lcd.write(text)