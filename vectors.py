'''
Created on 2011/02/09

@author: Kentaro Doba
'''
from numpy.ma.core import sqrt

class vector3:
    ''' variables '''
    x = 0.0
    y = 0.0
    z = 0.0

    ''' methods '''

    def __init__(self, px, py, pz):
        self.x = px
        self.y = py
        self.z = pz

    @staticmethod
    def add_vec (obj0, obj1):
        result = vector3(0.0,0.0,0.0)
        result.x = obj0.x + obj1.x
        result.y = obj0.y + obj1.y
        result.z = obj0.z + obj1.z
        return (result)

    @staticmethod
    def sub_vec (obj0, obj1):
        result = vector3(0.0,0.0,0.0)
        result.x = obj0.x - obj1.x
        result.y = obj0.y - obj1.y
        result.z = obj0.z - obj1.z
        return (result)

    @staticmethod
    def mul_vec (obj, coef):
        result = vector3(0.0,0.0,0.0)
        result.x = obj.x * coef
        result.y = obj.y * coef
        result.z = obj.z * coef
        return (result)

    @staticmethod
    def dot_vec (obj0, obj1):
        return (obj0.x*obj1.x + obj0.y*obj1.y + obj0.z*obj1.z )

    @staticmethod
    def crs_vec (obj0, obj1):
        result = vector3(0.0,0.0,0.0)
        result.x = obj0.y*obj1.z - obj0.z*obj1.y
        result.y = obj0.z*obj1.x - obj0.x*obj1.z
        result.z = obj0.x*obj1.y - obj0.y*obj1.x
        return (result)

    @staticmethod
    def norm (obj):
        return sqrt(obj.x*obj.x + obj.y*obj.y + obj.z*obj.z)

    @staticmethod
    def nrm_vec (obj):
        result = vector3(0.0,0.0,0.0)
        nrm = vector3.norm(obj)
        result.x = obj.x / nrm
        result.y = obj.y / nrm
        result.z = obj.z / nrm
        return (result)

