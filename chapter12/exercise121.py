#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 12.1
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "most_frequent" should output a list of letters in decreasing
# order of frequency
#
# 1. Write a function called "most_frequent" that takes a file and returns 
# a list of letters in decreasing order of frequency. 
#
# Use emma.txt to test this function. Compare your results with the tables at:
# http://en.wikipedia.org/wiki/Letter_frequencies
#

def histogram(s):
    d = dict()
    for line in s:
        for char in filter(str.isalpha,line.strip()):
            d[char.lower()] = d.get(char.lower(),0) + 1
    return d

def most_frequent(file):
    fin = open(file)
    dictionary = histogram(fin)
    t = []
    for char, freq in dictionary.items():
        t.append((freq,char))
    t.sort(reverse=True)
    res = []
    for item in t:
        res.append(item[1])
    return res