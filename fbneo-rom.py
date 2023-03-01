from xml.dom.minidom import parse
import os
import shutil
pathbase = r"F:\retro\FBA"
dom = parse('.\database\gamelist.xml')
data = dom.documentElement
roms = data.getElementsByTagName('game')
for rom in roms:
    romfile = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    try:
        romcatalog = rom.getElementsByTagName(
            'system')[0].childNodes[0].nodeValue
    except IndexError:
        romcatalog = 'UNKNOW'
    if romcatalog == 'Eighting / Raizing':
        romcatalog = 'Eighting Raizing'
    if os.path.exists(os.path.join(pathbase, romcatalog)) == False:
        os.mkdir(os.path.join(pathbase, romcatalog))
    try:
        shutil.move(os.path.join(pathbase, romfile),
                    os.path.join(pathbase, romcatalog, romfile))
    except FileNotFoundError:
        print(os.path.join(pathbase, romfile))
