"""
korgBtnConsts.py
Author: Brandon "Ninja Reaper" Jones
Date: November 3, 2021
Desc: Stores all button 
constants used by the main script.

*** CHANGE MIDI VALUES HERE. ***
Note: Some buttons need to be set to toggle 
and some need to be set to momentary.

Check the header comment above 
each set of constants to figure 
out what each button needs to be set to.
"""

"""
Transport Button Constants

Button Type Key:
- M = Momentary
- T = Toggle
"""
TRANSPORT = {
    "PLAY": 80, # M
    "STOP": 63, # M
    "START": 62, # M
    "CYCLE": 54, # M
    "RECORD": 81, # T
    "REWIND": 58, # T
    "FASTFORWARD": 59 # T
}

"""
UI Button Constants
- Note: All buttons need 
to be set to momentary.
"""
UI = {
    "PREV": 60,
    "NEXT": 61,
    "JOG": 83
}

"""
Marker Button Constants
- Note: All buttons need 
to be set to momentary.
"""
MARKER = {
    "SET": 55,
    "PREV": 56,
    "NEXT": 57
}

"""
Mixer Button Constants
- Note: All buttons need 
to be set to toggle.
"""
MIXER = [
    # Bus 1
    {
        "SELECT": 2,
        "MUTE": 13,
        "SOLO": 21,
        "ARM": 29,
        "KNOB": 38,
        "SLIDER": 46
    },

    # Bus 2
    {
        "SELECT": 3,
        "MUTE": 14,
        "SOLO": 22,
        "ARM": 30,
        "KNOB": 39,
        "SLIDER": 47
    },

    # Bus 3
    {
        "SELECT": 4,
        "MUTE": 15,
        "SOLO": 23,
        "ARM": 31,
        "KNOB": 40,
        "SLIDER": 48
    },

    # Bus 4
    {
        "SELECT": 5,
        "MUTE": 16,
        "SOLO": 24,
        "ARM": 33,
        "KNOB": 41,
        "SLIDER": 49
    },

    # Bus 5
    {
        "SELECT": 6,
        "MUTE": 17,
        "SOLO": 25,
        "ARM": 34,
        "KNOB": 42,
        "SLIDER": 50
    },

    # Bus 6
    {
        "SELECT": 8,
        "MUTE": 18,
        "SOLO": 26,
        "ARM": 35,
        "KNOB": 43,
        "SLIDER": 51
    },

    # Bus 7
    {
        "SELECT": 9,
        "MUTE": 19,
        "SOLO": 27,
        "ARM": 36,
        "KNOB": 44,
        "SLIDER": 52
    },

    # Bus 8
    {
        "SELECT": 12,
        "MUTE": 20,
        "SOLO": 28,
        "ARM": 37,
        "KNOB": 45,
        "SLIDER": 53
    }
]