"""
korgTransport.py
Author: Brandon "Ninja Reaper" Jones
Date: November 3, 2021
Desc: Handles the transport 
functions of the nanoKONTROL.

M = Momentary
T = Toggle
"""
import midi
import ui
import transport

# Class Constants.
_BUTTON_UP = 0; _BUTTON_DOWN = 127
_SS_START = 2; _SS_STOP = 0
_SONG_START = 0

class MIDITransport:
    """
    This class controls the Korg\'s 
    transport capabilities.
    """
    def __init__(self, play, stop, start, cycle, record, rewind, fastForward):
        self._buttons = {
            "PLAY": play, #M
            "STOP": stop, #M
            "START": start, #M
            "CYCLE": cycle, #M
            "RECORD": record, #T
            "REWIND": rewind, #T
            "FORWARD": fastForward #T
        }

    """
    Core Functions.
    """
    def _togglePlay(self):
        """
        Toggles the play status of the DAW.
        """
        transport.start()
    
    def _toggleStop(self):
        """
        Toggles the stop status of the DAW.
        """
        transport.stop()

    def _skipToStart(self):
        """
        Skips the playback to the start.
        """
        transport.setSongPos(_SONG_START)

    def _cycleLoopMode(self):
        """
        Cycles between song and pattern modes.
        """
        transport.setLoopMode()

    def _toggleRecord(self):
        """
        Toggles to the DAW\'s recording status.
        """
        transport.record()

    """
    Playback Speed Functions.
    """
    def _startRewind(self):
        """
        Starts the DAW\'s rewind functionality.
        """
        ui.setHintMsg("Engaging rewind.")
        transport.rewind(_SS_START, midi.GT_All)
    
    def _stopRewind(self):
        """
        Stops the DAW\'s rewind functionality.
        """
        ui.setHintMsg("De-engaging rewind.")
        transport.rewind(_SS_STOP, midi.GT_All)

    def _startForward(self):
        """
        Starts the DAW\'s fast-forward functionality.
        """
        ui.setHintMsg("Engaging fast-foward.")
        transport.fastForward(_SS_START, midi.GT_All)
    
    def _stopForward(self):
        """
        Stops the DAW\'s fast-forward functionality.
        """
        ui.setHintMsg("De-engaging fast-forward.")
        transport.fastForward(_SS_STOP, midi.GT_All)

    # Main Function.
    def determineAction(self, cType, cVal):
        """
        Determines which action to take based on button pressed.
        :param controlType: The control input being used.
        :param controlValue: Value of the control type.
        :return: True - The event was handled.
        """
        # Creates internal lambda functions for checks.
        isButtonUp = lambda: cVal == _BUTTON_UP
        isButtonDown = lambda: cVal == _BUTTON_DOWN
        checkType = lambda c_t: cType == self._buttons[c_t]

        # Handles base transport functionality.
        if checkType("PLAY") and isButtonDown(): 
            self._togglePlay()
        elif checkType("STOP") and isButtonDown():
            self._toggleStop()
        elif checkType("START") and isButtonDown():
            self._skipToStart()
        elif checkType("CYCLE") and isButtonDown():
            self._cycleLoopMode()
        elif checkType("RECORD"):
            self._toggleRecord()

        # Handles playback speed functionality.
        elif checkType("REWIND") and isButtonDown():
            self._startRewind()
        elif checkType("REWIND") and isButtonUp():
            self._stopRewind()
        elif checkType("FORWARD") and isButtonDown():
            self._startForward()
        elif checkType("FORWARD") and isButtonUp():
            self._stopForward()

        return True