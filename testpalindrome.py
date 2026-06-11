# This question concerns devising a set of tests for 'is_palindrome()' that cumulatively achieve path coverage. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 23 April 2025

"""
>>> import palindrome
>>> palindrome.is_palindrome('level')
True
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('Level')
False
>>> palindrome.is_palindrome('asantaatnasa')
True
>>> palindrome.is_palindrome('s')
True

"""
import doctest
doctest.testmod(verbose=True)