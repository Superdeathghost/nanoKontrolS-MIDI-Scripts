"""
korgMarker.py
Author: Brandon "Ninja Reaper" Jones
Date: October 31, 2021
Desc: Handles marker setting and tracking.

Note: All buttons are coded 
with momentary in mind.
"""
import arrangement

# Class Constant
_BUTTON_DOWN = 127
_PREV_MARK = -1; _NEXT_MARK = 1
_SELECT = True

class MIDIMarker:
    """
    This class controls how 
    markers are set and tracked.
    """
    def __init__(self, set, prev, next):
        self._buttons = {
            "SET": set,
            "PREV": prev,
            "NEXT": next
        }

    # Handles moving between markers.
    def _toPrevMarker(self):
        """
        Moves to the previous marker.
        """
        arrangement.jumpToMarker(_PREV_MARK, _SELECT)
    def _toNextMarker(self):
        """
        Moves to next marker.
        """
        arrangement.jumpToMarker(_NEXT_MARK, _SELECT)

    # Handles marker placement.
    def _setMarker(self):
        """
        Sets marker at time and stores it.
        """
        time = arrangement.currentTime(True)
        arrangement.addAutoTimeMarker(time, "New Marker")

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

        # Checks if the button is down.
        if isButtonDown():
            # Checks which button is pressed.
            if checkType("SET"):
                self._setMarker()
            elif checkType("PREV"):
                self._toPrevMarker()
            elif checkType("NEXT"):
                self._toNextMarker()
        
        return True