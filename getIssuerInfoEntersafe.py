#! /usr/bin/env python
"""
Sample script that tries to execute a SELECT FILE command in a FTCOS PKI Card.

__author__ = "http:www.emergya.es"

Copyright 2012 Emergya
Author: Alejandro Diaz Torres, mailto:adiaz@emergya.com

This file is part of pyscard-entersafe-exaples.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from smartcard.util import toHexString
from entersafeBase import *

# define the apdus used in this script


def entersafe_manage_get_issuer_info(response, sw1, sw2):

    # there is a OK
    if sw1 == SW1_EXPECTED:
	print 'Issuer info is', toHexString(response)
    else:
	if sw1==0x67:
		print 'Incorrect length'
	else: 
		if sw1 == 0x6e:
				print 'Invalid CLA'
		else: 
			if sw1 == 0x69:
				print 'Insufficient condition for using the command'
			else:
				
				if sw1 == 0x6C:
					print ' Length error for LE, 10 expected'
				else:
					if sw1 == 0x6A:
						if sw2 == 0x86:
							print 'Invalid P1/P2'
					else:
						print 'Not mapped response (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'

# TODO    
# 	SW1  SW2  Significado
#      
#	69   85   Insufficient condition for using the command
#       6C   10   Length error for LE, '10' expected
#	6A   86   Invalid P1/P2
#	6E   00   Invalid CLA
