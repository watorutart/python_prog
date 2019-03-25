import os.path

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "sample.txt")

# f = open(path, mode="r", encoding="utf-8")
with open(path,mode="r", encoding="utf-8") as f: # with文の場合はclose()が不要
    lines = f.readlines() # ファイル内をすべて読み込み
    for n, line in enumerate(lines):
        line = line.rstrip("\n")
        print(f"{n + 1}:{line}")
# f.close()

with open(path,mode="r", encoding="utf-8") as f: # with文の場合はclose()が不要
    for n, line in enumerate(f):
        line = line.rstrip("\n")  # 1行ずつ読み込み
        print(f"{n + 1}:{line}")
