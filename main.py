'''
Created on 2011/02/09

@author: Kentaro Doba
'''

## import libraries ##
from ray import vector3
from ray import ray
from PIL import Image
from PIL import ImageDraw
from objects import face, sphere
from numpy.ma.core import tan


##  main process  ##
if __name__ == '__main__':
    ##  initialize parameters  ##
    w = 320
    h = 240
    PI = 3.14159265
    view_angle = 60 * PI / 180.0 
    view_ratio = tan(view_angle/2) / (w/2.0)
    img_size = (w,h)
    im = Image.new("RGB", img_size, 'rgb(128,128,128)')
    draw = ImageDraw.Draw(im)

    ##  objects in virtual space  ##
    ''' set light '''
    light = ray(vector3(1.0,-1.8,5.0), vector3(0.0,1.0,0.0))
    ''' set eye position'''
    eye = vector3(0.0,0.0,-1.0)
    ''' primitive objects '''
    obj_list = []
    obj_list.append(face(vector3(0.0,-2.0,0.0), vector3(0.0,1.0,0.0), 255))
    obj_list.append(face(vector3(0.0, 2.0,0.0), vector3(0.0,-1.0,0.0), 255<<8))
    obj_list.append(face(vector3(-2.0,0.0,0.0), vector3(1.0,0.0,0.0), 255<<16))
    obj_list.append(face(vector3( 2.0,0.0,0.0), vector3(-1.0,0.0,0.0), 255 + (255<<8)))
    obj_list.append(face(vector3(0.0,0.0,10.0), vector3(0.0,0.0,-1.0), 255 + (255<<8) + (255<<16)))
    obj_list.append(sphere(vector3(0.0,0.7,5.0), 1.5, 255 + (255<<16)))

    v_percentage = 1
    ##  each line  ##
    for y in range(0,h):
        if  v_percentage <= y*100 // h :
            print str(v_percentage) + " %" 
            v_percentage = y*100//h + 1
        ##  each pixel  ##
        for x in range(0,w):
            screen = vector3((x-w/2)*view_ratio, (y-h/2)*view_ratio, 0.0)
            inv_eyevec = vector3.sub_vec(screen, eye)
            inv_ray = ray(eye,inv_eyevec)
            ##  calc color  ##
            pixel_color = inv_ray.calcColor(light, obj_list)
            draw.point((x,y), pixel_color)

    ##  print percentage  ##
    print str(v_percentage) + " %" 

    ##  save image  ##
    im.save(r'out.png')
    print("done.")
    pass
