from xml.dom.minidom import parse
import os
import shutil
import csv

pathbase = r"F:\retro\FBA"
thumbpath = r"F:\retro\thumbnails\FBA\Named_Snaps"

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
    gamename = rom.getElementsByTagName(
        'name')[0].childNodes[0].nodeValue
    filebasename = os.path.splitext(romfile)[0]
    if filebasename in gamedict.keys():
        label = gamedict[filebasename]
        for i in ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]:
            gamename = gamename.replace(i, '-')
            label = label.replace(i, '-')
        try:
            shutil.move(os.path.join(thumbpath, gamename+".png"),
                        os.path.join(thumbpath, label+".png"))
        except FileNotFoundError:
            print(os.path.join(thumbpath, filebasename+".png"))
