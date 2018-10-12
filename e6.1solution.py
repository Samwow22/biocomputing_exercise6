#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:43:10 2018

@author: Samuel_Clarin
"""
#exercise 6 problem 1
#fname is file name, nlines is number of rows you want to return
#usage: head(filename, # of lines you want to return)


def head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
