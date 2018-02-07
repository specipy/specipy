# test_runner.py
import inspect

from _specipy.framework import AssertionException
from tests.examples import unit_test


def run_test(test_name, test_method):
    try:
        print(">", test_name)
        test_method()
        print("Passed")
    except AssertionException as error:
        print("Failed with AssertionException: " + str(error))
    except Exception as error:
        print("Failed with Exception: " + str(error))


if __name__ == "__main__":
    members = inspect.getmembers(unit_test)
    for member in members:
        if "is_test" in dir(member[1]):
            run_test(member[0], member[1])
