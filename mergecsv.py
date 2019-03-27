# encoding=utf8
import csv
from datetime import datetime as dt
import hashlib
donedict = {}
k = 0
with open('input2.csv',newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        perc = k/390
        print(k,":    Done: ",perc, " %")
        epitheto = row[0]
        name = row[1]
        birthday = row[3]
        gender = row[5]
        print("Working with: ", epitheto, " birthday: ", birthday)
        tobehashed = epitheto.join(birthday).encode()
        hash_object = hashlib.md5(tobehashed)
        if (hash_object.hexdigest() in donedict):
            for i in range(0,len(row)-1):
                if(donedict[hash_object.hexdigest()][i] == '' and row[i] != ''): #if we have an empty cell
                        donedict[hash_object.hexdigest()][i] = row[i]
                elif (donedict[hash_object.hexdigest()][i] != '' and row[i] != ''):
                    a = dt.strptime(donedict[hash_object.hexdigest()][4],"%m/%d/%Y")
                    b = dt.strptime(row[4],"%m/%d/%Y")
                    if(b<a):
                        donedict[hash_object.hexdigest()][i] = row[i]
        else:
            donedict.update({hash_object.hexdigest():row})
        k +=1
    with open('output.csv','w',newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        for (key, value) in donedict.items() :
            writer.writerow(value)
