#name=Korg nanoKONTROL Studio

"""
Korg nanoKONTROL Studio Script
Author: Brandon "Ninja Reaper" Jones
Date: October 29, 2021
"""
# Imports Relevant Modules.
import midi

# Imports custom modules.
import korgBtnConsts as btnCon
from korgUI import MIDIUI
from korgTransport import MIDITransport
from korgMarker import MIDIMarker
from korgMixer import MIDIMixer

def OnMidiMsg(event):
    """
    Accepts MIDI events from DAW and directs 
    them to the correct manager objects.
    :param event: An object that contains MIDI event data.
    """
    event.handled = False
    # print(event.midiId, event.data1, event.data2)

    # Detects the type of MIDI input.
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        """
        Checks type of event data.
        Utilizes button constant dictionaries.
        """
        # Determines what manager to utilize.
        if event.data1 in btnCon.TRANSPORT.values():
            event.handled = transportManager.determineAction(event.data1, event.data2)
        elif event.data1 in btnCon.UI.values():
            event.handled = uiManager.determineAction(event.data1, event.data2)
        elif event.data1 in btnCon.MARKER.values():
            event.handled = markerManager.determineAction(event.data1, event.data2)
        else:
            for bus in range(len(btnCon.MIXER)):
                if event.data1 in btnCon.MIXER[bus].values():
                    event.handled = mixerManagers[bus].determineAction(event.data1, event.data2)

if __name__ == "__main__": 
    # Creates standard managers.
    uiManager = MIDIUI(btnCon.UI["PREV"], btnCon.UI["NEXT"], btnCon.UI["JOG"])
    transportManager = MIDITransport(\
        btnCon.TRANSPORT["PLAY"], btnCon.TRANSPORT["STOP"], \
        btnCon.TRANSPORT["START"], btnCon.TRANSPORT["CYCLE"], \
        btnCon.TRANSPORT["RECORD"], btnCon.TRANSPORT["REWIND"], \
        btnCon.TRANSPORT["FASTFORWARD"]
    )
    markerManager = MIDIMarker(btnCon.MARKER["SET"], btnCon.MARKER["PREV"], btnCon.MARKER["NEXT"])

    # Creates mixer managers.
    mixerManagers = []
    for bus in range(len(btnCon.MIXER)):
        mixerManagers.append(
            MIDIMixer(\
                btnCon.MIXER[bus]["SELECT"], btnCon.MIXER[bus]["MUTE"], \
                btnCon.MIXER[bus]["SOLO"], btnCon.MIXER[bus]["ARM"], \
                btnCon.MIXER[bus]["KNOB"], btnCon.MIXER[bus]["SLIDER"]
            )
        )