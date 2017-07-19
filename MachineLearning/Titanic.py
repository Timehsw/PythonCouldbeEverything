import csv as csv
import numpy as np

csv_file_object=csv.reader(open('./data/csv/train.csv','rb'))
header=csv_file_object.next()

data=[]
for row in csv_file_object:
    data.append(row)

data=np.array(data)

print data[0]
print data[-1]
print data[0,3]
print data[0][3]
print data[0::,4]