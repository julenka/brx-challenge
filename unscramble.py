#!/usr/bin/env python
# coding=utf-8
""" 
"""
__author__ = 'julenka'

scrambled_file = open("strings_scrambled.txt")

# 0 1 2 3 -> 1 0 2 3
lines = []
for line in scrambled_file:
    line = line.replace("\"", " ")
    a, b, c, d = line[:4]
    lines.append("{}{}{}{}".format(b, a, c, d))

# linea
# lineb

# to:
# lineb
# linea
print
print "reversed:"
print

for i in xrange(1, len(lines), 2):
    print lines[i + 1] + lines[i]



