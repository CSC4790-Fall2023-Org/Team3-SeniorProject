import viz
import vizfx
import vizshape
import vizact
import random
import vizfx

viz.setMultiSample(4)

viz.go()
viz.MainWindow.fov(60)

lobby = vizfx.addChild('piazza.osgb')
viz.collision(viz.ON)

#vizshape.addAxes() adds an axis object

spin = vizact.spin(1,1,1,1000)

viz.MainView.move([0,0,-8]) #change the camera position
#viz.MainView.setEuler([0,0,30])  change the angles of the camera

plants = []
for x in [-3,-1,1,3]:
	for z in [4,2,0,-2,4]:
		plant = viz.addChild('plant.osgb', cache=viz.CACHE_CLONE)
		plant.setPosition([x,0,z])
		plants.append(plant)
	
#		plant.setEuler([0,0,20]) Change the rotation
#		plant.setScale([1,1,1])  Change the size

def spinPlant(plant):
	plant.addAction(spin)
#causes the plants to spin
vizact.ontimer2(0.5,19,spinPlant,vizact.choice(plants))

male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5,0,7])
male.setEuler([0,0,0])
male.state(14)

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])
female.state(14)

pigeons = []
for i in range(10):
	x = random.randint(-4,3)
	z = random.randint(4,8)
	yaw = random.randint(0,360)
	
	pigeon = viz.addAvatar('pigeon.cfg')
	
	pigeon.setPosition([x,0,z])
	#pigeon.setScale([10,10,10])
	pigeon.setEuler([yaw,0,0])
	pigeon.state(1)
	
	pigeons.append(pigeon)

def walkAvatars():
	walk1 = vizact.walkTo([4.5,0,-40])
	vizact.ontimer(0.5,female.addAction,walk1)
	
	walk2 = vizact.walkTo([3.5,0,-40])
	male.addAction(walk2)
	
def pigeonsFeed():
	random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
	random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
	random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
	random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
	pigeon_idle = vizact.sequence(random_speed, random_walk,random_animation,random_wait,viz.FOREVER)
	
	for pigeon in pigeons:
		pigeon.addAction(pigeon_idle)
		
vizact.onkeydown('1', walkAvatars)
vizact.onkeydown('2', pigeonsFeed)

def moveMushroom():
	move = vizact.animation(2,freeze=True)
	mushroom.addAction(move)	
	
mushroom = viz.addAvatar('Martial_arts_character.osgb')
mushroom.setScale([1,1,1])
vizact.onkeydown('3', moveMushroom)
