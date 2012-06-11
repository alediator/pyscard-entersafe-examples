#! /usr/bin/env python
"""
Sample script that tries to execute a GET CHALLENGE command in a FTCOS PKI.

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
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString, toBytes
from getChallengeEntersafe import *

# apdu testing
GET_CHALLENGE_INCORRECT_LENGTH = [CLA, INS, P1, P2, 0xff]
GET_CHALLENGE_INVALID_P1_P2 = [CLA, INS, 0x11, P2, LE]
GET_CHALLENGE_INVALID_CLA = [0xff, INS, P1, P2, LE]


# request any card type
cardtype = AnyCardType()



try:
    # request card insertion
    print 'insert a card (SIM card if possible) within 10s'
    cardrequest = CardRequest(timeout=10, cardType=cardtype)
    cardservice = cardrequest.waitforcard()


    # attach the console tracer
    observer = ConsoleCardConnectionObserver()
    cardservice.connection.addObserver(observer)

    # connect to the card and perform a few transmits
    cardservice.connection.connect()

    # Incorrect length error
    response, sw1, sw2 = test_apdu(GET_CHALLENGE_INCORRECT_LENGTH, cardservice)
    entersafe_manage_get_challenge(response, sw1, sw2)

    # Invalid p1/p2 error
    response, sw1, sw2 = test_apdu(GET_CHALLENGE_INVALID_P1_P2, cardservice)
    entersafe_manage_get_challenge(response, sw1, sw2)

    # Invalid cla error
    response, sw1, sw2 = test_apdu(GET_CHALLENGE_INVALID_CLA, cardservice)
    entersafe_manage_get_challenge(response, sw1, sw2)

    # Correct Get challenge
    response, sw1, sw2 = entersafe_get_challenge(cardservice)
    entersafe_manage_get_challenge(response, sw1, sw2)
    

except CardRequestTimeoutException:
    print 'time-out: no card inserted during last 10s'

except:
    import sys
    print sys.exc_info()[1]

import sys
if 'win32' == sys.platform:
    print 'press Enter to continue'
    sys.stdin.read(1)
