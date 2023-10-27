import viz
import viztask
import vizact
import vizinfo
import vizmat
import vizproximity
import vizshape
import vizfx
from loop import *
from utilFunctions import *

isCave = False

viz.phys.enable()

ALMOST_ZERO=0.000001

class MyDtrackManager():
	def __init__(self, default_head_pos=[0,1,0]):
		self.default_head_pos = default_head_pos
		self.wrapped_tracker = None
		self.raw_vrpn = None
		self.dtrack_updater = None
					
	def startDefaultHeadPosition(self):
		self.wrapped_tracker = vizconnect.getTracker("dtrack_head")
		self.raw_vrpn = self.wrapped_tracker.getRaw()
		
		fakeTracker = viz.addGroup()
		fakeTracker.setPosition(self.default_head_pos)
		self.wrapped_tracker.setRaw(fakeTracker)
		
		#This calls check_dtrack each frame
		self.dtrack_updater = vizact.onupdate(0, self.check_dtrack)
	
	def check_dtrack(self):
		x, y, z = self.raw_vrpn.getPosition()
		atOrigin = self.isAlmostZero(x) or self.isAlmostZero(y) or self.isAlmostZero(z)
		
		if not atOrigin:
			self.wrapped_tracker.setRaw(self.raw_vrpn)
			self.dtrack_updater.remove()
	
	#Will move to other library
	def isAlmostZero(self, val):
		if abs(val) <= ALMOST_ZERO:
			return True
		else:
			return False

joystickTracker = None
#viz.setMultiSample(4)
viz.fov(80)
if isCave:
	import vizconnect
	CONFIG_FILE = "vizconnect_config_CaveFloor+ART_headnode.py"
	#CONFIG_FILE = ""
	vizconnect.go(CONFIG_FILE)	
	dtrack_manager = MyDtrackManager()
	dtrack_manager.startDefaultHeadPosition()
	joystickTracker = vizconnect.getTracker("dtrack_flystick")
	viz.MainView.collision(viz.ON)
else:
	viz.go()
	viz.MainView.collision(viz.ON)

#variable for toggling door
isDoor = True

# Set up room and put up walls
room = viz.addChild('lab.osgb')

# Add table
table = viz.addChild('CustomModels/table1.osgb')
table.setScale([0.01, 0.0125, 0.01])
table.setPosition([4.5, 0, 0])
table.setEuler(90, 0, 0)

''''''''''''''''''''''' ABOVE DOOR -- TIMER '''''''''''''''''''''
#Load Textures
tex0 = viz.addTexture('CustomTextures/timer/0.png')
tex1 = viz.addTexture('CustomTextures/timer/1.png')
tex2 = viz.addTexture('CustomTextures/timer/2.png')
tex3 = viz.addTexture('CustomTextures/timer/3.png')
tex4 = viz.addTexture('CustomTextures/timer/4.png')
tex5 = viz.addTexture('CustomTextures/timer/5.png')
tex6 = viz.addTexture('CustomTextures/timer/6.png')
tex7 = viz.addTexture('CustomTextures/timer/7.png')
tex8 = viz.addTexture('CustomTextures/timer/8.png')
tex9 = viz.addTexture('CustomTextures/timer/9.png')
colon = viz.addTexture('CustomTextures/timer/colon.png')
white1 = viz.addTexture('CustomTextures/timer/white1.jpg')

#Add textures to an array, array numbers correspond with Quad# (3 is colon)
countUp1 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex0])
countUp2 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex0])
countUp4 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex0])
countUp5 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex0])

#Add a background to mount the clock on 
back = viz.addTexQuad()
back.setScale([2.5,0.6,0.5])
back.setPosition([0, 3.25, 4.999])  # Put quad in view
#Start digit at 0
back.texture(white1)


#Ones seconds digit
quad1 = viz.addTexQuad()
quad1.setScale([0.3,0.3,0.3])
quad1.setPosition([1, 3.25, 4.998])  # Put quad in view
#Start digit at 0
quad1.texture(tex0)

#Tens seconds digit
quad2 = viz.addTexQuad()
quad2.setScale([0.3,0.3,0.3])
quad2.setPosition([0.5, 3.25, 4.998])  # Put quad in view
#Start digit at 0
quad2.texture(tex0)

#Colon
quad3 = viz.addTexQuad()
quad3.setScale([0.3,0.3,0.3])
quad3.setPosition([0, 3.25, 4.998])  # Put quad in view
quad3.texture(colon)

#Ones minutes digit
quad4 = viz.addTexQuad()
quad4.setScale([0.3,0.3,0.3])
quad4.setPosition([-0.5, 3.25, 4.998])  # Put quad in view
#Start digit at 0
quad4.texture(tex0)

