pyscard-entersafe-exaples
=========================

Simple APDU commands for FTCOS PKI using pyscard

## Pre requisites: Pyscard instalation ##

Pyscard is the python smartcard library you need to execute this examples

### From source ###

1. Download [latest](http://sourceforge.net/projects/pyscard/files/latest/download)
2. Download and install  python dependencies
 * [distutils](http://docs.python.org/library/distutils.html)
3. Unpackage and install pyscard:
 <pre>setup.py install</pre>

### Debian package ###

<pre>~$ sudo apt-get install python-pyscard</pre>

## entersafe exercices ##

* GET CHALLENGE
* SELECT FILE

### GET CHALLENGE ###

<pre>
~$ ./sample_getChallenge.py
insert a card (SIM card if possible) within 10s
connecting to C3PO LTC31 (80060327) 00 00
&gt;  00 84 00 00 FF
&lt;  []  67 0 
Incorrect length
&gt;  00 84 11 00 08
&lt;  []  6A 86
Invalid P1/P2
&gt;  FF 84 00 00 08
&lt;  []  6E 0 
Invalid CLA
&gt;  00 84 00 00 08
&lt;  BB A2 E1 F1 AC 50 23 09 90 0 
Challenge is BB A2 E1 F1 AC 50 23 09
disconnecting from C3PO LTC31 (80060327) 00 00
~$
</pre>

### SELECT FILE ###

Complete the code:
<pre>
    # TODO:
    # 62 83 Invalid selected file
    # 69 85 Insufficient condition for using the command
    # 6A 81 Not supported function
    # 6A 82 File not found
    # 6A 86 Invalid P1/P2
    # 6E 00 Invalid CLA</pre>
