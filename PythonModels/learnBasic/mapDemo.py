# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/27.
'''

speed_map = {
    'dog': (48, '#7199cf'),
    'cat': (45, '#4fc4aa'),
    'cheetah': (120, '#e1a7a2')
}


arr=[x[0] for x in speed_map.values()]


print arr

names=speed_map.keys()
print names