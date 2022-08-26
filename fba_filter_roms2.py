import os
import csv
from xml.dom.minidom import parse
# 根据文件名-生成playlist-同时参考2个文件，来正确生成英文名称或者中文名称，中文名称优先

romspathdir = r"D:\trans\0816\arcade"

##############Chinese game name from csv##########################
with open(r"database\gamelist_merge.csv", mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    gamedict = {}
    for row in reader:
        gamedict[row['file']] = row['name']
#############English game name and description from xml####################
dom = parse(r'database\gamelist.xml')
data = dom.documentElement
roms = data.getElementsByTagName('game')
gamedict2 = {}
for rom in roms:
    romfile = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    gamename = rom.getElementsByTagName(
        'name')[0].childNodes[0].nodeValue
    try:
        gamedesc=rom.getElementsByTagName('desc')[0].childNodes[0].nodeValue
    except IndexError:
        gamedesc=''
    romfilename = os.path.splitext(romfile)[0]

    gamedict2[romfilename] = gamename
    gamedict2[romfilename+'_desc']=gamedesc
    
csvfile=r'database\gamelist_catalog2.csv'
for root, dirs, files in os.walk(romspathdir):
    if files:
        list1 = []
        dict1 = {}
        for file in files:
            filebasename = os.path.splitext(file)[0]
            try:
                desc=gamedict2[filebasename+'_desc']
            except KeyError:
                desc=''
            if filebasename in gamedict.keys():
                label = gamedict[filebasename]
                gamename=[filebasename,"Chinese Name",label,desc]
            elif filebasename in gamedict2.keys():
                label = gamedict2[filebasename]
                gamename=[filebasename,"Long Name",label,desc]
            else:
                label = filebasename
                gamename=[filebasename,"Short Name",label,desc]
            with open(csvfile,'a',encoding='utf8',newline='') as f:
                csvwriter=csv.writer(f)
                csvwriter.writerow(gamename)

