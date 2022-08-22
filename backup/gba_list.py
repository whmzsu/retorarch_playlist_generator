import re
import csv
with open("list.txt","r",encoding='utf8') as f:
    line=f.readlines()
    for i in line:
        i=i.replace("\n","")
        i=re.split("\(|\)",i)
        i.insert(0,i[0][:4])
        i[1]=i[1][7:]
        print(i)
        with open('list.csv','a',newline="",encoding='utf8') as wcsv:
            file=csv.writer(wcsv)
            file.writerow(i)
            

        