#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 04:43:24 2022

@author: bbq
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

# Step 1: User set an int number

num_set = int(sys.argv[1])

# Step 2: User set the directory

dir_work = sys.argv[3]

# Step 3: if calculation starts:
results = np.random.random((num_set,))


figure = plt.figure()
axes = figure.add_subplot(1,1,1)
axes.plot(results)

time.sleep(int(sys.argv[2])) # To simulate the calculation time
plt.savefig(dir_work+'/demo_fig.jpg')

print('success')
sys.stdout.flush()


