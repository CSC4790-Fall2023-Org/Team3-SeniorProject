import viz
import viztask
import vizact
import vizinfo
import vizmat
import vizproximity
import vizshape
import vizfx
import tools
import time
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
 
#Add table
#table = viz.addChild('CustomModels/table1.osgb')
#table.setScale([0.01, 0.0125, 0.01])
#table.setPosition([4.5, 0, 0])
#table.setEuler(90, 0, 0)

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

pillar1 = vizshape.addCylinder()
pillar1.collideBox(0.5, 1, 0.5)
pillar1.setScale([0.5, 1, 0.5])
pillar1.setPosition([-4.5, 2, -3])

pillar2 = vizshape.addCylinder()
pillar2.collideBox(0.5, 1, 0.5)
pillar2.setScale([0.5, 1, 0.5])
pillar2.setPosition([-4.5, 2, -1.5])

pillar3 = vizshape.addCylinder()
pillar3.collideBox(0.5, 1, 0.5)
pillar3.setScale([0.5, 1, 0.5])
pillar3.setPosition([-4.5, 2, -0])

pillar4 = vizshape.addCylinder()
pillar4.collideBox(0.5, 1, 0.5)
pillar4.setScale([0.5, 1, 0.5])
pillar4.setPosition([-4.5, 2, 1.5])

pillar5 = vizshape.addCylinder()
pillar5.collideBox(0.5, 1, 0.5)
pillar5.setScale([0.5, 1, 0.5])
pillar5.setPosition([-4.5, 2, 3])


# RED CUBE
redCube = vizshape.addCube()
redCube.collideBox(0.15,0.15,0.15)
redCube.setScale([0.15, 0.15, 0.15])
redCube.setPosition([-4.5, 3, -3])
redCube.color(viz.RED)
redCube.density = 2
redCube.label = '0110'

# BLUE CUBE
blueCube = vizshape.addCube()
blueCube.collideBox(0.15,0.15,0.15)
blueCube.setScale([0.15, 0.15, 0.15])
blueCube.setPosition([-4.5, 3, -1.5])
blueCube.color(viz.BLUE)
blueCube.density = 3
blueCube.label = '0101'

# GREEN CUBE
greenCube = vizshape.addCube()
greenCube.collideBox(0.15,0.15,0.15)
greenCube.setScale([0.15, 0.15, 0.15])
greenCube.setPosition([-4.5, 3, 0])
#greenCube.setPosition([-2, 3, 4.4])
greenCube.color(viz.GREEN)
greenCube.density = 4
greenCube.label = '1010'

# ORANGE CUBE
orangeCube = vizshape.addCube()
orangeCube.collideBox(0.15,0.15,0.15)
orangeCube.setScale([0.15, 0.15, 0.15])
orangeCube.setPosition([-4.5, 3, 1.5])
orangeCube.color(viz.ORANGE)
orangeCube.density = 1
orangeCube.label = '0011'

# BLACK CUBE
blackCube = vizshape.addCube()
blackCube.collideBox(0.15,0.15,0.15)
blackCube.setScale([0.15, 0.15, 0.15])
blackCube.setPosition([-4.5, 3, 3])
blackCube.color(viz.BLACK)
blackCube.density = 5
blackCube.label = '1100'


# PURPLE CUBE
purpleCube = vizshape.addCube()
purpleCube.collideBox(0.15,0.15,0.15)
purpleCube.setScale([0.15, 0.15, 0.15])
purpleCube.setPosition([3.75, 2, -4.4])
purpleCube.color(viz.PURPLE)
purpleCube.density = 2
purpleCube.label = '0111'

densityDisplay = viz.addText('',pos = [0, 0, 0])
densityDisplay.setScale([0.25,0.25,0.25])
densityDisplay.setEuler([-90,0,0])
densityDisplay.color(viz.BLACK)
densityDisplay.alignment(viz.ALIGN_CENTER_BOTTOM)

