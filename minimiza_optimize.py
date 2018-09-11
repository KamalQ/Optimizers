import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):

    Y = (X - 1.5)**2 + 0.5
    print('X = {}, Y={}'.format(X,Y))
    return Y