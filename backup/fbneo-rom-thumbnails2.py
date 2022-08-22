from xml.dom.minidom import parse
import os
import shutil

thumbpath = r"F:\retro\thumbnails\FBA\Named_Snaps_PFBA"


dom = parse('gamelist.xml')
data = dom.documentElement
roms = data.getElementsByTagName('game')
for rom in roms:
    romfile = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    realgamename = rom.getElementsByTagName('name')[0].childNodes[0].nodeValue
    gamename = os.path.splitext(romfile)[0]
    filebasename = os.path.splitext(romfile)[0]
    for i in ["<", ">", ":", '"', "'", "/", "'", "\\", "|", "?", "*", "*"]:
        gamename = gamename.replace(i, '_')
        realgamename = realgamename.replace(i, '_')
    try:
        shutil.move(os.path.join(thumbpath, realgamename+".png"),
                    os.path.join(os.path.join(thumbpath,"short"), gamename+".png"))
    except FileNotFoundError:
        print(os.path.join(thumbpath, realgamename+".png"))
