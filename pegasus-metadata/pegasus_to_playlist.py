import os
import configparser
import json
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename


class Game():
    def __init__(self, name, file, sortby, developer, publisher, genre,release,players,rating,description,assetsboxfront,assetsvideo,assetslogo,assetsscreenshot,assetsbackground):
        self.name = name
        self.file = file
        self.sortby = sortby
        self.developer = developer
        self.publisher = publisher
        self.genre = genre
        self.release=release
        self.players=players
        self.rating=rating
        self.description=description
        self.boxfront=assetsboxfront
        self.video=assetsvideo
        self.logo=assetslogo
        self.screenshot=assetsscreenshot
        self.background=assetsbackground

        for i in ["<", ">", ":", '"', "/", "\\", "|", "?", "*","`"]:
            self.name = self.name.replace(i, '_')

def write_playlist(gamelists,lplpathdir,rom_path):
    gamedict = {}
    gamedict["version"]= "1.4"
    gamedict["label_display_mode"]=  0
    gamedict["right_thumbnail_mode"]=  0
    gamedict["left_thumbnail_mode"]=  0
    gamedict["sort_mode"]=  0
      
    gamedict["items"] = gamelists
    content = json.dumps(gamedict, indent=4, ensure_ascii=False)
    playlist = os.path.join(lplpathdir, os.path.basename(rom_path))+".lpl"
    with open(playlist, "w", encoding='utf8') as f:
            f.write(content)
    
def prepare_sections(metadatafile):
    sections=[]
    section=[]
    with open(metadatafile,encoding='utf-8') as metadata_file:
        file_content=metadata_file.readlines()
        for line in file_content:
            if line.strip():
                section.append(line)
            else:
                if section:
                    sections.append(section)
                section=[]
        sections.append(section)
    return sections

def process_pic(game,rom_path,db_name):
    if game.screenshot:
        ss_full_file = game.screenshot.replace('./', rom_path+'/')
        ss_ext=os.path.splitext(ss_full_file)[1]
        db_path=os.path.splitext(db_name)[0]
        pic_dest_dir=os.path.join(rom_path,db_path,'Named_Snaps')
        ss_dest_file=os.path.join(pic_dest_dir,game.name+'.'+ss_ext)

        os.makedirs(pic_dest_dir,exist_ok=True)
        try:
            shutil.copyfile(ss_full_file, ss_dest_file)
        except Exception as e:
            print(e) 

def prepare_gamelists(sections,prefix,choice,rom_path,fix_db_name):
    gamelist = []
    for gamedes in sections:
        fulltext=''.join(gamedes)
        fulltext='[default]\r\n'+fulltext
        config = configparser.ConfigParser(interpolation=None)
        config.read_string(fulltext)

        name=config.get('default','game',fallback='')
        file=config.get('default','file',fallback='')
        sortby=config.get('default','sort-by',fallback='')
        developer=config.get('default','developer',fallback='')
        publisher=config.get('default','publisher',fallback='')
        genre=config.get('default','genre',fallback='')
        release=config.get('default','release',fallback='')
        players=config.get('default','players',fallback='')
        rating=config.get('default','rating',fallback='')
        description=config.get('default','description',fallback='')
        assetsboxfront=config.get('default','assets.boxfront',fallback='')
        assetsvideo=config.get('default','assets.video',fallback='')
        assetslogo=config.get('default','assets.logo',fallback='')
        assetsscreenshot=config.get('default','assets.screenshot',fallback='')
        assetsbackground=config.get('default','assets.background',fallback='')

        game=Game(name, file, sortby, developer, publisher, genre,release,players,rating,description,assetsboxfront,assetsvideo,assetslogo,assetsscreenshot,assetsbackground)

        gamefilename=os.path.split(game.file)[1]

        if prefix:
            game.file = game.file.replace('./', prefix)
        else:
            game.file = os.path.join(rom_path, gamefilename)

        if choice:
            game.file = game.file.replace("/", "\\")
        else:
            game.file = game.file.replace("\\", "/")
            game.file = game.file.replace("//", "/")

        if fix_db_name:
            db_name = fix_db_name
        else:
            db_name = os.path.basename(rom_path) + '.lpl'

        process_pic(game,rom_path,db_name)

        gamelist.append({"path": game.file,"label": game.name, "core_path": "DETECT", "core_name": "DETECT", "crc32": "DETECT", "db_name": db_name})

    return gamelist


def process(check1, entry_metadata_file, entry_dest_playlist, entry_prefix, entry_db_name):
    choice = check1.get()
    metadatafile = entry_metadata_file.get()
    lplpathdir = entry_dest_playlist.get()
    prefix = entry_prefix.get()
    fix_db_name = entry_db_name.get()
    rom_path=os.path.split(metadatafile)[0]

    sections=prepare_sections(metadatafile)
    gamelists=prepare_gamelists(sections,prefix,choice,rom_path,fix_db_name)

    write_playlist(gamelists,lplpathdir,rom_path)

    
    messagebox.showinfo('提示', '任务执行已结束,Task Completed')

#################GUI####################


def selectpath(path):
    path_ = askdirectory()
    path.set(path_)

def selectfile(file):
    file_ = askopenfilename()
    file.set(file_)

def main():
    window = tk.Tk()
    window.title("天马前端资源转 Retroarch 列表生成工具")

    file1 = tk.StringVar()
    path2 = tk.StringVar()

    check1 = tk.BooleanVar(value=True)

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

    entry_metadata_file = tk.Entry(frame2, textvariable=file1,
                              state=tk.DISABLED, width=60)
    button_metadata_file = tk.Button(
        frame2, text="天马前端数据文件选择pegasus.metadata.txt", command=lambda: selectfile(file1))

    entry_dest_playlist = tk.Entry(frame3, textvariable=path2,
                                   state=tk.DISABLED, width=60)
    button_dest_playlist = tk.Button(frame3, text="Retroarch Playlist output path 列表文件输出文件夹选择", command=lambda: selectpath(
        path2))

    entry_prefix_label = tk.Label(
        frame4, text="Rom path prefix 路径前缀,比如为其他平台制作列表的场景,\r\n默认为metadata文件所在目录(可选,Optional)")
    entry_prefix = tk.Entry(frame4, width=60)

    entry_db_name_label = tk.Label(
        frame5, text="固定所有列表文件的db_name值,比如MAME.lpl,需要和最终retroarch封面所在的文件夹名称一致，\r\n 默认为metadata所在文件夹名称(可选,Optional)")
    entry_db_name = tk.Entry(frame5, width=60)

    button_confirm = tk.Button(
        frame6, text="确定 Go", command=lambda: process(check1, entry_metadata_file, entry_dest_playlist, entry_prefix, entry_db_name))

    # label_ori_dir.pack()
    entry_metadata_file.pack()
    button_metadata_file.pack()

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


if __name__ == '__main__':
    main()