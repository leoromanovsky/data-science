# The first thing to do is to import the relevant packages
# that I will need for my script,
# these include the Numpy (for maths and arrays)
# and csv for reading and writing csv files
# If i want to use something from this I need to call
# csv.[function] or np.[function] first

import csv as csv
import numpy as np

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('training/train.csv', 'rb'))
header = csv_file_object.next()

data=[]
for row in csv_file_object:
    data.append(row)
data = np.array(data)

print data
