#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.2
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "strip_and_lower" should return a histogram in the form of a
# dictionary where the key is the word and the value is the number of times
# it occured.
#
# 1. Modify your function from the previous exercise to skip over the header 
# information at the beginning of the file, and process the rest of the words 
# as before. Then modify the function to count the total number of words in 
# the book, and the number of times each word is used. Use a histogram to
# collect this info and return that dictionary -- where the key is the word 
# and the value is the number of times it occured. 
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
            d[word] = d.get(word,0) + 1
    return d

def strip_and_lower(file):
    fin = open(file)
    skip_header(fin)
    hist = make_histogram(fin)
    
    return hist

strip_and_lower("emma.txt")