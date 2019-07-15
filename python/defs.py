#!/usr/bin/env python3
#
# defs.py
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

# Net interface defs
RQST_IP = ''
RQST_PORT = 10002

# Types
RQST_FRES = 'fres'
RQST_FSWR = 'fswr'
RQST_SCAN = 'scan'

# Scanner defs
CAL_FILE = 'REFL_miniVNA Tiny.cal'
SCAN_MODE = 'REFL'
EXPORTS = 'csv'
WIN_JAR = 'E:\\Projects\\MiniVNA\\VNAJ\\vnaJ-hl.3.2.10.jar'
LIN_JAR = '/home/pi/MiniVNA/VNAJ/vnaJ-hl.3.2.10.jar'

# Decoder defs
WIN_EXPORT_PATH = 'C:\\Users\\User\\VNAJ\\export'
LIN_EXPORT_PATH = '/home/pi/VNAJ/export'
DEC_FREQ = 0
DEC_SWR = 4

