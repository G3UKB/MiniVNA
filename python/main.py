#!/usr/bin/env python3
#
# main.py
# 
# Copyright (C) 2017 by G3UKB Bob Cowdery
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#    
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#    
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#    
#  The author can be reached by email at:   
#     bob@bobcowdery.plus.com
#

import os, sys
from defs import *
from time import sleep
import pickle

import netif
import vna
import decode

"""
    Main program for the VNA addon.
    This module provides SWR data as requested by the user over UDP.
    It is targetted to run on the RPi and connect to the MiniVNA Tiny via USB.
    However it will also run underWindows and other Linux distributions.
    Required Python 3.x
"""

class VNAMain:
    
    def __init__(self):
        
        # Run the net interface as this is the active thread.
        self.__netif = netif.NetIF(self.__netCallback)
        self.__netif.start()
        
        # Create a VNA reader
        self.__vna = vna.VNA()
        
        # Create a decoder
        self.__decoder = decode.Decode()        
        
    def mainLoop(self):
        
        try:
            # Main loop for ever
            while True:
                sleep(1)                
                
        except KeyboardInterrupt:
            
            # User requested exit
            # Terminate the netif thread and wait for it to close
            self.__netif.terminate()
            self.__netif.join()
            
            print('Interrupt - exiting...')
            
    def __netCallback(self, data):
        
        # Data arrived from caller
        try:
            request = pickle.loads(data)
            # request is an array of type followed by one or more parameters
            type = request[0]
            if type == RQST_FRES:
                if len(request) != 3:
                    print('Request %s requires 2 parameters, received %d' % (type, len(request)-1))
                    return
                if self.__vna.fres(request[1], request[2]):
                    self.__netif.response(self.__decoder.fres())
            elif type == RQST_FSWR:
                if len(request) != 2:
                    print('Request %s requires 1 parameters, received %d' % (type, len(request)-1))
                    return
                if self.__vna.fswr(request[1]):
                    self.__netif.response(self.__decoder.fswr())
            elif type == RQST_SCAN:
                if len(request) != 3:
                    print('Request %s requires 2 parameters, received %d' % (type, len(request)-1))
                    return
                if self.__vna.scan(request[1], request[2]):
                    self.__netif.response(self.__decoder.scan())
            else:
                print('Unknown request type %s!' % (type))
            
        except pickle.UnpicklingError:
            print('Failed to unpickle request data!')

# Entry point            
if __name__ == '__main__':
    main = VNAMain()
    main.mainLoop()        
    