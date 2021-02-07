# Utility functions
import os
import sys
from .cfg import MIN_BIG_WIDTH, MIN_BIG_HEIGHT


# Cell do as // but ceil instead of floor, ok for integers
def ceil(n, d):
    return (n + d - 1) // d


# TODO check sur windows que curses donne bien les coord maj car j'utilise encore la fonction classique
# Get Terminal size for windows
# Thanks UpGaDo https://github.com/UpGado/ascii_racer
def get_terminal_size():
    if sys.platform == 'win32':
        return _get_terminal_size_windows()
    else:
        return _get_terminal_size_unix()


def _get_terminal_size_windows():
    # http://code.activestate.com/recipes/440694-determine-size-of-console-window-on-windows/
    from ctypes import windll, create_string_buffer

    # stdin handle is -10
    # stdout handle is -11
    # stderr handle is -12

    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

    if res:
        import struct
        (_, _, _, _, _, left, top, right, bottom,
         *_) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
    else:                                                      # can't determine actual size
        sizex, sizey = MIN_BIG_WIDTH + 4, MIN_BIG_HEIGHT + 4   # 80 x 25 for VT100 standard i guess
    return (sizey, sizex)


def _get_terminal_size_unix():
    return tuple(int(i) for i in os.popen('stty size', 'r').read().split())
