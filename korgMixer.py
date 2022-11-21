"""
korgMixer.py
Author: Brandon "Ninja Reaper" Jones
Date: October 30, 2021
Desc: Handles the Korg's mixer functionality.

Note: All buttons are coded 
with toggle in mind.
"""
# Imports Control Modules.
import ui
import mixer

_MASTER = 0; _CURRENT = 126
_BUTTON_UP = 0; _BUTTON_DOWN = 127
_SOLO = 1; _UNSOLO = 0
_MAX_VAL = 127

class MIDIMixer:
    """
    This class controls how nanoKONTROL's
    mixer functionality works.
    """
    def __init__(self, select, mute, solo, arm, knob, slider):
        self._buttons = {
            "SELECT": select, 
            "MUTE": mute,
            "SOLO": solo,
            "ARM": arm,
            "KNOB": knob,
            "SLIDER": slider
        }
        self.mixerIndex = _MASTER
        self.busCaptured = False

    # Select Functions
    def _captureMixerBus(self):
        """
        Captures the index of a
        selected mixer bus.
        """
        if mixer.trackNumber() > _MASTER and mixer.trackNumber() < _CURRENT:
            ui.setHintMsg("Capturing mixer track #"
            + str(mixer.trackNumber()) + ".")
            self.mixerIndex = mixer.trackNumber()
            self.busCaptured = True
    def releaseMixerBus(self):
        """
        \"Releases\" captured 
        mixer bus index.
        """
        if self.busCaptured:
            ui.setHintMsg("Releasing mixer track #"
            + str(self.mixerIndex) + ".")
            self.mixerIndex = _MASTER
            self.busCaptured = False

    # Mute Function(s)
    def _toggleMuteState(self):
        """
        Toggles mixer bus mute state.
        """
        if self.busCaptured:
            mixer.muteTrack(self.mixerIndex)
            ui.setHintMsg("Toggled mute state of bus #" 
            + str(self.mixerIndex) + ".")

    # Solo Function(s)
    def _soloBus(self):
        """
        Solos mixer bus.
        """
        if self.busCaptured and not mixer.isTrackSolo(self.mixerIndex):
            mixer.soloTrack(self.mixerIndex, _SOLO)
            ui.setHintMsg("Soloed bus #" 
            + str(self.mixerIndex) + ".")
    def _unsoloBus(self):
        """
        Unsolos mixer bus.
        """
        if self.busCaptured and mixer.isTrackSolo(self.mixerIndex):
            mixer.soloTrack(self.mixerIndex, _UNSOLO)
            ui.setHintMsg("Unsoloed bus #" 
            + str(self.mixerIndex) + ".")

    # Arm (Rec) Function(s)
    def _toggleArmState(self):
        """
        Toggles mixer bus recording.
        """
        if self.busCaptured:
            mixer.armTrack(self.mixerIndex)
            ui.setHintMsg("Toggled arm state of bus #" 
            + str(self.mixerIndex) + ".")

    # Knob Function(s)
    def _setBusPan(self, value):
        """
        Sets mixer bus panning value.
        :param value: The control's value.
        """
        if self.busCaptured:
            panVal = value / (_MAX_VAL / 2) - 1
            mixer.setTrackPan(self.mixerIndex, panVal)

    # Slider Function(s)
    def _setTrackVol(self, value):
        """
        Sets mixer bus volume value.
        :param value: The control's value.
        """
        if self.busCaptured:
            mixer.setTrackVolume(self.mixerIndex, value / _MAX_VAL)

    # Main Function.
    def determineAction(self, cType, cVal):
        """
        Determines what action to take.
        :param controlType: The control input being used.
        :param controlValue: Value of the control type.
        :return: True - The event was handled.
        """
        # Creates internal lambda functions for checks.
        isButtonUp = lambda: cVal == _BUTTON_UP
        isButtonDown = lambda: cVal == _BUTTON_DOWN
        checkType = lambda c_t: cType == self._buttons[c_t]

        # Handles capturing and releasing.
        if checkType("SELECT") and isButtonDown():
            self._captureMixerBus()
        elif checkType("SELECT") and isButtonUp():
            self.releaseMixerBus()

        # Handles button functionality.
        elif checkType("MUTE"):
            self._toggleMuteState()
        elif checkType("SOLO") and isButtonDown():
            self._soloBus()
        elif checkType("SOLO") and isButtonUp():
            self._unsoloBus()
        elif checkType("ARM"):
            self._toggleArmState()

        # Handles knob and slider functionality.
        elif checkType("KNOB"):
            self._setBusPan(cVal)
        elif checkType("SLIDER"):
            self._setTrackVol(cVal)

        return True