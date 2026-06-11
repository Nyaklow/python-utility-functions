# This question concerns devising a set of tests for 'timeutil.py' that cumulatively achieve path coverage. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 23 April 2025

"""
>>> import timeutil
>>> timeutil.validate('01:30 a.m.')
False
>>> timeutil.validate('22 15 p.m.')
False
>>> timeutil.validate('1:15 ')
False
>>> timeutil.validate('NN:44 p.m.')
False
>>> timeutil.validate('11:ab a.m.')
False
>>> timeutil.validate('11:59 p.m.')
True

"""
import doctest
doctest.testmod(verbose=True)
