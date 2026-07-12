import sys
import os

sys.path.insert(0, "/system/apps/fireplace")
os.chdir("/system/apps/fireplace")

from badgeware import screen, io, run

FRAME_COUNT    = 20
FRAME_DURATION = 100   # ms per frame (matches original GIF)

_current_frame = 0
_last_tick     = None


def update():
    global _current_frame, _last_tick

    if _last_tick is None:
        _last_tick = io.ticks

    # Advance frame when enough time has passed
    if io.ticks - _last_tick >= FRAME_DURATION:
        _current_frame = (_current_frame + 1) % FRAME_COUNT
        _last_tick = io.ticks

    screen.load_into(f"frames/frame_{_current_frame:04d}.png")


run(update)
