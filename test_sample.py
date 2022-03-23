# content of test_sample.py
def func(x):
    return x + 2


def test_answer():
    assert func(3) == 5

def test_fail():
    assert func(3) == 6