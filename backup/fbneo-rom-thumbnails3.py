from xml.dom.minidom import parse
import os
import shutil
import csv

#根据中英文对照文件，生成完整的thumbnail

thumbpath_ori = r"F:\retro\FBA-1.0.3\thumbnails\FBA_ori\Named_Titles"
thumbpath_dest = r"F:\retro\FBA-1.0.3\thumbnails\FBA_ori\Named_Titles_cn"

with open(".\\database\\gamelist_catalog_full.csv", mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    gamedict = {}
    for row in reader:
        gamedict[row['file']] = row['name']

for file  in gamedict.keys():
    label = gamedict[file]
    for i in ["<", ">", ":", '"', "/", "\\", "|", "?", "*","`","&"]:
        label = label.replace(i, '_')
    try:
        shutil.copy(os.path.join(thumbpath_ori, file+".png"),
                    os.path.join(thumbpath_dest, label+".png"))
        #shutil.move(os.path.join(thumbpath_ori, gamename+".png"),os.path.join(thumbpath_dest, label+".png"))
    except FileNotFoundError:
            print(os.path.join(thumbpath_ori, file+".png"))
            #print(os.path.join(thumbpath_ori, filebasename+".png"))
