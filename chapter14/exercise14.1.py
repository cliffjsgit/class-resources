#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 14.1
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "sed" should return None or a string error message and should 
# write out the new file with the changes outlined below.
# 
# 1. Write a function called "sed" that takes as arguments a pattern string, a
# replacement string, and two filenames; it should read the first file and write
# the contents into the second file (creating it if necessary). If the pattern
# string appears anywhere in the file, it should be replaced with the
# replacement string.
# 
# If an error occurs while opening, reading, writing or closing files, your
# program should catch the exception, return an error message as a
# string, and exit.
#

def sed(pattern,replacement,oldFile,newFile):
    tempFile = ""
    with open(oldFile,"r") as fin:
        for line in fin:
            tempFile += line.strip().replace(pattern,replacement) + "\n\r"
    with open(newFile,"w") as fout:
        fout.write(tempFile)

sed("Emma","Emma the Vampire","emma.txt","emma_the_vampire.txt")