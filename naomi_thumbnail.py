from xml.dom.minidom import parse
import os
import shutil
import easygui
import json

picpath = easygui.diropenbox(
    "Playlist output dir", "Choose the lpl output dir,选择游戏列表文件输出目录")
gamelistfile = easygui.fileopenbox(
    "Choose gamelist.xml file", "Choose gamelist.xml file,选择游戏列表文件xml文件")

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
    gamefile=gamename+'.png'
    pngfile=os.path.splitext(romfile)[0]+'.png'
    ori_path=os.path.join(picpath,pngfile)
    dest_path=os.path.join(picpath,gamefile)
    shutil.move(ori_path,dest_path)
    



