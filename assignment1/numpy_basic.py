# show examples of basic numpy functions:
# shape, reshape, apply_along_axis, max

import numpy as np
import random


def test_basic_np_funcs():
    a = np.array([
        [1, 2, 3],
        [3, 5, 7]])

    x = np.apply_along_axis(lambda x: np.max(x), 1, a)
    y = np.apply_along_axis(lambda x: np.max(x), 0, a)

    print x  # [3, 7]
    print y  # [3, 5, 7]
    # print a -x  ValueError: operands could not be broadcast together with
    # shapes (2,3) (2,)
    print a - x.reshape(x.shape[0], 1)
    """
        [[-2 -1  0]
         [-4 -2  0]]
    """
    print y.shape  # (3, )
    print y.reshape(y.shape[0], 1)  # ([[3], [5], [7]])
    print np.max(a)  # 7
    print a.shape  # (2 ,3)

def test_random():
    rndstate = random.getstate()
    random.setstate(rndstate)
    print rndstate

if __name__ == "__main__":
    #test_basic_np_funcs()
    test_random()
