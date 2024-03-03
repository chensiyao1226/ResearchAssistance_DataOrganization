import numpy as np
import os
import pandas as pd
import csv
import openpyxl as xl
from csv import DictWriter

path_root = "E:\\4 Tamura\M1\\1.Experiment\\211022\ウニ2"
'''input('input folder root: (Ex:E:\\4 Tamura\M1\\1.Experiment\\211022\ウニ1)')'''

content_list=[]

#===========savename==========

'''
sym_num = 0
for i,j in enumerate(path_root):
    if j=="\\":
        sym_num += 1

sym_which = 0
save_name_flag = False
cow_name_flag = False
save_name = ''
cow_name = ''
'''



table=[]

counter=False
for subdir, dirs, files in os.walk(path_root):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".dat"):
            print (filepath)

            if(counter):
                data=pd.read_csv(filepath, skiprows=6, header=None, delimiter='\t')
                #print(data[1])
                list = data[1].to_numpy()
                table.append(list)
            else:
                data = pd.read_csv(filepath, skiprows=6, header=None, delimiter='\t')
                # print(data[1])
                list0 = data[0].to_numpy()
                list1 = data[1].to_numpy()
                table.append(list0)
                table.append(list1)


            counter = True

print(table)
print("start saving")

#np.savetxt(exc_save_magn, table)


#=====save======
exc_save_magn = path_root + '\\' + "save.csv"
with open(exc_save_magn, 'w', newline='\n') as f:

    writer = csv.writer(f)
    print("saving")
    table = np.array(table)
    table_t = table.T
    for i in range(len(table_t)):
        writer.writerow(table_t[i])


print("save")





'''
for line in infile.read().splitlines():
    print(line)

df = pd.read_table(filepath, sep="s+")
dat = np.loadtxt(filepath, unpack = True)
print(df)


with open(filepath) as infile, open("outfile.csv", "w") as outfile:
    csv_writer = csv.writer(outfile)
    prev = ''
    csv_writer.writerow(['ID', 'PARENT_ID'])
    for line in infile.read().splitlines():
        csv_writer.writerow([line, prev])
        prev = line
'''



'''
#============collect data=================
for root, dirs, files in os.walk(path_root):
    for d in dirs:
        print(d)
        path_list = os.path.join(root, d)
        flag = 0
        for filename in os.listdir(path_list):
            if (find_name == filename):
                file_path = path_list + '\\' + filename

                with open(file_path, "rt") as csvfile:
                    reader = csv.reader(csvfile)
                    for i, rows in enumerate(reader):
                        if i == 1:
                            content = rows

                content.append(cow_name)
                print(content)
                content_list.append(content)

                flag = 1
                counter+=1
                break
        if(flag==0):
            warning_message = 'no flowdata.csv in ' + path_list
            print(warning_message)


#=========save==============
try:
    exc_save_magn = path_root + '\\' + save_name_modi

    book = xl.Workbook()
    sheet = book.active
    for i in range (counter):
        sheet.append(content_list[i])
    book.save(exc_save_magn)
    print("Saved")

except:
    print("Falied!!!")

con = input('>>')

'''




