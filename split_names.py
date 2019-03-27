# encoding=utf8
import csv
from datetime import datetime as dt
import hashlib
donedict = {}

with open('input3.csv',newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for key,row in enumerate(reader):
        name_string = " "
        perc = key/3100
        print(key,":    Done: ",perc, " %")
        epitheto = row[0]
        name = row[1]
        birthday = row[3]
        gender = row[5]
        print("Working with: ", epitheto, " birthday: ", birthday)
        if((name == name_string) or (name == "")):
            epitheto_to_list = epitheto.split(" ")
            if "ΑΡΡΕΝ" in epitheto_to_list:
                gender = 'M'
                epitheto_to_list.remove("ΑΡΡΕΝ")
            if "ΘΗΛΥ" in epitheto_to_list:
                gender = 'F'
                epitheto_to_list.remove("ΘΗΛΥ")
            epitheto = epitheto_to_list[0]
            epitheto_to_list.remove(epitheto_to_list[0])
            name = name_string.join(epitheto_to_list)
            donedict.update({key:row})
        else:
            name_to_list = name.split(" ")
            if "ΑΡΡΕΝ" in name_to_list:
                gender = 'M'
                name_to_list.remove("ΑΡΡΕΝ")
            if "ΘΗΛΥ" in name_to_list:
                gender = 'F'
                name_to_list.remove("ΘΗΛΥ")
            name = name_string.join(name_to_list)
            donedict.update({key:row})
        donedict[key][0] = epitheto
        donedict[key][1] = name
        donedict[key][5] = gender

with open('outputzzz.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    for (key, value) in donedict.items():
        writer.writerow(value)
