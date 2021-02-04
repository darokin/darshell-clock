import pytest


def func(x):
    return x + 1


def test_fake():
    assert func(41) == 42