#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "strip_and_lower" should return a list of the 20 most frequently
# used words in the book in order of usage, decending.
# 
# Question 1
# 1. Modify the function from the previous exercise to return a list of the
# 20 most frequently used words in the book in order of usage, decending. 
#

import string

def skip_header(fin):
    for line in fin:
        if "*END*THE SMALL PRINT!" in line:
            break

def make_histogram(fin):
    d = dict()
    for line in fin:
        line = line.replace("-"," ").strip().replace("'","")
        for word in line.split(" "):
            word = word.strip(string.punctuation).strip().lower()
            if word != "":
                d[word] = d.get(word,0) + 1
    return d

def invert_histogram(d):
    t = []
    for char, freq in d.items():
        t.append((freq,char))
    t.sort(reverse=True)
    res = []
    for item in t:
        res.append(item[1])
    return res

def strip_and_lower(file):
    fin = open(file)
    skip_header(fin)
    hist = make_histogram(fin)
    topList = invert_histogram(hist)
    
    return topList[:20]

strip_and_lower("emma.txt")