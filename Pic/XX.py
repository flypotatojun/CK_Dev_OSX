
# encoding:utf-8

import os
fileFormat = ['.tif', '.tiff']
path = '/Users/CK/PycharmProjects/CK_Dev_OSX/Pic/'
filelists = os.listdir(path)
sort_num_first = []
name = (i for i in filelists for item in fileFormat if
                           os.path.splitext(i)[1] == item)
print(name)
for file in name:
    # sort_num_first.append(int(file.split("_")[2])
    sort_num_first.append(file)
    sort_num_first.sort()
print(sort_num_first)
sorted_file = []
for sort_num in sort_num_first:
    for file in name:
        if str(sort_num) == file.split("_")[2]:
            sorted_file .append(file)