def printWeight():
    object = viz.pick()
    if object.valid() and (object in [redCube, blueCube, greenCube, orangeCube, blackCube, purpleCube]):
        objPos = object.getPosition()
        objPos[1] += .3
        
        densityDisplay.setPosition(objPos)
        densityDisplay.message('Weight: ' + str(object.density) + '\nValue: ' + str(object.label))
    
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT, printWeight)

# Add knapsack table
knapsackTable = vizshape.addCube()
knapsackTable.setPosition([-2, .5, 4.4])
knapsackTable.setScale([1.6, 1, 1])
knapsackTable.collideBox(1.6, 1, 1)

def checkKnapsack():
	redPos = redCube.getPosition()
	orangePos = orangeCube.getPosition() # yellow cube
	greenPos = greenCube.getPosition()
	bluePos = blueCube.getPosition()
	purplePos = purpleCube.getPosition()
	blackPos = blackCube.getPosition()
	
	# Helper function to see if a position is within the bounds of our table
	def onTable(position):
		#If X is off to the left or right, return false
		if(position[0] < -2.75 or position[0] > -1.25):
			return False
		#If Z is too far forward or back, return false
		if(position[2] < 3.95 or position[2] > 4.85):
			return False
			
		#Fix this bottom part to make sure that it has to be on the surface! (or at least close enough)
		#If Y is not on the table top itself (Can't just hover it over the table) return false
		if(position[1] > 2 or position[1] < 1):
			return False
		return True
		
	#If there's an incorrect block on the table, return False
	if(onTable(redPos) or onTable(orangePos) or onTable(bluePos) or onTable(blackPos)):
		return False
	#If the right pair of blocks is on the table and no others from above, return true
	if(onTable(greenPos) and onTable(purplePos)):
		return True
	#If you've reached here, you only have one correct block or no blocks on the table at all
	return False

#add knapsack out light
knapOutLight = vizshape.addSphere()
knapOutLight.setPosition(1,2.25,5)
knapOutLight.setScale(.25,.25,.25)
knapOutLight.label = False

def changeKnapLightColor():
	if checkKnapsack():
		knapOutLight.color(viz.YELLOW)
	else:
		knapOutLight.color(viz.WHITE)
vizact.onupdate(20, changeKnapLightColor)

'''''''''''''''END OF RIGHT WALL -- KNAPSACK PROBLEM'''''''''

# Create Wall 1 with door
# The wall consists of three parts, left of the door, above the door, and right of the door
# Alternatively door could be overlaid on a singular instance of the wall, however this gives the option to have 
	# an event derender the door and create an openning to pass to another room
	


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
floor.setPosition([0,0,0])
floor.setEuler([0,90,0])
floor.setScale([10,10,10])
floor.collidePlane()


wallOneLeft.collidePlane(0,1,0,0)
wallOneRight.collidePlane(0,1,0,0)
wallOneAbove.collidePlane(0,1,0,0)

wallTwo.collidePlane(0,1,0,0)
wallThree.collidePlane(0,1,0,0)
wallFour.collidePlane(0,1,0,0)

ceiling.collidePlane()

# ---------------------------------
# viz.INTERSECT must be turned off for all the room walls so we don't accidentally pick up the floor !!!
# ---------------------------------

# Add light source
light = viz.addLight()
light.enable()
light.position(0, 3.9, 0)
light.spread(180)
light.intensity(2)

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
slot1 = viz.addTexQuad()
slot2 = viz.addTexQuad()
slot3 = viz.addTexQuad()
slot4 = viz.addTexQuad()

slot1.setPosition([-1, 2, -4.9])
slot1.setScale([7,0.39,0.5])
slot1.setEuler([180,0,0])
slot2.setPosition([-1, 1.53, -4.9])
slot2.setScale([7,0.39,0.5])
slot2.setEuler([180,0,0])
slot3.setPosition([-1, 1.08, -4.9])
slot3.setScale([7,0.39,0.5])
slot3.setEuler([180,0,0])
slot4.setPosition([-1, 0.6, -4.9])
slot4.setScale([7,0.39,0.5])
slot4.setEuler([180,0,0])

