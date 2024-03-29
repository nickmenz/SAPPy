#from sympy import *
from tkinter import Label
from tkinter.tix import LabelEntry
from tkinter.ttk import LabeledScale
import matplotlib.pyplot as plt
import numpy as np

#init_session()

#init_printing() 



#R = symbols('theta')
#A, L, I = symbols('A L I')


#T = Matrix((
#              [cos(R), sin(R),0,0,0,0],
#              [-sin(R), cos(R),0,0,0,0],
#              [0,0,1,0,0,0],
#              [0,0,0,cos(R),sin(R),0],
#              [0,0,0,-sin(R), cos(R),0],
#              [0,0,0,0,0,1]
#))
#K = Matrix((
#              [A*L**2/I, 0,0,-A*L**2/I,0,0],
#              [0,12,6*L,0,-12,6*L],
#              [0,6*L,4*L**2,0,-6*L,2*L**2],
#              [-A*L**2/I,0,0,A*L**2/I,0,0],
#              [0,-12,-6*L,0,12,-6*L],
#              [0,6*L,2*L**2,0,-6*L,4*L**2],
#))
#Result = transpose(T)*K*T
#Result = simplify(Result)
#pprint(Result)


#init_session()

#init_printing() 



#R = symbols('theta')
#A, L, I = symbols('A L I')


#T = Matrix((
#              [cos(R), sin(R),0,0,0,0],
#              [-sin(R), cos(R),0,0,0,0],
#              [0,0,1,0,0,0],
#              [0,0,0,cos(R),sin(R),0],
#              [0,0,0,-sin(R), cos(R),0],
#              [0,0,0,0,0,1]
#))
#K = Matrix((
#              [1, 0,0,-1,0,0],
#              [0,0,0,0,0,0],
#              [0,0,0,0,0,0],
#              [-1,0,0,1,0,0],
#              [0,0,0,0,0,0],
#              [0,0,0,0,0,0],
#))
#Result = transpose(T)*K*T
##Result = simplify(Result)
#pprint(Result, use_unicode=False, wrap_line = 1000)




######### HOW TO SCALE POLYGONS
#import matplotlib.pyplot as plt
#import matplotlib.patches as patches
#import matplotlib.transforms as transform
#import numpy as np
#from numpy import radians as rad

#fig, ax = plt.subplots()


#pin = plt.Polygon([[0, 0],[0.5, 1],[1, 0]],color='red',transform=ax.transData)
#ax.add_patch(pin)
#roller = patches.Circle([4, 6], radius=0.5, color='red',transform=ax.transData)
#ax.add_patch(roller)
#ax.scatter([-10, 10],[-50, 100])

## Need to add ax.transData second so that it scales first, then translates accordingly
#t1 =  transform.Affine2D().scale(10) + ax.transData
##t1 = transform.Affine2D().scale(30)
##t2 = transform.Affine2D().scale(1)
#roller.set(transform=t1)
#pin.set(transform=t1)
#ax.axis("equal")
#plt.show()


#import matplotlib.pyplot as plt
#plt.switch_backend('TkAgg')
#import time

#plt.ion()

#plt.plot([1.5, 3.0])

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon, Wedge

#x = np.linspace(0, 9, 10)
#y = x**3

#y1 = x*0

#fig,ax = plt.subplots()
#ax.plot(x, y)
#ax.plot(x, y1)
#collection = ax.fill_between(x, y, y1)
#print(collection)

#plt.show()

fig,ax = plt.subplots()
poly1 = Polygon([[0,0],
             [10,0],
             [10,15],
             [0,15]
             ])
patches = []
patches.append(poly1)
p = PatchCollection(patches)
ax.add_collection(p)
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
plt.show()

R = 1
trans_matrix = np.array(())

transform = 




