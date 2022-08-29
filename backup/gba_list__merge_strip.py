import csv

###生成GBA_list 完整的对照列表文件，临时文件，最终版本已修改为 gba_list_merge.csv
with open('database\\gba_list_merge.csv','r',encoding='utf-8') as file:
    csvreader=csv.reader(file)
    for line in csvreader:
        with open('database\\gba_list_merge2.csv','a',encoding='utf-8',newline='') as newfile:
            csvwriter=csv.writer(newfile)
            linenew=[*map(lambda x:x.strip(), line)]
            csvwriter.writerow(linenew)
        

        
        

