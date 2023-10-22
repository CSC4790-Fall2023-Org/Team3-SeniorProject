import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

def __init__(self, normal, node, name, node_path, name_path):
	self.normal
	
def createProblem():
	
	# Create and place code slots
	global slot1
	global slot2
	global slot3
	global slot4
	slot1 = viz.addTexQuad()
	slot2 = viz.addTexQuad()
	slot3 = viz.addTexQuad()
	slot4 = viz.addTexQuad()
	
	slot1.setPosition([-1, 3.4, -4.9])
	slot1.setScale([7,0.6,0.5])
	slot1.setEuler([180,0,0])
	slot2.setPosition([-1, 2.6, -4.9])
	slot2.setScale([7,0.6,0.5])
	slot2.setEuler([180,0,0])
	slot3.setPosition([-1, 1.8, -4.9])
	slot3.setScale([7,0.6,0.5])
	slot3.setEuler([180,0,0])
	slot4.setPosition([-1, 1, -4.9])
	slot4.setScale([7,0.6,0.5])
	slot4.setEuler([180,0,0])
	
	# Create chest
	wallBack = viz.addTexQuad()
	wallLeft = viz.addTexQuad()
	wallRight = viz.addTexQuad()
	wallFront = viz.addTexQuad()
	lid = viz.addTexQuad()
	
	wallBack.setPosition([3.6, 0, -4.8])
	wallBack.setScale([2, 1.5, 1.5])
	wallLeft.setPosition([4.6, 0, -4.3])
	wallLeft.setScale([1, 1.5, 1.5])
	wallLeft.setEuler([90, 0, 0])
	wallRight.setPosition([2.6, 0, -4.3])
	wallRight.setScale([1, 1.5, 1.5])
	wallRight.setEuler([90, 0, 0])
	wallFront.setPosition([3.6, 0, -3.8])
	wallFront.setScale([2, 1.5, 1.5])
	lid.setPosition([3.6, 0.75, -4.3])
	lid.setScale([2, 1, 1.5])
	lid.setEuler([0, 90, 0])
	
	return

box1 = vizshape.addBox(splitFaces=True)
box2 = vizshape.addBox(splitFaces=True)
box3 = vizshape.addBox(splitFaces=True)
box4 = vizshape.addBox(splitFaces=True)

def spawnCodeBoxes():
	
	global box1
	global box2
	global box3
	global box4
	
	box1.setPosition([1,0.1,-2])
	box2.setPosition([1,0.1,2])
	box3.setPosition([-2,0.1,-2])
	box4.setPosition([-2,0.1,2])
	
	box1.color(viz.BLACK)
	box2.color(viz.BLACK)
	box3.color(viz.BLACK)
	box4.color(viz.BLACK)
	
	return
	
def setTextures():
	
	global box1
	global box2
	global box3
	global box4
	
	newBox = vizshape.addBox(splitFaces=True)
	
	init = viz.addTexture('CustomImages/codeSolutions/init.jpg')
	sol1 = viz.addTexture('CustomImages/codeSolutions/sol1.jpg')
	sol2 = viz.addTexture('CustomImages/codeSolutions/sol2.jpg')
	sol3 = viz.addTexture('CustomImages/codeSolutions/sol3.jpg')
	
	slot1.texture(init)
	slot2.texture(sol1)
	slot3.texture(sol2)
	slot4.texture(sol3)
	
	box1.texture(init)
	box2.texture(sol1)
	box3.texture(sol2)
	box4.texture(sol3)