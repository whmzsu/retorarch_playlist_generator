import csv 
import os
import shutil
path=r'F:\retro\GBA-bak\未分类-英文名称'
with open('database\\gba_list_merge.csv','r',encoding='utf-8',newline='') as newfile:
    csvreader=csv.reader(newfile)
    for line in csvreader:
        try: 
            os.mkdir(os.path.join(path,line[6].strip()))
        except OSError:
            pass
        try:
            #shutil.copy(os.path.join(path,line[1]),os.path.join(path,line[6].strip(),line[1][0:4]+'-'+line[4]+'-'+line[2]+'-'+line[5]+'.zip'))
            shutil.move(os.path.join(path,line[1]),os.path.join(path,line[6].strip(),line[4]+'-'+line[2]+'-'+line[5]+'.zip'))
        except OSError as e:
            print(os.path.join(path,line[1]))
            print(e)
