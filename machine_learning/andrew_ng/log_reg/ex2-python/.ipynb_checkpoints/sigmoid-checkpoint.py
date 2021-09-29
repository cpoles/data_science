# sigmoid.py

import numpy as np
# define sigmoid function

def sigmoid(x):
    try:
        sig = 1 / (1 + np.exp(-x))
    except:
        raise ValueError('Error')
    return sig