#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 11.5
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "rotate_pair" should returns a dictionary of pairs.
#
# 1. Two words are "rotate pairs" if you can rotate one of them and get 
# the other (see rotate_word in Exercise 8.5). write a function called
# "rotate_pair" that takes in "words.txt" and returns a dictionary of
# pairs.
#

def make_dict(fin):
    fin=open(fin)
    mydict=dict()
    for word in fin:
        mydict[word.strip()] = 0
    return mydict

def rotate_word(word, n):
    rotated_word = ''
    for letter in word:
        rotated_word += chr(ord(letter) + n)
    return rotated_word

def rotate_pair(file):
    mydict = make_dict(file)
    pair = {}
    for word in mydict:
        for n in range(1, 26): 
            if rotate_word(word, n) in mydict:
                if word not in pair:
                    pair[word] = [rotate_word(word, n)]
                else:
                    pair[word].append(rotate_word(word, n))
                    
    return pair             