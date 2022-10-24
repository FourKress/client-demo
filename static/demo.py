#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 04:43:24 2022

@author: bbq
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocessing
import sys
import json

params = json.loads(sys.argv[1])

class matrix_test():
    def __init__(self,num,num_col=2):
        self.num_col = num_col
        self.data = np.zeros(shape=(num,self.num_col))
    pass

    def update_matrix_queue(self,queue):
        n = 10000
        data = queue.get()
        num_row = np.shape(data)[0]
        for i in range(n):
            randnum = np.random.random((num_row,self.num_col))
            data = data+randnum
        pass
        queue.put(data)
    pass

    def split_data_into_queues(self,index_range,list_queues):
        for i in range(num_pieces):
            indexs_row = index_range[i]
            list_queues[i].put(self.data[indexs_row[0]:indexs_row[1],:])
        pass
    pass

    def assemble_data_from_queues(self,index_range,list_queues):
        for i in range(num_pieces):
            indexs_row = index_range[i]
            self.data[indexs_row[0]:indexs_row[1],:] = list_queues[i].get()
        pass
    pass

def task_update_matrix(matrix_test,queue):
    matrix_test.update_matrix_queue(queue)
pass


# Step 1: User set an int number
num_set = params['num_set']

# Step 2: User set the directory

dir_work = params['dir_work']

# Step 3: if calculation starts:
num_rows = num_set
num_pieces = 3
num_iter = 1000
list_tasks = [[] for i in range(num_pieces)]
list_queues = [multiprocessing.Queue() for i in range(num_pieces)]
list_names = [['task_'+str(i)] for i in range(num_pieces)]


index_range = np.array([[(num_rows*i)//num_pieces,(num_rows*(i+1))//num_pieces] for i in range(num_pieces)],dtype=int)
my_matrix = matrix_test(num_rows)
my_matrix.split_data_into_queues(index_range,list_queues)

for i in range(num_pieces):
    list_tasks[i] = multiprocessing.Process(name=list_names[i],target=task_update_matrix,args = (my_matrix,list_queues[i]))
pass
for i in range(num_pieces):
    list_tasks[i].start()
    print('start task:{}'.format(i))
    sys.stdout.flush()
pass
my_matrix.assemble_data_from_queues(index_range,list_queues)
for i in range(num_pieces):
    list_tasks[i].join()
    print('join task:{}'.format(i))
    sys.stdout.flush()
pass


figure = plt.figure()
axes = figure.add_subplot(1,1,1)
axes.plot(my_matrix.data)

#time.sleep(10) # To simulate the calculation time
plt.savefig(dir_work+'/demo_fig.jpg')

print('success')
sys.stdout.flush()


