box1 = vizshape.addBox(splitFaces=True)
box2 = vizshape.addBox(splitFaces=True)
box3 = vizshape.addBox(splitFaces=True)
box4 = vizshape.addBox(splitFaces=True)

box1.setPosition([1,1,-2])
box2.setPosition([1,1,2])
box3.setPosition([-2,1,-2])
box4.setPosition([-2,1,2])

box1.setScale([0.5,0.5,0.5])
box2.setScale([0.5,0.5,0.5])
box3.setScale([0.5,0.5,0.5])
box4.setScale([0.5,0.5,0.5])

box1.color(viz.BLACK)
box2.color(viz.BLACK)
box3.color(viz.BLACK)
box4.color(viz.BLACK)

box1.collideBox([0.5,0.5,0.5])
box2.collideBox([0.5,0.5,0.5])
box3.collideBox([0.5,0.5,0.5])
box4.collideBox([0.5,0.5,0.5])

init = viz.addTexture('CustomImages/codeSolutions/init.jpg')
sol1 = viz.addTexture('CustomImages/codeSolutions/sol1.jpg')
sol2 = viz.addTexture('CustomImages/codeSolutions/sol2.jpg')
sol3 = viz.addTexture('CustomImages/codeSolutions/sol3.jpg')

box1.color(5,5,5)
box1.texture(init)
box2.color(5,5,5)
box2.texture(sol1)
box3.color(5,5,5)
box3.texture(sol2)
box4.color(5,5,5)
box4.texture(sol3)

createProblem()

box1Placed = False
box2Placed = False
box3Placed = False
box4Placed = False

def checkBox1Position():
	global box1Placed
	box1Position = box1.getPosition()
	if box1Position[0] > -4 and box1Position[0] < 2:
		if box1Position[1] > 1.8 and box1Position[1] < 2.4:
			if box1Position[2] < -4.6:
				slot1.texture(init)
				if isCave:
					box1.remove()
				box1Placed = True
				
def checkBox2Position():
	global box2Placed
	box2Position = box2.getPosition()
	if box2Position[0] > -4 and box2Position[0] < 2:
		if box2Position[1] > 1.33 and box2Position[1] < 1.83:
			if box2Position[2] < -4.6:
				slot2.texture(sol1)
				if isCave:
					box2.remove()
				box2Placed = True
				
def checkBox3Position():
	global box3Placed
	box3Position = box3.getPosition()
	if box3Position[0] > -4 and box3Position[0] < 2:
		if box3Position[1] > 0.88 and box3Position[1] < 1.28:
			if box3Position[2] < -4.6:
				slot3.texture(sol2)
				if isCave:
					box3.remove()
				box3Placed = True
				
def checkBox4Position():
	global box4Placed
	box4Position = box4.getPosition()
	if box4Position[0] > -4 and box4Position[0] < 2:
		if box4Position[1] < 0.8:
			if box4Position[2] < -4.6:
				slot4.texture(sol3)
				if isCave:
					box4.remove()
				box4Placed = True
				
forOutLight = vizshape.addSphere()
forOutLight.setPosition(1,0.75,5)
forOutLight.setScale(.25,.25,.25)
forOutLight.label = False

def checkFor():
	if box1Placed is True and box2Placed is True and box3Placed is True and box4Placed is True:
		return True
	else:
		return False

# Add callbacks
if not box1Placed: vizact.onupdate(15, checkBox1Position)
if not box2Placed: vizact.onupdate(16, checkBox2Position)
if not box3Placed: vizact.onupdate(17, checkBox3Position)
if not box4Placed: vizact.onupdate(18, checkBox4Position)

def changeForLightColor():
	print(box1Placed)
	if checkFor():
		forOutLight.color(viz.YELLOW)
	else:
		forOutLight.color(viz.WHITE)
vizact.onupdate(20, changeForLightColor)

light = viz.addLight()
light.color(viz.WHITE)
light.setPosition(0, 3, 0)
light.intensity(100)

objects = [box1, box2, box3, box4, redCube, blueCube, greenCube, orangeCube, blackCube, purpleCube]
objectHeld = False

def updateMouseGrabber(tool):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        tool.grabAndHold()

