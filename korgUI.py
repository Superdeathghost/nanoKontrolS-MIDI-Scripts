"""
korgUI.py
Author: Brandon "Ninja Reaper" Jones
Date: November 3, 2021
Desc: Handles the UI
functions of the nanoKONTROL.

Note: All buttons are coded
with momentary in mind.
"""
import ui

# Class Constant(s).
_BUTTON_DOWN = 127

class MIDIUI:
    """
    This class handles the 
    Korg's UI functionality.
    """
    def __init__(self, prev, next, jog):
        self._buttons = {
            "PREVIOUS": prev,
            "NEXT": next,
            "JOG": jog
        }

    def _goPrev(self):
        """
        Enables generic previous control.
        """
        ui.previous()
    
    def _goNext(self):
        """
        Enables generic next control.
        """
        ui.next()
    
    def _useJog(self, value):
        """
        Enables jog wheel usage.
        :param value: Jog wheel value.
        """
        ui.jog(value)

    # Main Function.
    def determineAction(self, cType, cVal):
        """
        Determines which action to take based on button pressed.
        :param controlType: The control input being used.
        :param controlValue: Value of the control type.
        :return: True - The event was handled.
        """
        # Creates internal lambda functions for checks.
        isButtonDown = lambda: cVal == _BUTTON_DOWN
        checkType = lambda c_t: cType == self._buttons[c_t]

        # Codes in standard UI functionality.
        if checkType("PREVIOUS") and isButtonDown():
            self._goPrev()
        elif checkType("NEXT") and isButtonDown():
            self._goNext()
        elif checkType("JOG"):
            self._useJog(cVal)

        return True