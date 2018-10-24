#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Trevor Kling
# Student ID: 002270716
# Email: kling109@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW08
###

import numpy as np

def s(T, t, n):
    """
    Implements a summation of a sin-based function with defined constants T and t.  The sum is computed
    up to a value n, and should converge to 1, -1, or 0 depending on the range t falls into.
    0 < t < T/2: Converges to 1.
    t = 0: Converges to 0.
    -T/2 < t < 0: Converges to -1
    """
    summationArray = np.arange(1, n+1)
    def func(k):
        return (((1)/(2*k - 1))*np.sin((2*(2*k - 1)*np.pi*t)/(T)))
    summer = np.vectorize(func)
    result = (4/np.pi)*np.sum(summer(summationArray))
    return result

def f(T, t):
    """
    Checks if t is between particular values, and returns what the above function will converge to at
    infinity for the given t value.
    """
    if 0 < t < (T/2):
        return 1
    elif t == 0:
        return 0
    elif -(T/2) < t < 0:
        return -1
    else:
        print("That is not within the given range of [-T/2, T/2]")
        return None