def localPositionCallback(item, boxNum):
	itemPos = item.getPosition()
	if boxNum == 1:
		if box1Placed:
			box1.setPosition([10, 10, 10])
	elif boxNum == 2:
		if box2Placed:
			box2.setPosition([-10, 10, -10])
	elif boxNum == 3:
		if box3Placed:
			box3.setPosition([10, 10, -10])
	elif boxNum == 4:
		if box4Placed:
			box4.setPosition([-10, 10, 10])
		

# 0 is box
# 1 is cube
# 2 is gate
def positionCallback(item, itemType, gateArray = 0):
	global objectHeld
	
	userPosition = viz.MainView.getPosition()
	userDirection = viz.MainView.getMatrix().getForward()
	interactionDot = vizmat.MoveAlongVector(userPosition, userDirection, 2)
	yEuler = -1 * joystickTracker.getEuler()[1]
	dotPos = [interactionDot[0], interactionDot[1] * (yEuler/30) + 1, interactionDot[2]]
	dot.setPosition(dotPos)
	itemPosition = item.getPosition()
	if dotPos[0] > itemPosition[0] - 0.3 and dotPos[0] < itemPosition[0] + 0.3:
		if dotPos[1] > itemPosition[1] - 0.3 and dotPos[1] < itemPosition[1] + 0.3:
			if dotPos[2] > itemPosition[2] - 0.3 and dotPos[2] < itemPosition[2] + 0.3:
				#dot.color(3,3,3)
				rawInput = vizconnect.getConfiguration().getRawDict("input")['flystick']
				if itemType != 2: # boxes and cubes
					if rawInput.isButtonDown(0) and not objectHeld:
						objectHeld = True
						item.setPosition(dotPos)
						item.collideNone()
					else:
						objectHeld = False
						#dot.color(0,0,0)
						if itemType == 0:
							item.collideBox([0.5,0.5,0.5])
						elif itemType == 1:
							item.collideBox([0.15,0.15,0.15])
				else: # gates
					if rawInput.isButtonDown(0):
						print("gate check")
						time.sleep(0.2)
						changeTexture(gateArray)
	elif itemPos[0] > 5 or itemPos[0] < -5 or itemPos[2] > 5 or itemPos[2] < -5:
		item.setPosition([0, 2, 0])
						

'''''''''''''''''''''''''''''LOGIC GATE PROBLEM'''''''''''''''''''''''''''''''''
def changeTexture(gateArr): #Add the Not gate stuff and encode it in a different way
	global gate1
	global gate2
	global gate3
	global gate4
	global gate5
	global NotGate
	if gateArr[1] == 4:
		gateArr[1] = 5
		gateArr[0].texture(blankGateTex)
	elif gateArr[1] == 5:
		gateArr[1] = 4
		gateArr[0].texture(notGateTex)
	else:
		gateArr[1] = (gateArr[1] + 1) % 3
		gateArr[0].texture(gateTextures[gateArr[1]])
		
	wire6[1] = GateOutput(gate1[1], gate1[2], gate1[3])
	wire7[1] = GateOutput(gate2[1], gate2[2], gate2[3])
	wire8[1] = wire6[1]
	gate3[2] = wire8[1]
	wire9[1] = wire7[1]
	wire10[1] = wire5[1]
	gate4[2], gate4[3] = wire9[1], wire10[1]
	wire11[1] = NotGate(gate3[1], gate3[2])
	wire12[1] = GateOutput(gate4[1], gate4[2], gate4[3])
	gate5[2], gate5[3] = wire11[1], wire12[1]
	wire13[1] = GateOutput(gate5[1], gate5[2], gate5[3])
	logicOutlight1[1] = wire13[1]
	logicOutlight2[1] = wire13[1]
	
	objColor(wire6[0], wire6[1])
	objColor(wire7[0], wire7[1])
	objColor(wire8[0], wire8[1])
	objColor(wire9[0], wire9[1])
	objColor(wire10[0], wire10[1])
	objColor(wire11[0], wire11[1])
	objColor(wire12[0], wire12[1])
	objColor(wire13[0], wire13[1])
	objColor(logicOutlight1[0], logicOutlight1[1])
	objColor(logicOutlight2[0], logicOutlight2[1])

