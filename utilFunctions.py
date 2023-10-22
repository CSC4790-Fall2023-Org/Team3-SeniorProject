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
		
def setParent(parent, lineStart, lineEnd):
	hovered = viz.intersect(lineStart, lineEnd)
	if hovered.valid:
		hovered.object.setParent(parent)	

line = None
def drawJoystickLine(joystickTracker):
	global line
	if line is not None:
		line.remove()
	lineStart = joystickTracker.getPosition()
	direction = joystickTracker.getMatrix().getForward()
	lineEnd = vizmat.MoveAlongVector(lineStart, direction, 50)
	line = drawLine(lineStart, lineEnd)