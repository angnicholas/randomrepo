import pytest
from myproject.module2.file2 import anotherfunction


def test_anotherfunction():
    assert anotherfunction() == 2  # change to 2 to be green
