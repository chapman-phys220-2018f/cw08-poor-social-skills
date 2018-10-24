#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import sinesum
import math

def test_s():
    """
    Tests if the sinsum.s converges toward 1, 0, and -1 for the corresponding t values
    """
    testVal = sinesum.s(5, 2, 1000)
    testVal2 = sinesum.s(5, 0, 1000)
    testVal3 = sinesum.s(5, -2, 1000)
    assert (math.isclose(testVal, 0.999, abs_tol=1e-3) and math.isclose(testVal2, 0, abs_tol=1e-3) and math.isclose(testVal3, -0.999, abs_tol=1e-3))


def test_f():
    testVal = sinesum.f(5, 2)
    testVal2 = sinesum.f(5, 0)
    testVal3 = sinesum.f(5, -2)
    assert testVal == 1 and testVal2 == 0 and testVal3 == -1
