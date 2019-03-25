import os.path

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "output.txt")
with open(path, "w", encoding="utf8") as f:
    f.write("こんにちは")
    f.write("Python" + "\n")
    f.write("Python 入門" +"\n")
    
