import numpy as np

from myproject.module1.file1 import somefunction


def anotherfunction():  # returns 2
    return somefunction() + (np.array([3, 1, 6])[1])
