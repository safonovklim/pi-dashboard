import time
import math
import datetime
import microdotphat

microdotphat.set_clear_on_exit(True)


def set_brightness(value):
    microdotphat.set_brightness(value)


def wait(seconds):
    time.sleep(seconds)


def reset():
    microdotphat.clear()
    microdotphat.show()


def print_string_fade(text):
    start = time.time()
    speed = 3
    shown = True

    b = 0
    while shown:
        b = (math.sin((time.time() - start) * speed) + 1) / 2
        microdotphat.set_brightness(b)

        if b < 0.002 and shown:
            microdotphat.clear()
            microdotphat.write_string(text, kerning=False)

            microdotphat.show()
            shown = False

        if b > 0.998:
            shown = True

        time.sleep(0.01)


def print_string(text):
    microdotphat.write_string(text, kerning=False)
    microdotphat.show()


# Duration in seconds
def show_time(duration = 10):
    repeat_in = 0.05
    repeat_times = int(duration / repeat_in)

    for counter in range(0, repeat_times):
        microdotphat.clear()
        t = datetime.datetime.now()
        if t.second % 2 == 0:
            microdotphat.set_decimal(3, 1)
        else:
            microdotphat.set_decimal(3, 0)
        microdotphat.write_string(t.strftime(' %H%M'), kerning=False)
        microdotphat.show()
        time.sleep(repeat_in)


def display_strings_array(lines):
    delay = 0.03

    line_height = microdotphat.HEIGHT + 2

    lengths = [0] * len(lines)

    offset_left = 0

    for line, text in enumerate(lines):
        lengths[line] = microdotphat.write_string(text, offset_x=offset_left, offset_y=line_height * line, kerning=False)
        offset_left += lengths[line]

    microdotphat.set_pixel(0, (len(lines) * line_height) - 1, 0)

    current_line = 0

    microdotphat.show()

    pos_x = 0
    pos_y = 0
    for current_line in range(len(lines)):
        time.sleep(delay * 10)
        for y in range(lengths[current_line]):
            microdotphat.scroll(1, 0)
            pos_x += 1
            time.sleep(delay)
            microdotphat.show()
        if current_line == len(lines) - 1:
            microdotphat.scroll_to(0, 0)
        else:
            for x in range(line_height):
                microdotphat.scroll(0, 1)
                pos_y += 1
                microdotphat.show()
                time.sleep(delay)


