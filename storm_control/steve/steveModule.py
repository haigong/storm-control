#!/usr/bin/env python
"""
The base class for all of the modules in Steve.

Hazen 10/18
"""

from PyQt5 import QtWidgets

import storm_control.sc_library.hdebug as hdebug


class SteveModule(QtWidgets.QWidget):

    @hdebug.debug
    def __init__(self, comm = None, parameters = None, **kwds):
        super().__init__(**kwds)

        self.comm = comm
        self.parameters = parameters
    
    @hdebug.debug
    def halMessageSend(self, message):
        """
        Sends a message to HAL message via the comm object.
        """
        self.comm.sendmessage(message)


        
