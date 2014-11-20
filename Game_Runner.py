import os
import sys
gameLoop = True
while gameLoop:
    fileOpen = open('save.txt','r')
    str = []
    for line in fileOpen:
        tempStr = ""
        for k in range(0,len(line)-1): #Make it so \n does not appear!
            tempStr = tempStr+line[k]
        str.append(tempStr)
    fileOpen.close()
    os.system("python Game.py "+str[0]+" "+str[1]+" "+str[2])
    #Find some means to close this program
    fileOpen = open('save.txt','r')
    str = []
    for line in fileOpen:
        tempStr = ""
        for k in range(0,len(line)-1): #Make it so \n does not appear!
            tempStr = tempStr+line[k]
        str.append(tempStr)
    fileOpen.close()
    if str[3] == "0":
        sys.exit()