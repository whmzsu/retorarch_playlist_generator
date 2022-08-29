import os
import csv

files=os.listdir(r'F:\roms\GBA官方原版-2819\all')


with open('database\\gba_list.csv','r',encoding='utf-8') as file:
    csvreader=csv.reader(file)
    i=0
    for line in csvreader:
        line.insert(1,files[i])
        i=i+1
        print(line)
        with open('database\\gba_list_merge2.csv','a',encoding='utf-8',newline='') as newfile:
            csvwriter=csv.writer(newfile)
            csvwriter.writerow(line)
        

        
        

