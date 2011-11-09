'''
Created on 2011/02/09

@author: 0000136102
'''
from vectors import vector3
from objects import face, sphere
from numpy.ma.core import sqrt, max

class ray(vector3):
    ''' variables '''
    point = vector3(0.0,0.0,0.0)
    direction = vector3(1.0,0.0,0.0)

    ''' methods '''
    def __init__(self, ppnt, pdir):
        self.point = ppnt
        self.direction = vector3.nrm_vec(pdir)
    
    def reflect(self, face, normal):
        self.point = self.intersection(face)
        '''  calc direction '''
        tmp_vec = vector3.mul_vec(normal, 2*vector3.dot_vec(self.direction, normal))
        self.direction = vector3.sub_vec(self.direction, tmp_vec)
    
    def intersection (self, obj):
        k = 0.0
        if obj.radius > 0.0: #sphere
            o2e = vector3.sub_vec(self.point, obj.point)
            half_b = vector3.dot_vec(o2e, self.direction)
            c = vector3.dot_vec(o2e,o2e) - obj.radius*obj.radius
            if half_b*half_b - c >= 0:
                k =  -half_b - sqrt(half_b*half_b - c)
            else :
                k = 1.0e8
        else : #face
            o2e = vector3.sub_vec(self.point, obj.point)
            b = vector3.dot_vec(self.direction,obj.normal)
            if abs(b) > 1.0e-3 :
                k = -(vector3.dot_vec(o2e,obj.normal)) / b
            else :
                k = 1.0e8
        if k<0 : k = 1.0e8
        return vector3.mul_vec(self.direction, k)
    
    def checkInter(self, objlist):
        min_length = 1.0e8
        min_object = face(vector3(0.0,0.0,0.0), vector3(0.0,0.0,0.0), 0)
        for element in objlist:
            dest = self.intersection(element)
            if vector3.norm(dest) < min_length :
                min_length = vector3.norm(dest)
                min_object = element
        i_point = vector3.add_vec(self.point, vector3.mul_vec(self.direction, min_length))
        return i_point, min_object
    
    def checkShadow(self, start, light, objlist):
        occluded = 0
        o2light = vector3.nrm_vec(vector3.sub_vec(light.point, start))
        min_length = vector3.norm(o2light)
        if min_length > 1.0e6 : print "a"; return 0
        ray2light = ray(vector3.sub_vec(start,vector3.mul_vec(o2light, -1.0e-8)), o2light)
        for element in objlist:
            dest = ray2light.intersection(element)
            if vector3.norm(dest) < min_length :
                occluded = 1
        return occluded
    
    def calcColor(self, light, objlist):
        dest, i_obj = self.checkInter(objlist)
        occluded = self.checkShadow(dest, light, objlist)
        
        light2dest = vector3.nrm_vec(vector3.sub_vec(dest, light.point))
        if i_obj.radius > 0.0 :
            obj_normal = vector3.nrm_vec(vector3.sub_vec(dest,i_obj.point))
        else :
            obj_normal = i_obj.normal
        shading = -vector3.dot_vec(light2dest, obj_normal)
        if shading < 0.2 : shading = 0.2
        
        d_color = i_obj.color
        d_red = d_color & 255
        d_grn = (d_color>>8) & 255
        d_blu = (d_color>>16) & 255
        d_red *= shading
        d_grn *= shading
        d_blu *= shading
        
        if occluded > 0 :
            penalty = 128
            if d_red >= penalty : d_red -= penalty
            else : d_red = 0
            if d_grn >= penalty : d_grn -= penalty
            else : d_grn = 0
            if d_blu >= penalty : d_blu -= penalty
            else : d_blu = 0
        d_red = int(d_red)
        d_grn = int(d_grn)
        d_blu = int(d_blu)
        return (int(d_red) + (int(d_grn)<<8) + (int(d_blu)<<16))
        
        
            
            
            