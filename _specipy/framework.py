# test_framework.py
def test(f):
    f.is_test = True
    return f


class AssertionException(Exception):
    pass


def assert_true(conditional):
    if not conditional:
        raise AssertionException("Expected True. Was False")
