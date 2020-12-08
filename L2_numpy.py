# -*- coding: utf-8 -*-

"""
Created on 12/8/20 10:34 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import numpy as np

if __name__ == '__main__':
    vector = np.array([1, 2, 3, 4])
    matrix = np.array([[1, 'Jenny'], [2, 'Justin']])
    reshaped = vector.reshape(2,2)
    print(reshaped)
