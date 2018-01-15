#!/usr/bin/python

import os
import sys

filename = sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))

# Reading the input file
count = 1
data_dict = {}
file_sp = open(filename,'r')
for line in file_sp.readlines():
    l = line.split(' ') 
    l[-1] = l[-1].replace('\n','')
    l = [int(x) for x in l]
    data_dict[count] = l
    count += 1
file_sp.close()

# Removing the duplicates and sorting values
for k in data_dict:
    data_dict[k] = list(set(data_dict[k]))
    data_dict[k].sort()

# Getting the max number to define number of attributes in the file
num_max = []
for k in data_dict:
    num_max.append(max(data_dict[k]))
att_num = max(num_max)

# Writing attributes to the output file
file_n = filename.split('.')[0]
d_type = '{0,1}'
file_output = open(path + '/' + str(file_n) + '.arff','a')
file_output.writelines('@relation ' + str(file_n) + '\n')
for i in range(att_num+1):
    file_output.writelines('@attribute i' + str(i) + ' ' + str(d_type) + '\n')
file_output.writelines('@data' + '\n')
file_output.close()

# Writing data to the output file
file_output = open(path + '/' + str(file_n) + '.arff','a')
for k in data_dict:
    file_output.writelines('{')
    for element in data_dict[k]:
        if(element != data_dict[k][-1]):
            file_output.writelines(str(element) + ' ' + str(1) + ',')
        else:
            file_output.writelines(str(element) + ' ' + str(1))
    file_output.writelines('}' + '\n')
file_output.close()

