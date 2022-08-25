import csv 

with open("mame_0820.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    gamedict = {}
    for row in reader:
        gamedict[row['file']] = row['name']

with open("FBNeo-1.0.0.3.csv", mode="r", encoding="utf-8") as f2:
    reader2 = csv.DictReader(f2)
    gamedict2 = {}
    for row2 in reader2:
        gamedict2[row['file']] = row['name']

gamedict3={**gamedict,**gamedict2}

with open("gamelist_merge.csv", mode="w", encoding="utf8",newline='') as f3:
    csvwriter = csv.DictWriter(f3, fieldnames=["file", "name"])
    csvwriter.writeheader()
    game={}
    for key in gamedict3.keys():
        game['file']=key
        game['name']=gamedict3[key]
        csvwriter.writerow(game)