def NotGate(c, i):
	if c == 4:
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
blankGateTex = viz.addTexture("CustomTextures/logic-symbols/blankGate.jpg")
gateTextures = [andGateTex, orGateTex, xorGateTex]

light1 = [vizshape.addSphere(), False]
light1[0].setPosition(5,2.25,-2.5)
light1[0].setScale(.25,.25,.25)
objColor(light1[0], light1[1])

light2 = [vizshape.addSphere(), True]
light2[0].setPosition(5,1.75,-2.5)
light2[0].setScale(.25,.25,.25)
objColor(light2[0], light2[1])

light3 = [vizshape.addSphere(), True]
light3[0].setPosition(5,1.25,-2.5)
light3[0].setScale(.25,.25,.25)
objColor(light3[0], light3[1])

light4 = [vizshape.addSphere(), True]
light4[0].setPosition(5,0.75,-2.5)
light4[0].setScale(.25,.25,.25)
objColor(light4[0], light4[1])

light5 = [vizshape.addSphere(), False]
light5[0].setPosition(5,0.25,-2.5)
light5[0].setScale(.25,.25,.25)
objColor(light5[0], light5[1])

wire1 = [vizshape.addCylinder(), light1[1]] #[object, boolVal]
wire1[0].setPosition(5,2.25,-2)
wire1[0].setScale(.1,1,.1)
wire1[0].setEuler([0,90,0])
objColor(wire1[0], wire1[1])

wire2 = [vizshape.addCylinder(), light2[1]]
wire2[0].setPosition(5,1.75,-2)
wire2[0].setScale(.1,1,.1)
wire2[0].setEuler([0,90,0])
objColor(wire2[0], wire2[1])

wire3 = [vizshape.addCylinder(), light3[1]]
wire3[0].setPosition(5,1.25,-2)
wire3[0].setScale(.1,1,.1)
wire3[0].setEuler([0,90,0])
objColor(wire3[0], wire3[1])

wire4 = [vizshape.addCylinder(), light4[1]]
wire4[0].setPosition(5,0.75,-2)
wire4[0].setScale(.1,1,.1)
wire4[0].setEuler([0,90,0])
objColor(wire4[0], wire4[1])

wire5 = [vizshape.addCylinder(), light5[1]]
wire5[0].setPosition(5,0.25,-1)
wire5[0].setScale(.1,2.5,.1)
wire5[0].setEuler([0,90,0])
objColor(wire5[0], wire5[1])

