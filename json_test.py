import json


with open("D:\Study\Python\json\FC.JSON", "r") as f:
    game = json.load(f)

content = json.dumps(game, indent=4)
with open("D:\Study\Python\json\dump.json", "w") as f:
    f.write(content)
