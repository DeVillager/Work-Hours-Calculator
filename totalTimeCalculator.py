import sys
import os

#-*- coding: cp1252 -*-

def main():
    #Replace the ? below with the path of your time lapse folder.
    path="?"
    a=os.listdir(path)
    s,m,h=0,0,0
    for f in a:
        b=open(path+"/"+f,"r")
        l = b.read().split(":")
        l[2]=l[2].split(".")[0]
        s+=int(l[2])
        m+=int(l[1])
        h+=int(l[0])
    m+=int(s/60)
    h+=int(m/60)
    print("total time: ",h," hours, ",m%60," minutes")

if __name__ == "__main__":
    main()






