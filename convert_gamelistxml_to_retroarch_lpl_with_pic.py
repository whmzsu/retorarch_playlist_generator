# convert emulationstation gamelist.xml and pic to retroarch
from xml.dom.minidom import parse
import os
import shutil
import easygui
import json

gamelistfile = easygui.fileopenbox(
    "Choose gamelist.xml file", "Choose gamelist.xml file,选择游戏列表文件gamelist.xml文件")

lplpathdir = easygui.diropenbox(
    "Playlist output dir", "Choose the lpl output dir,选择游戏列表文件输出目录")

prefix = easygui.enterbox(
    "Input the rom prefix,Only for other platform like android,(optional)，default is the dir of gamelist.xml,\r\n 输入路径前缀替换,填入此前缀路径,默认同gamelist.xml所在路径")

db_name = easygui.enterbox(
    "Input the rom db_name,\r\n 输入db_name,关联图片,默认gamelist.xml所在路径的最后一个文件夹")

choice = easygui.choicebox("请选择你的游戏平台", "选择你的游戏平台", [
                           "Windows", "非Windows,Not Windows，比如Linux，Android，Switch等等"])

picpath = easygui.diropenbox(
    "Pic  png file input dir", "Choose pic or media or image  dir,选择游戏图片所在文件目录,必选")
    
if not db_name:
    db_path=os.path.dirname(gamelistfile)
    db_name=os.path.basename(db_path)

dom = parse(gamelistfile)
data = dom.documentElement
roms = data.getElementsByTagName('game')
gamedict = {}
list1=[]
for rom in roms:
    rompath = rom.getElementsByTagName('path')[0].childNodes[0].nodeValue
    romfile=os.path.basename(rompath)
    gamename = rom.getElementsByTagName(
        'name')[0].childNodes[0].nodeValue
    try:    
        image_full = rom.getElementsByTagName(
        'image')[0].childNodes[0].nodeValue
    except IndexError:
        image_full=os.path.splitext(romfile)[0]+'.png'
    image_file=os.path.basename(image_full)
    for i in ["<", ">", ":", '"', "'", "/", "\\", "|", "?", "*", "&"]:
        gamename = gamename.replace(i, '_')
    if prefix:
        rom_path = os.path.join(prefix, romfile)
    else:
        rom_path = os.path.join(os.path.dirname(gamelistfile), romfile)
    if choice == "Windows":
       rom_path = rom_path.replace("/", "\\")
    else:
       rom_path = rom_path.replace("\\", "/")
       rom_path = rom_path.replace("//", "/")
    list1.append({"path": rom_path,"label": gamename, "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": db_name})
    
    gamefile=gamename+'.png'
    #pngfile=os.path.splitext(romfile)[0]+'.png'
    #ori_file=os.path.join(picpath,pngfile)

    ori_file=os.path.join(picpath,image_file)

    dest_path=os.path.join(picpath,db_name,'Named_Snaps')
    dest_file=os.path.join(dest_path,gamefile)
    
    try:
        os.makedirs(dest_path)
    except Exception as e:
        pass
    
    try:
        shutil.copy(ori_file,dest_file)
    except FileNotFoundError as e:
        print(ori_file)

dict1 = {"items": list1}
content = json.dumps(dict1, indent=4, ensure_ascii=False)
playlist = os.path.join(lplpathdir, db_name+".lpl")
with open(playlist, "w", encoding='utf8') as f:
            f.write(content)
print("Playlist file done !")

