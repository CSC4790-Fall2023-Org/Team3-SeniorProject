import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

def __init__(self, normal, node, name, node_path, name_path):
	self.normal
	
#slot1 = viz.addTexQuad()
#slot2 = viz.addTexQuad()
#slot3 = viz.addTexQuad()
#slot4 = viz.addTexQuad()
	
def createProblem():
	
	# Create and place code slots and sensors
#	global slot1
#	global slot2
#	global slot3
#	global slot4
#	
#	slot1.setPosition([-1, 3.4, -4.9])
#	slot1.setScale([7,0.6,0.5])
#	slot1.setEuler([180,0,0])
#	slot2.setPosition([-1, 2.6, -4.9])
#	slot2.setScale([7,0.6,0.5])
#	slot2.setEuler([180,0,0])
#	slot3.setPosition([-1, 1.8, -4.9])
#	slot3.setScale([7,0.6,0.5])
#	slot3.setEuler([180,0,0])
#	slot4.setPosition([-1, 1, -4.9])
#	slot4.setScale([7,0.6,0.5])
#	slot4.setEuler([180,0,0])
	
	#slotSensor = vizproximity.Sensor(vizproximity.Box([8,6,2],center=[-1,2,-4.9]),source=plantMarker)
	
	# Create chest
	wallBack = viz.addTexQuad()
	wallLeft = viz.addTexQuad()
	wallRight = viz.addTexQuad()
	wallFront = viz.addTexQuad()
	lid = viz.addTexQuad()
	
	crateSide = viz.addTexture('CustomTextures/woodpanel.jpg')
	
	wallBack.setPosition([3.6, 0, -4.8])
	wallBack.setScale([2, 1.25, 1.5])
	wallBack.texture(crateSide)
	wallLeft.setPosition([4.6, 0, -4.3])
	wallLeft.setScale([1, 1.25, 1.5])
	wallLeft.setEuler([90, 0, 0])
	wallLeft.texture(crateSide)
	wallRight.setPosition([2.6, 0, -4.3])
	wallRight.setScale([1, 1.25, 1.5])
	wallRight.setEuler([90, 0, 0])
	wallRight.texture(crateSide)
	wallFront.setPosition([3.6, 0, -3.8])
	wallFront.setScale([2, 1.25, 1.5])
	wallFront.texture(crateSide)
	
	lid.setPosition([3.6, 0.625, -4.3])
	lid.setScale([2, 1, 1.5])
	lid.setEuler([0, 90, 0])
	lid.texture(crateSide)
	
	return

# Initialize boxes and prox sensors
#box1 = vizshape.addBox(splitFaces=True)
#box2 = vizshape.addBox(splitFaces=True)
#box3 = vizshape.addBox(splitFaces=True)
#box4 = vizshape.addBox(splitFaces=True)

