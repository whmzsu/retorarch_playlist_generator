from xml.dom.minidom import parse
import os
import shutil
import csv

thumbpath = r"F:\retro\pfba-fbneo-media\mixrbv2-cn"

with open("mame-list-cn.csv", mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    gamedict = {}
    for row in reader:
        gamedict[row['file']] = row['name']

dom = parse('gamelist.xml')
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
    for i in ["<", ">", ":", '"', "'", "/", "'", "\\", "|", "?", "*", "*"]:
        gamename = gamename.replace(i, '_')
        label = label.replace(i, '_')
    try:
        shutil.move(os.path.join(thumbpath, gamename+".png"),
                    os.path.join(thumbpath, label+".png"))
    except FileNotFoundError:
        print(os.path.join(thumbpath, filebasename+".png"))