#Tens minutes digit
quad5= viz.addTexQuad()
quad5.setScale([0.3,0.3,0.3])
quad5.setPosition([-1, 3.25, 4.998])  # Put quad in view
#Start digit at 0
quad5.texture(tex0)
	
def swap_timer_tex(a1, q1, a2, q2, a3, q3, a4, q4):
	counter = 0
	while True:
		yield viztask.waitTime(1)
		counter = counter + 1
		#print(counter)
		
		#increment ones digit of seconds
		q1.texture(a1.next())
		
		#increment tens digits of seconds
		if(counter % 10 == 0):
			q2.texture(a2.next())
		
		#increment ones digit of minutes
		if(counter % 60 == 0):
			q3.texture(a3.next())
		
		#increment tens digit of minutes
		if(counter % 600 == 0):
			q4.texture(a4.next())
		
timer = viztask.schedule( swap_timer_tex(countUp1, quad1, countUp2, quad2, countUp4, quad4, countUp5, quad5) )
''''''''''''''''''''''' END OF ABOVE DOOR -- TIMER '''''''''''''''''''''

'''''''''RIGHT WALL -- KNAPSACK PROBLEM'''''''''
# Left Box
leftBox = vizshape.addCube()
leftBox.collideMesh()
leftBox.setScale([1, 1.75, 1.3])
leftBox.setPosition([-4.7, 0, -2])
leftBox.color(viz.BLACK)
leftBox.disable(viz.DYNAMICS)

# Middle Box
middleBox = vizshape.addCube()
middleBox.collideMesh()
middleBox.setScale([1, 1.75, 1.3])
middleBox.setPosition([-4.7, 0, 0.5])
middleBox.color(viz.BLACK)
middleBox.disable(viz.DYNAMICS)

# Right Box
rightBox = vizshape.addCube()
rightBox.collideMesh()
rightBox.setScale([1, 1.75, 1.3])
rightBox.setPosition([-4.7, 0, 3])
rightBox.color(viz.BLACK)
rightBox.disable(viz.DYNAMICS)


# RED CUBE
redCube = vizshape.addCube()
redCube.collideBox()
redCube.setScale([0.15, 0.15, 0.15])
redCube.setPosition([-4.7, 1.2, 3])
redCube.color(viz.RED)

# BLUE CUBE
blueCube = vizshape.addCube()
blueCube.collideBox()
blueCube.setScale([0.15, 0.15, 0.15])
blueCube.setPosition([-4.7, 1.2, 0.5])
blueCube.color(viz.BLUE)

# GREEN CUBE
greenCube = vizshape.addCube()
greenCube.collideBox()
greenCube.setScale([0.15, 0.15, 0.15])
greenCube.setPosition([-4.8, 1.2, -1.6])
greenCube.color(viz.GREEN)

# ORANGE CUBE
orangeCube = vizshape.addCube()
orangeCube.collideBox()
orangeCube.setScale([0.15, 0.15, 0.15])
orangeCube.setPosition([-4.35, 1.2, -2.4])
orangeCube.color(viz.ORANGE)



'''
# BLACK CUBE
blackCube = vizshape.addCube()
blackCube.collideBox(density=5)

blackCube.setScale([0.2, 0.2, 0.2])
blackCube.setPosition([-4.83, 0.24, -2.3])
blackCube.color(viz.BLACK)

# PURPLE CUBE
purpleCube = vizshape.addCube()
purpleCube.collideBox(density=5)

purpleCube.setScale([0.2, 0.2, 0.2])
purpleCube.setPosition([-4.83, 1.57, -2.8])
purpleCube.color(viz.PURPLE)
'''
'''''''''END OF RIGHT WALL -- KNAPSACK PROBLEM'''''''''


# Create Wall 1 with door
# The wall consists of three parts, left of the door, above the door, and right of the door
# Alternatively door could be overlaid on a singular instance of the wall, however this gives the option to have 
	# an event derender the door and create an openning to pass to another room

if isDoor: 
	door = viz.addTexQuad()
	door.setScale([1.5,2.5,1])
	door.setPosition([0,1.25,5])
	doorCover = viz.addTexture('CustomTextures/door.jpg')
	door.texture(doorCover)

# Fill in wall around door
wallOneLeft = viz.addTexQuad()
wallOneRight = viz.addTexQuad()
wallOneAbove = viz.addTexQuad()

wallOneLeft.setPosition([-2.875,2.5,5])
wallOneRight.setPosition([2.875,2.5,5])
wallOneAbove.setPosition([0,3.75,5])

wallOneLeft.setScale([4.25,5,1])
wallOneRight.setScale([4.25,5,1])
wallOneAbove.setScale([1.5,2.5,1])

