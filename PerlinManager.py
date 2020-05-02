import matplotlib.pyplot as plt
import numpy as np
class Perlin():
    def __init__(self,x,y,seed=0):
        self.result = self.perlin(x,y,seed)
        
    def perlin(self,x,y,seed=0):
        np.random.seed(seed)
        p = np.arange(256,dtype=int)
        np.random.shuffle(p)
        p = np.stack([p,p]).flatten()
        xi = x.astype(int)
        yi = y.astype(int)
        xf = x - xi
        yf = y - yi
        u = self.fade(xf)
        v = self.fade(yf)
        n00 = self.gradient(p[p[xi]+yi],xf,yf)
        n01 = self.gradient(p[p[xi]+yi+1],xf,yf-1)
        n11 = self.gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
        n10 = self.gradient(p[p[xi+1]+yi],xf-1,yf)
        x1 = self.lerp(n00,n10,u)
        x2 = self.lerp(n01,n11,u)
        return self.lerp(x1,x2,v)

    def lerp(self,a,b,x):
        return a + x * (b-a)

    def fade(self,t):
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    def gradient(self,h,x,y):
        vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
        g = vectors[h%4]
        return g[:,:,0] * x + g[:,:,1] * y

lin = np.linspace(0,5,100,endpoint=False)
x,y = np.meshgrid(lin,lin)
res = Perlin(x,y).result
