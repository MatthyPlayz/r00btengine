from ScreenManager import *
from math import floor, ceil
class TextBox():
    def __init__(self, label, content, w, h):
        self.PrintTB(self.PrepareTB(label, content, w,h))
        self.result = self.PrintTB(self.PrepareTB(label, content, w,h))
    def PrepareTB(self, label, content, w,h): # Size min 7x5
        n = w
        parts = [content[i:i+n] for i in range(0, len(content), n)]
        n = len(parts)
        tlc = "╔"
        trc = "╗"
        blc = "╚"
        brc = "╝"
        hl = "═"
        vl = "║"
        li = "╠"
        ri = "╣"
        top = tlc+(hl*w)+trc+"\n"
        mid = vl+(" "*w)+vl+"\n"
        lab = vl+((" "*ceil(w/2-len(label)/2))+label+((" "*floor(w/2-len(label)/2))+vl+"\n"))
        fps = ""
        for i in range(0, n):
            fps += (vl+((" "*ceil(w/2-len(parts[i])/2))+parts[i]+((" "*floor(w/2-len(parts[i])/2))+vl+"\n")))
        las = li+(hl*w)+ri
        bot = blc+(hl*w)+brc
        full = top+lab+las+"\n"+fps+bot
        return full
    def PrintTB(self,preptb):
        print(preptb)
        return preptb
        
        
