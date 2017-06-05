#!/usr/bin/env python3
#
# decode.py
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
import glob

from defs import *

"""
Decode data set written to the output file by the vna/j command line program.

"""

class Decode:
    
    def __init__(self):
        pass
    
    def fres(self):
        """ Find the resonant frequency in the result set """
        
        r, resultSet = self.__reader()
        first = True
        results = []
        swr = None
        resonantFreq = None
        if r:
            # Parse result set
            for line in resultSet:
                if first:
                    # Skip the headings line
                    first = False
                else:
                    temp = line.split(',')
                    if swr == None:
                        swr = temp[DEC_SWR]
                        resonantFreq = temp[DEC_FREQ]
                    else:
                        if temp[DEC_SWR] < swr:
                            swr = temp[DEC_SWR]
                            resonantFreq = temp[DEC_FREQ]

            results.append((resonantFreq, swr))
        return results
    
    def fswr(self):
        """ Find the SWR at the first frequency in the result set """
        
        r, resultSet = self.__reader()
        results = []
        if r:
            # We should only have 2 results of which the first is the required frequency
            results.append(resultset[1][DEC_FREQ], resultset[1][DEC_SWR])
        return results
    
    def scan(self):
        """ Return the entire scan """
        
        r, resultSet = self.__reader()
        first = True
        results = []
        if r:
            # Parse result set
            for line in resultSet:
                if first:
                    # Skip the headings line
                    first = False
                else:
                    temp = line.split(',')
                    results.append((temp[DEC_FREQ], temp[DEC_SWR]))                   
        return results
    
    def __reader(self):
        """ Read the result file """
        
        try:
            newest = max(glob.iglob(EXPORT_PATH + '/*.csv'), key=os.path.getctime)
            f = open(newest)
            return True, f.readlines()
        except ValueError:
            return False, None
                   