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
                        if float(temp[DEC_SWR]) < float(swr):
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
            temp = resultSet[1].split(',')
            results.append((temp[DEC_FREQ], temp[DEC_SWR]))
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
            if sys.platform == 'win32':
                exportPath = WIN_EXPORT_PATH
            elif sys.platform == 'linux':
                exportPath = LIN_EXPORT_PATH
            else:
                print('Unsupported platform %s' % (sys.platform))
                return
            newest = max(glob.iglob(exportPath + '/*.csv'), key=os.path.getctime)
            f = open(newest)
            data = f.readlines()
            f.close()
            # Remove old files
            files = glob.glob(exportPath + '/*.csv')
            for file in files:
                if file != newest:
                    os.remove(file)
            return True, data
        except ValueError:
            return False, None
                   