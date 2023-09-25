import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

def createProblem():
	
	# Create and place code slots
	slot1 = viz.addTexQuad()
	slot2 = viz.addTexQuad()
	slot3 = viz.addTexQuad()
	slot4 = viz.addTexQuad()
	
	slot1.setPosition([-1, 3.4, -4.9])
	slot1.setScale([7,0.6,0.5])
	slot2.setPosition([-1, 2.6, -4.9])
	slot2.setScale([7,0.6,0.5])
	slot3.setPosition([-1, 1.8, -4.9])
	slot3.setScale([7,0.6,0.5])
	slot4.setPosition([-1, 1, -4.9])
	slot4.setScale([7,0.6,0.5])
	
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
	
def spawnCodeBoxes():
	# Create and place boxes
	return
	
# def 