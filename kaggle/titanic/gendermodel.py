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
# '1' '0' '3' 'Braund, Mr. Owen Harris' 'male' '22' '1' '0' 'A/5 21171' '7.25' '' 'S'
print data[0]

# The size() function counts how many elements are in
# in the array and sum() (as you would expects) sums up
# the elements in the array.

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"

# Using the index from above we select the females and males separately
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

# Then we finds the proportions of them that survived
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

# and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

# Read test data and write results.
test_file = open('training/test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

prediction_file = open("submission/genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female':
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
