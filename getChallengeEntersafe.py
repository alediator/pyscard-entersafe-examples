#! /usr/bin/env python
"""
Sample script that tries to execute a GET CHALLENGE command in a FTCOS PKI Card.

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
GET_RESPONSE = [0x00, 0xC0, 0x00, 0x00]
# apdu bytes
CLA=0x00
INS=0x84
P1=0x00
P2=0x00
# LE get challenge (challenge length)
LE=0x08
# apdu get challenge
GET_CHALLENGE = [CLA, INS, P1, P2, LE]

# expected response
SW1_EXPECTED=0x90 

def entersafe_manage_get_challenge(response, sw1, sw2):

    # there is a OK
    if sw1 == SW1_EXPECTED:
	print 'Challenge is', toHexString(response)

    else: 
	if sw1==0x67:
		print 'Incorrect length'
	else: 
		if sw1 == 0x6e:
				print 'Invalid CLA'
		else: 
			if sw1 == 0x6A:
				if sw2 == 0x86:
					print 'Invalid P1/P2'
			else:
				print 'No entersafe'
			

def entersafe_get_challenge(cardservice):

    return test_apdu(GET_CHALLENGE, cardservice)
