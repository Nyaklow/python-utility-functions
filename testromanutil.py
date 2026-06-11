# This question concerns devising a set of tests for 'from_roman' that cumulatively achieve path coverage. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 23 April 2025

"""
>>> import romanutil
>>> romanutil.from_roman('VI')
6
>>> romanutil.from_roman('IV')
4
>>> romanutil.from_roman('XXXIV')
34
>>> romanutil.from_roman('DMIX')
509
>>> romanutil.from_roman('MIX')
1009
>>> romanutil.from_roman('VIII')
8

"""
import doctest
doctest.testmod(verbose=True)
