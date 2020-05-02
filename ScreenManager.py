# ScreenPrinter will take a format like this:
# [
#   ["_","_","_"],
#   ["|"," ","|"],
#   ["|","_","|"]
# ]
Test = [
    ["#"," "," ","#","#","#"," ","#"," "," "," "," "," "],
    ["#"," "," ","#"," ","#"," ","#"," "," "," "," "," "],
    ["#","#"," ","#","#","#"," ","#","#"," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "," ","#","#"],
    [" "," "," "," "," "," "," "," "," "," "," ","#"," "],
    [" "," "," "," "," "," "," "," "," "," "," ","#","#"],
    [" "," "," "," "," "," "," "," "," "," "," ","#"," "],
    [" "," "," "," "," "," "," "," "," "," "," ","#"," "]
]
from math import floor, ceil
def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return ceil(middle - .5)
    else:
        return ceil(middle)

class Screen():
    def __init__(self, screendata, resw=10, resh=5,topp=0,leftp=0):
        a = self.JoinScreen(screendata, resw, resh, leftp, topp)
        b = self.PlacePlayer(a, resw, resh)
        c = self.LineupScreen(b, resw, resh, leftp, topp)
        self.result = self.PrintScreen(c)
    def JoinScreen(self, scrndat, resw, resh, leftp, topp):
        final = []
        if(leftp==0):
            for lis in scrndat[:resh]:
                if lis == None:
                    lis = "ERR"
                final.append("".join(lis))
        else:
            for lis in scrndat[:resh]:
                if lis == None:
                    lis = "ERR"
                final.append("".join(lis[leftp:-1]))
        return final
    def PlacePlayer(self, sd, resw, resh):
        lst = sd
        tstr = []
        b = 0
        for i in lst[findMiddle(lst)-1]:
            if i == lst[findMiddle(lst)-1][int(findMiddle(lst[findMiddle(lst)-1])/2)] and b == int(findMiddle(lst[findMiddle(lst)-1])/2)+2:
                tstr.append("@")
            else:
                tstr.append(i)
            b+=1
        lst[findMiddle(lst)-1] = tstr
        return lst
    def LineupScreen(self, scrndatJoin, resw, resh, leftp, topp):
        final = ""
        if(leftp==0):
            for lis in scrndatJoin[0:resw]:
                if lis == None:
                    lis = "ERR"
                final+="".join(lis)+"\n"
        else:
            for lis in scrndatJoin[topp:resw]:
                if lis == None:
                    lis = "ERR"
                final+="".join(lis)+"\n"
        return final
    def PrintScreen(self, scrndatLineup):
        print(scrndatLineup)
        return scrndatLineup
    
