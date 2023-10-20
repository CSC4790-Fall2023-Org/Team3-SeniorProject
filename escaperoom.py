import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
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
	viz.phys.enable()
	

#variable for toggling door
isDoor = True

# Set up room and put up walls
room = viz.addChild('lab.osgb')


table = viz.addChild('CustomModels/table1.osgb')
table.collidePlane()
table.disable(viz.DYNAMICS)
table.setScale([0.01, 0.0125, 0.01])
table.setPosition([4.5, 0, 0])
table.setEuler(90, 0, 0)



'''''''''RIGHT WALL -- KNAPSACK PROBLEM'''''''''
# Left Box
leftBox = vizshape.addCube()
leftBox.collideMesh()
leftBox.setScale([1, 1.75, 1])
leftBox.setPosition([-4.7, 0, -2])
leftBox.color(viz.BLACK)
leftBox.disable(viz.DYNAMICS)

# Middle Box
middleBox = vizshape.addCube()
middleBox.collideMesh()
middleBox.setScale([1, 1.75, 1])
middleBox.setPosition([-4.7, 0, 0.5])
middleBox.color(viz.BLACK)
middleBox.disable(viz.DYNAMICS)

# Right Box
rightBox = vizshape.addCube()
rightBox.collideMesh()
rightBox.setScale([1, 1.75, 1])
rightBox.setPosition([-4.7, 0, 3])
rightBox.color(viz.BLACK)
rightBox.disable(viz.DYNAMICS)


# RED CUBE
redCube = vizshape.addCube()
redCube.collideBox()
redCube.setScale([0.2, 0.2, 0.2])
redCube.setPosition([-4.7, 1.2, 3])
redCube.color(viz.RED)

# BLUE CUBE
blueCube = vizshape.addCube()
blueCube.collideBox()
blueCube.setScale([0.2, 0.2, 0.2])
blueCube.setPosition([-4.7, 1.2, 0.5])
blueCube.color(viz.BLUE)

# GREEN CUBE
greenCube = vizshape.addCube()
greenCube.collideBox()
greenCube.setScale([0.2, 0.2, 0.2])
greenCube.setPosition([-4.7, 1.2, -2])
greenCube.color(viz.GREEN)

'''
# ORANGE CUBE
orangeCube = vizshape.addCube()
orangeCube.setScale([0.2, 0.2, 0.2])
orangeCube.setPosition([-4.83, 2.02, -0.2])
orangeCube.color(viz.ORANGE)

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
checkHover(lineStart, lineEnd)

viz.MainView.lookAt(table.getPosition())