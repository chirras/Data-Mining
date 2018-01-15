#!/usr/bin/python
import os
import sys

filename = sys.argv[1]
l_lim = int(sys.argv[2])
u_lim = int(sys.argv[3])
pre = int(sys.argv[4])

f_name = (filename.split('.')[0]).split('_')[0]
# Getting the directory of the python file
path = os.path.dirname(os.path.abspath(__file__))
# Reading the Input file and creating the output file 
input_file = open(filename, 'r')
output_file = open(path + '/' + f_name + '_out_' + str(l_lim) + '_' + str(u_lim) + '_' + str(pre) + '.txt' , 'w')
# Reading the data from file and scaling the columns
line = input_file.readlines()
l = str(line).strip().split(',')
ncol = len(l)
data = []
for i in range(ncol):
    col = []
    col_norm = []
    with open(filename,'r') as file:
        for line in file:
            l = line.strip().split(' ')
            col.append(float(l[i]))
        ma = max(col)
        mi = min(col)
        for element in col:
            element = (u_lim-l_lim) * (element-mi)/(ma-mi) + l_lim
            p = ('%.' + str(pre) +'f')
            col_norm.append(p % element)
        data.append(col_norm)
# Writing the scaled data to file
nrow = len(data[0])
for i in range(nrow):
    for j in range(len(data)):
        if(j < (nrow-1)):
            output_file.writelines(str(data[j][i]) + ' ')
        else:
            output_file.writelines(data[j][i])
    output_file.writelines('\n')
output_file.close()   