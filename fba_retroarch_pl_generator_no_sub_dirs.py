import os
import json
import easygui
import csv
from xml.dom.minidom import parse
# 根据文件名-生成playlist-同时参考2个文件，来正确生成英文名称或者中文名称，中文名称优先

romspathdir = easygui.diropenbox(
    "Roms dir ", "Choose the rom file location，选择ROM所在目录")

lplpathdir = easygui.diropenbox(
    "Playlist output dir", "Choose the lpl output dir,选择游戏列表文件输出目录")

prefix = easygui.enterbox(
    "Input the rom prefix,Only for other platform like android,(optional),\r\n 输入路径前缀替换(可选),给其他平台如Android等准备Playlist时需要填入此前缀路径")

fixdbname = easygui.enterbox(
    "Input the dbname if want it fixed ,for example FBA.lpl (optional,default is the roms located dir name),\r\n 输入dbname(可选),固定playlist dbname 名称，比如 FBA.lpl,默认为ROM所在文件夹名称")

choice = easygui.choicebox("请选择你的游戏平台", "选择你的游戏平台", [
                           "Windows", "非Windows,Not Windows，比如Linux，Android，Switch等等"])

with open(r"\database\gamelist_merge.csv", mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    gamedict = {}
    for row in reader:
        gamedict[row['file']] = row['name']


dom = parse(r'\database\gamelist.xml')
data = dom.documentElement
roms = data.getElementsByTagName('game')
gamedict2 = {}
for rom in roms:
    romfile = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    gamename = rom.getElementsByTagName(
        'name')[0].childNodes[0].nodeValue
    romfilename = os.path.splitext(romfile)[0]
    gamedict2[romfilename] = gamename


for root, dirs, files in os.walk(romspathdir):
    if files:
        list1 = []
        dict1 = {}
        for file in files:
            if prefix:
                prefix_real = root.replace(romspathdir, prefix)
                rom_path = os.path.join(prefix_real, file)
            else:
                rom_path = os.path.join(root, file)
            if choice == "Windows":
                rom_path = rom_path.replace("/", "\\")
            else:
                rom_path = rom_path.replace("\\", "/")
                rom_path = rom_path.replace("//", "/")
            rom_path=os.path.join(romspathdir, file)   #####no_sub_dirs
            db_name = os.path.basename(root) + '.lpl'
            if fixdbname:
                db_name = fixdbname
            filebasename = os.path.splitext(file)[0]
            if filebasename in gamedict.keys():
                label = gamedict[filebasename]
            elif filebasename in gamedict2.keys():
                label = gamedict2[filebasename]
            else:
                label = filebasename
            for i in ["<", ">", ":", '"', "/", "\\", "|", "?", "*","`"]:
                label = label.replace(i, '_')
            list1.append({"path": rom_path,
                          "label": label, "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": db_name})
        dict1 = {"items": list1}
        content = json.dumps(dict1, indent=4, ensure_ascii=False)
        playlist = os.path.join(lplpathdir, os.path.basename(root))+".lpl"
        with open(playlist, "w", encoding='utf8') as f:
            f.write(content)
