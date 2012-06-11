#! /usr/bin/env python
"""
Sample script that tries to simple apdu test command.

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

# apdus to use
GET_RESPONSE = [0x00,0xC0,0x00,0x00]

# expected response
SW1_EXPECTED=0x90 

def test_apdu(apdu, cardservice):

    return cardservice.connection.transmit(apdu)

def entersafe_get_response(cardservice):
    
    return cardservice.connection.transmit(GET_RESPONSE)

def entersafe_manage_get_response(response, sw1, sw2):

    # there is a OK
    if sw1 == SW1_EXPECTED:
	print 'Challenge is', toHexString(response)

    # error manage
    else: 
	if sw1 == 0x6E:
		print 'Invalid CLA'
	else: 
		if sw1 == 0x6F:
				print 'No available valid data to be returned from card'
		else: 
			if sw1 == 0x69 & sw2 == 0x85:
					print 'Insufficient condition for using the command'
			else:
				if sw1 == 0x6A & sw2 == 0x81:
						print 'Not supported function'
				else:
					if sw1 == 0x6C:
							print 'Reissue the command using "',sw2,'" as Le'

