# unit_test.py
from _specipy.framework import *


@test
def a_passing_test():
    assert_true(1 + 2 == 3)


@test
def z_failing_test():
    assert_true(1 + 2 == 5)
