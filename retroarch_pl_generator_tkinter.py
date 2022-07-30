import os
import json
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


def get():
    romspathdir = entry_rom_path.get()
    iplpathdir = entry_dest_playlist.get()
    prefix = entry_prefix.get()
    choice = check1.get()

    param_flag = 1
    if not romspathdir:
        param_flag = 0
        messagebox.showinfo('提示', '请输入正确ROM路径,Please choose the rom path !')
    if not iplpathdir:
        param_flag = 0
        messagebox.showinfo(
            '提示', '请输入正确的Playlist文件输出路径,Please choose the ipl output path !')

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
                    db_name = os.path.basename(root) + '.ipl'
                    label = os.path.splitext(file)[0]
                    list1.append({"path": rom_path,
                                  "label": label, "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": db_name})
                dict1 = {"items": list1}
                content = json.dumps(dict1, indent=4, ensure_ascii=False)
                playlist = os.path.join(
                    iplpathdir, os.path.basename(root))+".ipl"
                with open(playlist, "w") as f:
                    f.write(content)
        messagebox.showinfo('提示', '任务执行已结束,Task Completed')

#################GUI####################


def selectpath(path):
    path_ = askdirectory()
    path.set(path_)


window = tk.Tk()
window.title("Retroarch Playlist generator 列表生成工具")

path1 = tk.StringVar()
path2 = tk.StringVar()
path3 = tk.StringVar()


check1 = tk.BooleanVar()
check1.set(1)

frame1 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame2 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame3 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame4 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)
frame5 = tk.Frame(window, highlightbackground="blue", highlightthickness=1)

OS_type1 = tk.Radiobutton(frame1, text="Windows", variable=check1,
                          value=1, justify='left')
OS_type2 = tk.Radiobutton(frame1, text="非(Not) Windows", variable=check1,
                          value=0, justify='left')


entry_rom_path = tk.Entry(frame2, textvariable=path1,
                          state=tk.DISABLED, width=60)
button_rom_path = tk.Button(
    frame2, text="ROM path 所在文件夹选择", command=lambda: selectpath(path1))


entry_dest_playlist = tk.Entry(frame3, textvariable=path2,
                               state=tk.DISABLED, width=60)
button_dest_playlist = tk.Button(frame3, text="Playlist output path 输出文件夹选择", command=lambda: selectpath(
    path2))

entry_label = tk.Label(frame4, text="Rom path prefix 路径前缀(可选Optional)")
entry_prefix = tk.Entry(frame4, textvariable=path3, width=60)
button_confirm = tk.Button(frame5, text="确定 Go", command=lambda: get())

# label_ori_dir.pack()
entry_rom_path.pack()
button_rom_path.pack()


# label_dest_dir.pack()
entry_dest_playlist.pack()
button_dest_playlist.pack()

OS_type1.pack(anchor='w')
OS_type2.pack(anchor='w')

entry_label.pack()
entry_prefix.pack()
button_confirm.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
frame3.pack(padx=10, pady=10)
frame4.pack(padx=10, pady=10)
frame5.pack(padx=10, pady=10)

window.mainloop()
