import os
from evdev import InputDevice, categorize, ecodes
import keyboard
# event-number from /proc/bus/input/devices
dev = InputDevice('/dev/input/event19')
dev.grab()
commands = { # hardware 
  "KEY_NUMLOCK":    'F4', # shido white
  "KEY_KPSLASH":    'F8', # shido blue
  "KEY_KPASTERISK": '2', # new/ok (2 minutes)
  "KEY_KPMINUS":    '', # - (dash)
  "KEY_KP7":        'F1', # ippon white
  "KEY_KP8":        'F5', # ippon blue
  "KEY_KP9":        '9', # gold/auto 
  "KEY_KP4":        'F2', # wazari white
  "KEY_KP5":        'F6', # wazari blue
  "KEY_KP6":        '', # hantei
  "KEY_KP1":        'Shift+F1+F2', # yuko white->remove white's score
  "KEY_KP2":        'Shift+F5+F6', # yuko blue->remove blue's score
  "KEY_KP3":        'Up', # white
  "KEY_KP0":        'space', # hajime/mate
  "KEY_KPDOT":      'Down', # red
  "KEY_KPPLUS":     '', # sonomama/yoshi
  "KEY_KPENTER":    'Return'  # osaekomi/toketa
}

# os.system runs command as if bash script, 'xdotool key' simulates key presses

for event in dev.read_loop():
  if event.type == ecodes.EV_KEY:
    key = categorize(event)
    if key.keystate == key.key_down:
      os.system('xdotool key '+commands[key.keycode])
