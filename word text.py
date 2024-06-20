fp=open("word.txt","w")
if fp:
    print("successfully opened the txt")
    fp.write("i")
    fp.write("a")
    fp.write(" ")
    fp.close()