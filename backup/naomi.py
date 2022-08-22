from xml.dom.minidom import parse
import os
import shutil
import easygui
import json

gamelistfile = easygui.fileopenbox(
    "Choose gamelist.xml file", "Choose gamelist.xml file,选择游戏列表文件xml文件")

lplpathdir = easygui.diropenbox(
    "Playlist output dir", "Choose the lpl output dir,选择游戏列表文件输出目录")

prefix = easygui.enterbox(
    "Input the rom prefix,Only for other platform like android,(optional),\r\n 输入路径前缀替换(可选),给其他平台如Android等准备Playlist时需要填入此前缀路径")

choice = easygui.choicebox("请选择你的游戏平台", "选择你的游戏平台", [
                           "Windows", "非Windows,Not Windows，比如Linux，Android，Switch等等"])

dom = parse(gamelistfile)
data = dom.documentElement
roms = data.getElementsByTagName('game')
gamedict = {}
list1=[]
for rom in roms:
    rompath = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    romfile=os.path.split(rompath)[1]
    gamename = rom.getElementsByTagName(
        'name')[0].childNodes[0].nodeValue
    for i in ["<", ">", ":", '"', "'", "/", "\\", "|", "?", "*", "&"]:
        gamename = gamename.replace(i, '_')
    rom_path = os.path.join(prefix, romfile)
    if choice == "Windows":
       rom_path = rom_path.replace("/", "\\")
    else:
       rom_path = rom_path.replace("\\", "/")
       rom_path = rom_path.replace("//", "/")
    list1.append({"path": rom_path,"label": gamename, "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": "naomi"})
    

dict1 = {"items": list1}
content = json.dumps(dict1, indent=4, ensure_ascii=False)
playlist = os.path.join(lplpathdir, 'naomi'+".lpl")
with open(playlist, "w", encoding='utf8') as f:
            f.write(content)