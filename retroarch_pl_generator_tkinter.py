import os
import json
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


def get():
    choice = check1.get()
    romspathdir = entry_rom_path.get()
    lplpathdir = entry_dest_playlist.get()
    prefix = entry_prefix.get()
    fix_db_name = entry_db_name.get()

    param_flag = 1
    if not romspathdir:
        param_flag = 0
        messagebox.showinfo('提示', '请输入正确ROM路径,Please choose the rom path !')
    if not lplpathdir:
        param_flag = 0
        messagebox.showinfo(
            '提示', '请输入正确的Playlist文件输出路径,Please choose the lpl output path !')

    if param_flag:
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
                    if choice == 1:
                        rom_path = rom_path.replace("/", "\\")
                    else:
                        rom_path = rom_path.replace("\\", "/")
                        rom_path = rom_path.replace("//", "/")
                    if fix_db_name:
                        db_name = fix_db_name
                    else:
                        db_name = os.path.basename(root) + '.lpl'
                    label = os.path.splitext(file)[0]
                    list1.append({"path": rom_path,
                                  "label": label, "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": db_name})
                dict1 = {"items": list1}
                content = json.dumps(dict1, indent=4, ensure_ascii=False)
                playlist = os.path.join(
                    lplpathdir, os.path.basename(root))+".lpl"
                with open(playlist, "w", encoding='utf8') as f:
                    f.write(content)
        messagebox.showinfo('提示', '任务执行已结束,Task Completed')
        os.startfile(lplpathdir)


#################GUI####################


def selectpath(path):
    path_ = askdirectory()
    path.set(path_)


window = tk.Tk()
window.title("Retroarch Playlist generator 列表生成工具")

path1 = tk.StringVar()
path2 = tk.StringVar()


check1 = tk.BooleanVar()
check1.set(1)

frame1 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame2 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame3 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame4 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame5 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame6 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)

OS_type1 = tk.Radiobutton(frame1, text="游戏环境Windows系统", variable=check1,
                          value=1, justify='left')
OS_type2 = tk.Radiobutton(frame1, text="游戏环境非(Not) Windows，比如Linux，Android系统", variable=check1,
                          value=0, justify='left')


entry_rom_path = tk.Entry(frame2, textvariable=path1,
                          state=tk.DISABLED, width=60)
button_rom_path = tk.Button(
    frame2, text="ROM path 所在文件夹选择", command=lambda: selectpath(path1))


entry_dest_playlist = tk.Entry(frame3, textvariable=path2,
                               state=tk.DISABLED, width=60)
button_dest_playlist = tk.Button(frame3, text="Playlist output path 输出文件夹选择", command=lambda: selectpath(
    path2))

entry_prefix_label = tk.Label(
    frame4, text="Rom path prefix 路径前缀,比如为其他平台制作列表的场景(可选,Optional)")
entry_prefix = tk.Entry(frame4, width=60)

entry_db_name_label = tk.Label(
    frame5, text="固定所有列表文件的db_name值,比如FBA.lpl？默认为rom所在文件夹名称(可选,Optional)")
entry_db_name = tk.Entry(frame5, width=60)


button_confirm = tk.Button(frame6, text="确定 Go", command=lambda: get())

# label_ori_dir.pack()
entry_rom_path.pack()
button_rom_path.pack()


# label_dest_dir.pack()
entry_dest_playlist.pack()
button_dest_playlist.pack()

OS_type1.pack(anchor='w')
OS_type2.pack(anchor='w')

entry_prefix_label.pack()
entry_prefix.pack()
button_confirm.pack()

entry_db_name_label.pack()
entry_db_name.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
frame3.pack(padx=10, pady=10)
frame4.pack(padx=10, pady=10)
frame5.pack(padx=10, pady=10)
frame6.pack(padx=10, pady=10)
window.mainloop()
