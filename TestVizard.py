import viz
import vizfx
import vizshape
import vizact
import random

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
#vizact.ontimer2(0.5,19,spinPlant,vizact.choice(plants))

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

#
def changeTexture():
	global gateValue
	object = viz.pick()
	if object.valid():
		gateValue = (gateValue + 1) % 3
		gate.texture(gateTextures[gateValue])
	wireColor(wire3, GateOutput(gateValue, wire1Value, wire2Value))

def NotGate(b):
    return not b

def BufferGate(b):
    return b

def GateOutput(c, i1, i2):
	if c == 0:
		return i1 and i2
	elif c == 1:
		return i1 or i2
	else:
		if b1 == b2:
			return False
		else:
			return True

def objColor(obj, val):
	if val:
		obj.color(viz.YELLOW)
	else:
		obj.color(viz.WHITE)

andGateTex = viz.addTexture("AndGate.png")
orGateTex = viz.addTexture("OrGate.png")
xorGateTex = viz.addTexture("XorGate.png")
notGateTex = viz.addTexture("NotGate.png")
gateTextures = [andGateTex, orGateTex, xorGateTex]

light1 = [vizshape.addSphere(), False]
light2 = [vizshape.addSphere(), True]
light3 = [vizshape.addSphere(), True]
light4 = [vizshape.addSphere(), True]
light5 = [vizshape.addSphere(), False]
#outLight = vizshape.addSphere()

light1[0].setPosition(10,10,0)
light2[0].setPosition(10,8,0)
light3[0].setPosition(10,6,0)
light4[0].setPosition(10,4,0)
light5[0].setPosition(10,2,0)

light1[0].setScale(.5,.5,.5)
light2[0].setScale(.5,.5,.5)
light3[0].setScale(.5,.5,.5)
light4[0].setScale(.5,.5,.5)
light5[0].setScale(.5,.5,.5)

objColor(light1[0], light1[1])
objColor(light2[0], light2[1])
objColor(light3[0], light3[1])
objColor(light4[0], light4[1])
objColor(light5[0], light5[1])

wire1 = [vizshape.addCylinder(), light1[1]] #[object, boolVal]
wire1[0].setScale(.1,2,.1)
wire1[0].setPosition(10,10,-1.5)
wire1[0].setEuler([0,90,0])
objColor(wire1[0], wire1[1])

wire2 = [vizshape.addCylinder(), light2[1]]
wire2[0].setScale(.1,2,.1)
wire2[0].setPosition(10,8,-1.5)
wire2[0].setEuler([0,90,0])
objColor(wire2[0], wire2[1])

wire3 = [vizshape.addCylinder(), light3[1]]
wire3[0].setScale(.1,2,.1)
wire3[0].setPosition(10,6,-1.5)
wire3[0].setEuler([0,90,0])
objColor(wire3[0], wire3[1])

wire4 = [vizshape.addCylinder(), light4[1]]
wire4[0].setScale(.1,2,.1)
wire4[0].setPosition(10,4,-1.5)
wire4[0].setEuler([0,90,0])
objColor(wire4[0], wire4[1])

wire5 = [vizshape.addCylinder(), light5[1]]
wire5[0].setScale(.1,2,.1)
wire5[0].setPosition(10,2,-1.5)
wire5[0].setEuler([0,90,0])
objColor(wire5[0], wire5[1])

gate1 = [viz.addTexQuad(), 1, wire1[1], wire2[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate1[0].setPosition([10,9,-3])
gate1[0].texture(gateTextures[gate1[1]])
gate1[0].setEuler([90,0,0])

wire6 = [vizshape.addCylinder(), GateOutput(gate1[1], gate1[2], gate1[3])]
wire6[0].setScale(.1,2,.1)
wire6[0].setPosition(10,9,-5)
wire6[0].setEuler([0,90,0])
objColor(wire6[0], wire6[1])

'''
Test Logic gate code
wire1 = vizshape.addCylinder()
wire1.setPosition(5,2,2)
wire1.setScale(.1,4,.1)
wire1.setEuler([0,90,90])
wire1Value = False

wire2 = vizshape.addCylinder()
wire2.setPosition(5,2.5,2)
wire2.setScale(.1,4,.1)
wire2.color(viz.YELLOW)
wire2.setEuler([0,90,90])
wire2Value = True

wire3 = vizshape.addCylinder()
wire3.setPosition(10,2.25,2)
wire3.setScale(.1,4,.1)
wire3.setEuler([0,90,90])
wire3Value = False

vizact.onkeydown('r', changeTexture) #ROTATE GATE OPTIONS
''''''
