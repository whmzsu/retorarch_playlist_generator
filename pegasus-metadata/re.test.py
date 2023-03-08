import re
import os

# 要替换的特征字符串
pattern = "pegasus"

# 要替换成的路径
new_path = "hehehe"

# 遍历目录下的所有文件
for root, dirs, files in os.walk(r"D:\Study\retorarch_playlist_generator\pegasus-metadata"):
    for file in files:
        print(file)
        # 获取文件的完整路径
        file_path = os.path.join(root, file)
        # 使用正则表达式匹配特征字符串
        match = re.search(pattern, file_path)
        print(match)
        if match:
            # 如果匹配成功，将前半部分替换为新的路径
            new_file_path = os.path.join(new_path, file_path[match.end():])
            # 打印替换前后的路径
            print("原路径：", file_path)
            print("新路径：", new_file_path)
            # 将文件移动到新的路径
            #os.rename(file_path, new_file_path)