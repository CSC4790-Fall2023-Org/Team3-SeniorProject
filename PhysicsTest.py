import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
from loop import *
from utilFunctions import *

viz.go()

#Turn on the physics engine 
viz.phys.enable() 

#Add ground 
ground = viz.addChild('ground.osgb')
ground.collidePlane() #Make ground collide with objects as if it were an infinite plane

#Create seesaw board
seesaw = viz.addChild('box.wrl')
seesaw.setScale([10,0.3,1])
seesaw.collideBox() #Make object collide as if a bounding box surrounded the object


#Create balance point of seesaw
fulcrum = viz.addChild('tut_cone.wrl')
fulcrum.setScale([0.5,0.5,0.5])
fulcrum.setPosition([0,.01,1])
fulcrum.collideMesh() #Make object collide if its actual geometry intersects anotherobject
fulcrum.disable(viz.DYNAMICS) #Disablesdynamic physics forces from acting on the object


#Create weight on right side of seesaw
load = viz.addChild('duck.wrl')
load.collideBox()

#Create weight on left side of seesaw
counterWeight = viz.addAvatar('duck.cfg')
counterWeight.collideBox(density=5) #The high density parameter makes the object heavier




#Move the viewpoint so that it can see the show
viz.MainView.setPosition([0,2,-15])



#Puts the moving objects in their original state
def reset():    
    seesaw.reset() #Zeros out all forces
    seesaw.setPosition([0,3,5])
    seesaw.setEuler([0,0,0]) #Puts object upright

    load.reset()
    load.setPosition([4,5,5])
    load.setEuler([0,0,0])

    counterWeight.reset()
    counterWeight.setPosition([-4, 11, 5])
    counterWeight.setEuler([90,0,0])

#Reset simulation
reset()

vizact.onkeydown(' ', reset)
