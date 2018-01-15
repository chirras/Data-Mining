
#!/usr/bin/python

import os
import sys

filename = sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))

# Considering the datatypes be Nominal/Numeric
def datatype(filename):
    d_list = []
    input_file = open(filename, 'r')   
    line = input_file.readline()
    l = str(line).strip().split(',')
    ncol = len(l)
    for i in range(ncol):
        att = []
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                l = line.strip().split(',')
                att.append(l[i]) 
        temp = list(set(att))
        if(len(temp) < len(att)/2):
           d_list.append(temp)
        elif(len(temp) > len(att)/2):
            d_list.append('Numeric')
    return(d_list)


# Reading the input csv file
input_file = open(filename , 'r')                                             
# Creating an outpu arff file
file_n = filename.split('.')[0]
output_file = open(path + '/' + str(file_n) + '.arff', 'w')
    
dt_count = 0
d_type = []
temp = datatype(filename)
for element in temp:
    if(isinstance(element, list)):
        element = list(filter(None, element))
    d_type.append(element)
    
# Header of arff file
output_file.writelines('@relation ' + str(file_n) + '\n')
count = 0
for line in input_file:
    count += 1
    l = line.strip()
    if(count == 1):
        for word in str(l).split(','):
            output_file.writelines('@attribute ' + str(word).strip() + ' ' + str(d_type[dt_count]).replace('[','{').replace(']','}').replace("'","").replace(' ','') + '\n') 
            dt_count += 1
        output_file.writelines('@data ' + '\n')
    # Writing the data to file
    if(count > 1):
        output_file.writelines(l + '\n')
output_file.close()