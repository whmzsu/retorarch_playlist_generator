import os
import json
import easygui


romspathdir = easygui.diropenbox(
    "Roms dir ", "Choose the rom file location，选择ROM所在目录")

iplpathdir = easygui.diropenbox(
    "Playlist output dir", "Choose the ipl output dir,选择游戏列表文件输出目录")

prefix = easygui.enterbox(
    "Input the rom prefix,Only for other platform like android,(optional),\r\n 输入路径前缀替换(可选),给其他平台如Android等准备Playlist时需要填入此前缀路径")

for root, dirs, files in os.walk(romspathdir):
    if files:
        list1 = []
        dict1 = {}
        for file in files:
            if prefix:
                rom_path = os.path.join(prefix, file)
            else:
                rom_path = os.path.join(root, file)
            list1.append({"path": rom_path,
                          "label": os.path.splitext(file)[0], "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": os.path.basename(root)+'.ipl'})
        dict1 = {"items": list1}
        content = json.dumps(dict1, indent=4, ensure_ascii=False)
        with open(os.path.join(iplpathdir, os.path.basename(root))+".ipl", "w") as f:
            f.write(content)
