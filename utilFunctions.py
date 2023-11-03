import viz
import vizconnect
import vizmat

def drawLine(p1, p2, pointSize=10, color=viz.WHITE):
	viz.startLayer(viz.LINES)
	viz.pointSize(pointSize)
	viz.vertexColor(color)
	viz.vertex(p1)
	viz.vertex(p2)
	return viz.endLayer()
	
def checkHover(joystickTracker):
	lineStart = joystickTracker.getPosition()
	direction = joystickTracker.getMatrix().getForward()
	lineEnd = vizmat.MoveAlongVector(lineStart, direction, 30)
	hovered = viz.intersect(lineStart, lineEnd)
	
	if hovered.valid:
		hovered.object.color(viz.BLUE)
		
#def setParent(parent, lineStart, lineEnd):
#	hovered = viz.intersect(lineStart, lineEnd)
#	if hovered.valid:
#		hovered.object.setParent(parent)	

line = None
lineStart = None
lineEnd = None

def drawJoystickLine(joystickTracker):
	global line
	global lineStart
	global lineEnd
	
	if line is not None:
		line.remove()
	lineStart = joystickTracker.getPosition()
	direction = joystickTracker.getMatrix().getForward()
	lineEnd = vizmat.MoveAlongVector(lineStart, direction, 50)
	line = drawLine(lineStart, lineEnd)
	
def triggerCheck(joystickTracker):
	global lineStart
	global lineEnd
	global line
	
	if checkPress(trigger):
		hovered = viz.intersect(lineStart, lineEnd)
		if hovered.valid:
			hovered.object.setParent(line)