wallTwo = viz.addTexQuad()
wallTwo.setPosition([5,2.5,0])
wallTwo.setEuler([90,0,0])
wallTwo.setScale([10,5,10])
wallThree = viz.addTexQuad()
wallThree.setPosition([-5,2.5,0])
wallThree.setEuler([-90,0,0])
wallThree.setScale([10,5,10])
wallFour = viz.addTexQuad()
wallFour.setPosition (0,2.5,-5)
wallFour.setScale([10,5,10])
ceiling = viz.addTexQuad()
ceiling.setPosition([0,4,0])
ceiling.setEuler([0,90,0])
ceiling.setScale([10,10,10])
floor = viz.addTexQuad()
floor.setPosition([0,0.001,0])
floor.setEuler([0,90,0])
floor.setScale([10,10,10])

# ---------------------------------
# viz.INTERSECT must be turned off for all the room walls so we don't accidentally pick up the floor !!!
# ---------------------------------


# Create textures
wallCover = viz.addTexture('CustomTextures/concreteWall.jpg')
ceilingCover = viz.addTexture('images/tile_slate.jpg')
floorCover = viz.addTexture('CustomTextures/wood.jpg')


# Cover walls with texture
wallOneLeft.texture(wallCover)
wallOneRight.texture(wallCover)
wallOneAbove.texture(wallCover)
wallTwo.texture(wallCover)
wallThree.texture(wallCover)
wallFour.texture(wallCover)
ceiling.texture(ceilingCover)

# Cover floor with texture
floor.texture(floorCover)

# Spawn loop problem structure
createProblem()
spawnCodeBoxes()

# Establish line
#lineStart = [0,3,0]
#lineEnd = [1,0.1,-2]
#line = drawLine(lineStart, lineEnd)

# Add callbacks
#vizact.onupdate(0, checkHover, joystickTracker)
#vizact.onupdate(0, drawJoystickLine, joystickTracker)

# Testing
#selected = viz.Intersect(lineStart, lineEnd)
#checkHover(lineStart, lineEnd)
# setTextures()

light = viz.addLight()
light.color(viz.WHITE)
light.setPosition(0, 3, 0)
light.intensity(100)



'''''''''''''''''''''''''''''LOGIC GATE PROBLEM'''''''''''''''''''''''''''''''''
def changeTexture():
	global gateValue
	object = viz.pick()
	if object.valid():
		gateValue = (gateValue + 1) % 3
		gate.texture(gateTextures[gateValue])
	wireColor(wire3, GateOutput(gateValue, wire1Value, wire2Value))

def NotGate(c, i):
	if c == 0:
		return not i
	else:
		return i

def GateOutput(c, i1, i2):
	if c == 0:
		return i1 and i2
	elif c == 1:
		return i1 or i2
	else:
		if i1 == i2:
			return False
		else:
			return True

def objColor(obj, val):
	if val:
		obj.color(viz.YELLOW)
	else:
		obj.color(viz.WHITE)
		
andGateTex = viz.addTexture("CustomTextures/logic-symbols/AndGate.png")
orGateTex = viz.addTexture("CustomTextures/logic-symbols/OrGate.png")
xorGateTex = viz.addTexture("CustomTextures/logic-symbols/XorGate.png")
notGateTex = viz.addTexture("CustomTextures/logic-symbols/NotGate.png")
gateTextures = [andGateTex, orGateTex, xorGateTex]

light1 = [vizshape.addSphere(), False]
light1[0].setPosition(5,3.5,1.5)
light1[0].setScale(.25,.25,.25)
objColor(light1[0], light1[1])

light2 = [vizshape.addSphere(), True]
light2[0].setPosition(5,2.75,1.5)
light2[0].setScale(.25,.25,.25)
objColor(light2[0], light2[1])

light3 = [vizshape.addSphere(), True]
light3[0].setPosition(5,2,1.5)
light3[0].setScale(.25,.25,.25)
objColor(light3[0], light3[1])

light4 = [vizshape.addSphere(), True]
light4[0].setPosition(5,1.25,1.5)
light4[0].setScale(.25,.25,.25)
objColor(light4[0], light4[1])

light5 = [vizshape.addSphere(), False]
light5[0].setPosition(5,0.5,1.5)
light5[0].setScale(.25,.25,.25)
objColor(light5[0], light5[1])

wire1 = [vizshape.addCylinder(), light1[1]] #[object, boolVal]
wire1[0].setPosition(5,3.5,2)
wire1[0].setScale(.1,1,.1)
wire1[0].setEuler([0,90,0])
objColor(wire1[0], wire1[1])

wire2 = [vizshape.addCylinder(), light2[1]]
wire2[0].setPosition(5,2.75,2)
wire2[0].setScale(.1,1,.1)
wire2[0].setEuler([0,90,0])
objColor(wire2[0], wire2[1])

wire3 = [vizshape.addCylinder(), light3[1]]
wire3[0].setPosition(5,2,2)
wire3[0].setScale(.1,1,.1)
wire3[0].setEuler([0,90,0])
objColor(wire3[0], wire3[1])

