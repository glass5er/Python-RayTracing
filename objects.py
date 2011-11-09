'''
Created on 2011/02/09

@author: 0000136102
'''
from vectors import vector3

class face:
    point = vector3(0.0,0.0,0.0)
    normal = vector3(0.0,0.0,0.0)
    redius = 0.0
    color = 255 + (255<<8) + (255<<16)
    
    def __init__(self, ppnt, pnrm, pcol):
        self.point = ppnt
        self.normal = pnrm
        self.color = pcol
        self.radius = 0.0
    
    def calcNormal(self):
        return (self.normal)
        
class sphere:
    point = vector3(0.0,0.0,0.0)
    normal = vector3(0.0,0.0,0.0)
    radius = 0.0
    color = 255 + (255<<8) + (255<<16)
    
    def __init__(self, ppnt, prad, pcol):
        self.point = ppnt
        self.radius = prad
        self.color = pcol
        self.normal = vector3(0.0,0.0,0.0)


    