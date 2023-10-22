import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import vizfx
from loop import *
from utilFunctions import *

isCave = False

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
			
#viz.setMultiSample(4)
viz.fov(80)
if isCave:
	import vizconnect
	CONFIG_FILE = "E:\\VizardProjects\\_CaveConfigFiles\\vizconnect_config_CaveFloor+ART_headnode.py"
	vizconnect.go(CONFIG_FILE)	
	dtrack_manager = MyDtrackManager()
	dtrack_manager.startDefaultHeadPosition()
else:
	viz.go()
	viz.collision(viz.ON)

#variable for toggling door
isDoor = True

# Set up room and put up walls
room = viz.addChild('lab.osgb')

# Add table
table = viz.addChild('CustomModels/table1.osgb')
table.setScale([0.01, 0.0125, 0.01])
table.setPosition([4.5, 0, 0])
table.setEuler(90, 0, 0)


'''''''''RIGHT WALL -- KNAPSACK PROBLEM'''''''''
# LEFT SHELF
shelf = viz.addChild('CustomModels/shelf.fbx')
shelf.setEuler(90, 0, 0)
shelf.setScale([0.013, 0.0125, 0.01])
shelf.setPosition([-4.5, 0, -2])

# MIDDLE SHELF
shelf = viz.addChild('CustomModels/shelf.fbx')
shelf.setEuler(90, 0, 0)
shelf.setScale([0.013, 0.0125, 0.01])
shelf.setPosition([-4.5, 0, 0.5])

# RIGHT SHELF
shelf = viz.addChild('CustomModels/shelf.fbx')
shelf.setEuler(90, 0, 0)
shelf.setScale([0.013, 0.0125, 0.01])
shelf.setPosition([-4.5, 0, 3])


# RED CUBE
redCube = vizshape.addCube()
redCube.setScale([0.2, 0.2, 0.2])
redCube.setPosition([-4.63, 1.1, 2.25])
redCube.color(viz.RED)

# BLUE CUBE
blueCube = vizshape.addCube()
blueCube.setScale([0.2, 0.2, 0.2])
blueCube.setPosition([-4.63, 1.55, 2.6])
blueCube.color(viz.BLUE)

# GREEN CUBE
greenCube = vizshape.addCube()
greenCube.setScale([0.2, 0.2, 0.2])
greenCube.setPosition([-4.63, 0.65, 0])
greenCube.color(viz.GREEN)

# ORANGE CUBE
orangeCube = vizshape.addCube()
orangeCube.setScale([0.2, 0.2, 0.2])
orangeCube.setPosition([-4.63, 2, -0.2])
orangeCube.color(viz.ORANGE)

# BLACK CUBE
blackCube = vizshape.addCube()
blackCube.setScale([0.2, 0.2, 0.2])
blackCube.setPosition([-4.63, 0.22, -2.3])
blackCube.color(viz.BLACK)

# PURPLE CUBE
purpleCube = vizshape.addCube()
purpleCube.setScale([0.2, 0.2, 0.2])
purpleCube.setPosition([-4.63, 1.55, -2.8])
purpleCube.color(viz.PURPLE)
'''''''''END OF RIGHT WALL -- KNAPSACK PROBLEM'''''''''




# Create Wall 1 with door
# The wall consists of three parts, left of the door, above the door, and right of the door
# Alternatively door could be overlaid on a singular instance of the wall, however this gives the option to have 
	# an event derender the door and create an openning to pass to another room

if isDoor: 
	door = viz.addTexQuad()
	door.setScale([1.5,2.5,1])
	door.setPosition([0,1.25,5])
	doorCover = viz.addTexture('CustomImages/door.jpg')
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
wallCover = viz.addTexture('CustomImages/concreteWall.jpg')
ceilingCover = viz.addTexture('images/tile_slate.jpg')
floorCover = viz.addTexture('CustomImages/wood.jpg')


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
lineStart = [0,3,0]
lineEnd = [1,0.1,-2]
line = drawLine(lineStart, lineEnd)

# Testing
#selected = viz.Intersect(lineStart, lineEnd)
#checkHover(lineStart, lineEnd)

'''light = viz.addLight()
light.color(viz.BLUE)
light.setPosition(0, 3, 0)
light.intensity(100)'''

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

andGateTex = viz.addTexture("AndGate.png")
orGateTex = viz.addTexture("OrGate.png")
xorGateTex = viz.addTexture("XorGate.png")
notGateTex = viz.addTexture("NotGate.png")
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
	
mushroom = viz.addAvatar('Martial_arts_character.osgb')
vizact.onkeydown('3', moveMushroom)
mushroom.setScale([0.5, 0.5, 0.5])
mushroom.setPosition([4.5, 1, 0])
mushroom.setEuler(90,0,0)