wire4 = [vizshape.addCylinder(), light4[1]]
wire4[0].setPosition(5,1.25,2)
wire4[0].setScale(.1,1,.1)
wire4[0].setEuler([0,90,0])
objColor(wire4[0], wire4[1])

wire5 = [vizshape.addCylinder(), light5[1]]
wire5[0].setPosition(5,0.5,3.5)
wire5[0].setScale(.1,4,.1)
wire5[0].setEuler([0,90,0])
objColor(wire5[0], wire5[1])

gate1 = [viz.addTexQuad(), 1, wire1[1], wire2[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate1[0].setPosition([4.9,3,2.8])
gate1[0].setScale(0.75,0.75,0.75)
gate1[0].setEuler([90,0,180])
gate1[0].texture(gateTextures[gate1[1]])

wire6 = [vizshape.addCylinder(), GateOutput(gate1[1], gate1[2], gate1[3])]
wire6[0].setPosition(5,3,4)
wire6[0].setScale(.1,3,.1)
wire6[0].setEuler([0,90,0])
objColor(wire6[0], wire6[1])

gate2 = [viz.addTexQuad(), 0, wire3[1], wire4[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate2[0].setPosition([4.9,1.7,2.7])
gate2[0].setScale(0.75,0.75,0.75)
gate2[0].setEuler([90,0,180])
gate2[0].texture(gateTextures[gate1[2]])

wire7 = [vizshape.addCylinder(), GateOutput(gate2[1], gate2[2], gate2[3])]
wire7[0].setPosition(5,1.7,4)
wire7[0].setScale(.1,3,.1)
wire7[0].setEuler([0,90,0])
objColor(wire7[0], wire7[1])

wire8 = [vizshape.addCylinder(), wire6[1]]
wire8[0].setPosition(4.5,3,5)
wire8[0].setScale(.1,1,.1)
wire8[0].setEuler([90,90,0])
objColor(wire8[0], wire8[1])

wire9 = [vizshape.addCylinder(), wire7[1]]
wire9[0].setPosition(4.5,1.7,5)
wire9[0].setScale(.1,1,.1)
wire9[0].setEuler([90,90,0])
objColor(wire9[0], wire9[1])

wire10 = [vizshape.addCylinder(), wire5[1]]
wire10[0].setPosition(4.5,0.5,5)
wire10[0].setScale(.1,1,.1)
wire10[0].setEuler([90,90,0])
objColor(wire10[0], wire10[1])

gate3 = [viz.addTexQuad(), 0, wire8[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate3[0].setPosition([3.5,3,4.8])
gate3[0].setScale(0.75,0.75,0.75)
gate3[0].setEuler([0,0,180])
gate3[0].texture(notGateTex)

gate4 = [viz.addTexQuad(), 2, wire9[1], wire10[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate4[0].setPosition([3.5,1.2,4.8])
gate4[0].setScale(0.75,0.75,0.75)
gate4[0].setEuler([0,0,180])
gate4[0].texture(gateTextures[gate4[1]])

wire11 = [vizshape.addCylinder(), NotGate(gate3[1], gate3[2])]
wire11[0].setPosition(2.8,2.5,5)
wire11[0].setScale(.1,1.5,.1)
wire11[0].setEuler([90,35,0])
objColor(wire11[0], wire11[1])

wire12 = [vizshape.addCylinder(), GateOutput(gate4[1], gate4[2], gate4[3])]
wire12[0].setPosition(2.8,1.2,5)
wire12[0].setScale(.1,1,.1)
wire12[0].setEuler([90,90,0])
objColor(wire12[0], wire12[1])

gate5 = [viz.addTexQuad(), 1, wire11[1], wire12[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate5[0].setPosition([2,1.5,4.8])
gate5[0].setScale(0.75,0.75,0.75)
gate5[0].setEuler([0,0,180])
gate5[0].texture(gateTextures[gate5[1]])

wire12 = [vizshape.addCylinder(), GateOutput(gate5[1], gate5[2], gate5[3])]
wire12[0].setPosition(1.5,1.5,5)
wire12[0].setScale(.1,0.5,.1)
wire12[0].setEuler([90,90,0])
objColor(wire12[0], wire12[1])

outlight = [vizshape.addSphere(), wire12[1]]
outlight[0].setPosition(1,1.5,5)
outlight[0].setScale(.25,.25,.25)
objColor(outlight[0], outlight[1])

def moveMushroom():
	move = vizact.animation(2)
	mushroom.addAction(move)	
	
mushroom = viz.addAvatar('CustomModels/MushroomMan/Martial_arts_character.osgb')
vizact.onkeydown('3', moveMushroom)
mushroom.setScale([0.5, 0.5, 0.5])
mushroom.setPosition([4.5, 1, 0])
mushroom.setEuler(90,0,0)


