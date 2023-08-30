import os
def clr(fname):
    f=open("temp.json","w")
    f.close()
    os.remove(fname)
    os.rename("temp.json",fname)

clr("datewise.json")
clr("locationwise.json")
clr("data.json")
