from xml.dom.minidom import parse
import os
import shutil
import csv

thumbpath_ori = r"F:\retro\FBA-1.0.3\FBNeo 1.0.3-zip\thumbnails\FBNeo - Arcade Games\Named_Titles"
thumbpath_dest = r"F:\retro\FBA-1.0.3\FBNeo 1.0.3-zip\thumbnails\FBNeo - Arcade Games\Named_Titles_cn"

with open(".\\database\\gamelist_merge.csv", mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    gamedict = {}
    for row in reader:
        gamedict[row['file']] = row['name']

dom = parse('.\\database\\gamelist.xml')
data = dom.documentElement
roms = data.getElementsByTagName('game')
for rom in roms:
    romfile = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    realgamename = rom.getElementsByTagName('name')[0].childNodes[0].nodeValue
    gamename = os.path.splitext(romfile)[0]
    filebasename = os.path.splitext(romfile)[0]
    if filebasename in gamedict.keys():
        label = gamedict[filebasename]
    else:
        label = realgamename
    for i in ["<", ">", ":", '"', "/", "\\", "|", "?", "*","`"]:
        #gamename = gamename.replace(i, '_')
        realgamename = realgamename.replace(i, '_')

    for i in ["<", ">", ":", '"', "/", "\\", "|", "?", "*","`","&"]:
        #gamename = gamename.replace(i, '_')
        label = label.replace(i, '_')
    try:
        shutil.copy(os.path.join(thumbpath_ori, realgamename+".png"),
                    os.path.join(thumbpath_dest, label+".png"))
    except FileNotFoundError:
        print(os.path.join(thumbpath_ori, realgamename+".png"))
        #print(os.path.join(thumbpath_ori, filebasename+".png"))
