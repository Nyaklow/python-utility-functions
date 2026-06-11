# This question concerns devising a set of tests for 'format_date' that cumulatively achieve path coverage. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 23 April 2025

"""
>>> import dateutil
>>> dateutil.format_date(5, 13, 2024)
'Invalid date'
>>> dateutil.format_date(31, 9, 2024)
'Invalid date'
>>> dateutil.format_date(30, 9, 2024)
'30 September 2024'
>>> dateutil.format_date(30, 2, 2024)
'Invalid date'
>>> dateutil.format_date(29, 2, 2024)
'29 February 2024'
>>> dateutil.format_date(28, 2, 2023)
'28 February 2023'
>>> dateutil.format_date(29, 2, 2023)
'Invalid date'
>>> dateutil.format_date(32, 12,2024)
'Invalid date'
>>> dateutil.format_date(31, 12, 2024)
'31 December 2024'

"""

import doctest
doctest.testmod(verbose=True)
