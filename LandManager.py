from math import ceil, floor
from opensimplex import OpenSimplex
from random import randint
def Landifier(inte):
    if int(ceil(inte)) <= 0:
        return " "
    elif str(ceil(inte)) == "0":
        return " "
    elif str(ceil(inte)) == "1":
        return "$"
    elif int(str(floor(inte))) == "2":
        return "#"
    elif int(ceil(inte)) >= 2: 
        return "%"

def Land(w=64,h=64,seed=randint(0,1000)):
    tmp = OpenSimplex(seed=seed)
    land = []
    tmp2 = []
    for y in range(h):
        for x in range(w):
            tmp2.append(tmp.noise2d(x=x, y=y))
        
        land.append(tmp2)
        tmp2=[]
    return land

def LandifyLand(li):
    land = []
    tmp2 = []
    
    for y in range(len(li)):
        for x in range(len(li[y])):
            tmp2.append(Landifier(li[y][x]))

        land.append(tmp2)
        tmp2=[]
    return land
def StackNoise(w=16,h=16,seed=randint(0,1000),times=5):
    land = []
    tmp2 = []
    NoiseLayers = []
    for i in range(1,times):
        NoiseLayers.append(Land(w,h,seed))
    li = NoiseLayers[0]
    for t in range(1,len(NoiseLayers)):
        for y in range(len(NoiseLayers[t])):
            for x in range(len(NoiseLayers[t][y])):
                li[y][x] += NoiseLayers[t][y][x]
    return li
def SettingLand(arg):
    if arg == "A":
        return LandifyLand(StackNoise(times=2))
    elif arg == "MA":
        return LandifyLand(StackNoise(times=3))
    elif arg == "MI":
        return LandifyLand(StackNoise(times=6))
    else:
        return LandifyLand(Land())