gate1 = [viz.addTexQuad(), 0, wire1[1], wire2[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate1[0].setPosition([4.9,2,-1.25])
gate1[0].setScale(0.75,0.75,0.75)
gate1[0].setEuler([90,0,180])
gate1[0].texture(gateTextures[gate1[1]])

wire6 = [vizshape.addCylinder(), GateOutput(gate1[1], gate1[2], gate1[3])]
wire6[0].setPosition(5,2,-.5)
wire6[0].setScale(.1,1,.1)
wire6[0].setEuler([0,90,0])
objColor(wire6[0], wire6[1])

gate2 = [viz.addTexQuad(), 2, wire3[1], wire4[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate2[0].setPosition([4.9,1,-1.25])
gate2[0].setScale(0.75,0.75,0.75)
gate2[0].setEuler([90,0,180])
gate2[0].texture(gateTextures[gate1[2]])

wire7 = [vizshape.addCylinder(), GateOutput(gate2[1], gate2[2], gate2[3])]
wire7[0].setPosition(5,1,-.5)
wire7[0].setScale(.1,1,.1)
wire7[0].setEuler([0,90,0])
objColor(wire7[0], wire7[1])

#WIRE 8, 9 AND 10 ARE NOT NEEDED BUT I DIDNT WANT TO DELETE THEM SO THE LOGIC WOULDNT GET MESSED UP
wire8 = [vizshape.addCylinder(), wire6[1]]
wire8[0].setPosition(10,10,10)
wire8[0].setScale(.1,1,.1)
wire8[0].setEuler([90,90,0])
objColor(wire8[0], wire8[1])

wire9 = [vizshape.addCylinder(), wire7[1]]
wire9[0].setPosition(10,10,10)
wire9[0].setScale(.1,1,.1)
wire9[0].setEuler([90,90,0])
objColor(wire9[0], wire9[1])

wire10 = [vizshape.addCylinder(), wire5[1]]
wire10[0].setPosition(10,10,10)
wire10[0].setScale(.1,1,.1)
wire10[0].setEuler([90,90,0])
objColor(wire10[0], wire10[1])
#END OF USELESS STUFF

gate3 = [viz.addTexQuad(), 4, wire8[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate3[0].setPosition([4.9,2,.25])
gate3[0].setScale(0.75,0.75,0.75)
gate3[0].setEuler([90,0,180])
gate3[0].texture(notGateTex)

gate4 = [viz.addTexQuad(), 0, wire9[1], wire10[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate4[0].setPosition([4.9,.6,.25])
gate4[0].setScale(0.75,0.75,0.75)
gate4[0].setEuler([90,0,180])
gate4[0].texture(gateTextures[gate4[1]])

wire11 = [vizshape.addCylinder(), NotGate(gate3[1], gate3[2])]
wire11[0].setPosition(5,1.75,1)
wire11[0].setScale(.1,1,.1)
wire11[0].setEuler([0,125,0])
objColor(wire11[0], wire11[1])

wire12 = [vizshape.addCylinder(), GateOutput(gate4[1], gate4[2], gate4[3])]
wire12[0].setPosition(5,0.6,1)
wire12[0].setScale(.1,1,.1)
wire12[0].setEuler([0,90,0])
objColor(wire12[0], wire12[1])

gate5 = [viz.addTexQuad(), 0, wire11[1], wire12[1]] #[object, what gate its on (and, or, xor), input wire val, input wire val]
gate5[0].setPosition([4.9,1,1.75])
gate5[0].setScale(0.75,0.75,0.75)
gate5[0].setEuler([90,0,180])
gate5[0].texture(gateTextures[gate5[1]])

wire13 = [vizshape.addCylinder(), GateOutput(gate5[1], gate5[2], gate5[3])]
wire13[0].setPosition(5,1,2.25)
wire13[0].setScale(.1,0.5,.1)
wire13[0].setEuler([0,90,0])
objColor(wire13[0], wire13[1])

logicOutlight1 = [vizshape.addSphere(), wire13[1]]
logicOutlight1[0].setPosition(5,1,2.75)
logicOutlight1[0].setScale(.25,.25,.25)
objColor(logicOutlight1[0], logicOutlight1[1])

logicOutlight2 = [vizshape.addSphere(), wire13[1]]
logicOutlight2[0].setPosition(1,1.5,5)
logicOutlight2[0].setScale(.25,.25,.25)
objColor(logicOutlight2[0], logicOutlight2[1])

vizact.onkeydown('5', changeTexture, gate1)
vizact.onkeydown('6', changeTexture, gate2)
vizact.onkeydown('7', changeTexture, gate3)
vizact.onkeydown('8', changeTexture, gate4)
vizact.onkeydown('9', changeTexture, gate5)

viz.fov(80)
if isCave:
	import vizconnect
	CONFIG_FILE = "vizconnect_config_CaveFloor+ART_headnode.py"
	vizconnect.go(CONFIG_FILE)	
	dtrack_manager = MyDtrackManager()
	dtrack_manager.startDefaultHeadPosition()
	joystickTracker = vizconnect.getTracker("dtrack_flystick")

	dot = vizshape.addSphere()
	dot.setScale([0.1, 0.1, 0.1])

	vizact.onupdate(0, positionCallback, box1, 0)
	vizact.onupdate(1, positionCallback, box2, 0)
	vizact.onupdate(2, positionCallback, box3, 0)
	vizact.onupdate(3, positionCallback, box4, 0)
	vizact.onupdate(4, positionCallback, redCube, 1)
	vizact.onupdate(5, positionCallback, greenCube, 1)
	vizact.onupdate(6, positionCallback, blackCube, 1)
	vizact.onupdate(7, positionCallback, orangeCube, 1)
	vizact.onupdate(8, positionCallback, blueCube, 1)
	vizact.onupdate(9, positionCallback, purpleCube, 1)
	vizact.onupdate(10, positionCallback, gate1[0], 2, gate1)
	vizact.onupdate(11, positionCallback, gate2[0], 2, gate2)
	vizact.onupdate(12, positionCallback, gate3[0], 2, gate3)
	vizact.onupdate(13, positionCallback, gate4[0], 2, gate4)
	vizact.onupdate(14, positionCallback, gate5[0], 2, gate5)
	
	viz.MainView.collision(viz.ON)
	
else:
	from vizconnect.util import virtual_trackers
	usingPhysics=False
	from tools import grabber
	from tools import highlighter
	tool = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_OUTLINE)
	tool.setItems(objects)
	mouseTracker = virtual_trackers.ScrollWheel(followMouse = True)
	mouseTracker.distance = 3
	arrow = vizshape.addArrow(length=0.2,color=viz.BLUE)
	arrowLink = viz.link(mouseTracker, arrow)
	arrowLink.postMultLinkable(viz.MainView)
	viz.link(arrowLink,tool)
	tool.setUpdateFunction(updateMouseGrabber)
	
	vizact.onupdate(5, localPositionCallback, box1, 1)
	vizact.onupdate(6, localPositionCallback, box2, 2)
	vizact.onupdate(7, localPositionCallback, box3, 3)
	vizact.onupdate(8, localPositionCallback, box4, 4)
	
	viz.go()
	viz.MainView.collision(viz.ON)			

def moveMushroom():
	move = vizact.animation(2)
	mushroom.addAction(move)	
	
mushroom = viz.addAvatar('CustomModels/MushroomMan/Martial_arts_character.osgb')
vizact.onkeydown('3', moveMushroom)
mushroom.setScale([0.5, 0.5, 0.5])
mushroom.setPosition([0, 0, 10])
mushroom.setEuler(0,0,0)

#Checking all lights to open door
door = viz.addTexQuad()
door.setScale([1.5,2.5,1])
door.setPosition([0,1.25,5])
doorCover = viz.addTexture('CustomTextures/door.jpg')
door.texture(doorCover)
door.remove()

#Red Carpet
carpet = viz.addTexQuad()
carpet.setPosition([0,0,10])
carpet.setEuler([0,90,0])
carpet.setScale([4,10,10])
carpet.collidePlane()
carpetTex = viz.addTexture('CustomTextures/redCarpet.jpg')
carpet.texture(carpetTex)

def checkLights():
	global door
	if checkKnapsack() and logicOutlight1[1]:
		if box1Placed is True and box2Placed is True and box3Placed is True and box4Placed is True:
			door.remove()
			moveMushroom()
	

vizact.onupdate(23, checkLights)


knapValuesTex = viz.addTexture('CustomImages/KnapValuesVisual.jpg')
knapValues = viz.addTexQuad()
knapValues.texture(knapValuesTex)
knapValues.setScale([2, 1.5, 1.5])
knapValues.setPosition([-4.95,2.5,-1.5])
knapValues.setEuler([270, 0, 0])

knapWeightsTex = viz.addTexture('CustomImages/KnapWeightsVisual.jpg')
knapWeights = viz.addTexQuad()
knapWeights.texture(knapWeightsTex)
knapWeights.setScale([2, 1.5, 1.5])
knapWeights.setPosition([-4.95,2.5,1.5])
knapWeights.setEuler([270, 0, 0])

knapLimitTex = viz.addTexture('CustomImages/KnapLimitVisual.jpg')
knapValues = viz.addTexQuad()
knapValues.texture(knapLimitTex)
knapValues.setScale([1.4, 1.1, 1.1])
knapValues.setPosition([-2,2.1,4.95])
knapValues.setEuler([0, 0, 270])
