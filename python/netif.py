#!/usr/bin/env python3
#
# netif.py
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
import threading
import socket
from defs import *

"""
Interface to the MiniVNA Tiny application:

Commands are UDP:
    fres(lower, upper)  --  return the frequency at which the antenna is currently resonant
                            The frequency hints give the lower and upper frequency to scan.
                            If no resonant point is found return None.
    fswr(freq)          --  Retuen the SWR at the given frequency.
    scan(lower, upper)  --  return the full scan results between lower and upper.

"""

class NetIF(threading.Thread):
    
    def __init__(self, callback):
        """
        Constructor
        
        Arguments:
            callback    --  callback here when data arrives
            
        """

        super(NetIF, self).__init__()
        
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind((EVNT_IP, EVNT_PORT))
        self.__sock.settimeout(3)
        
        self.__address = None
        self.__terminate = False
    
    def terminate(self):
        """ Terminate thread """
        
        self.__terminate = True
    
    def response(self, data):
        """
        Send response data
        
        Arguments:
            data    --  bytestream to send
        
        """
        
        if self.__address != None:
            try:
                self.__sock.sendto(data, self.__address)
                
            except Exception as e:
                print('Exception on socket send %s' % (str(e)))
                
    def run(self):
        """ Listen for requests """
        
        while not self.__terminate:
            try:
                data, self.__address = self.__sock.recvfrom(100)
                self.__callback(data)
            except socket.timeout:
                continue
            