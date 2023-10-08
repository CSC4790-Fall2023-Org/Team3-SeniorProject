import viz

def drawLine(p1, p2, pointSize=10, color=viz.WHITE):
	viz.startLayer(viz.LINES)
	viz.pointSize(pointSize)
	viz.vertexColor(color)
	viz.vertex(p1)
	viz.vertex(p2)
	return viz.endLayer()
	
def checkHover(parent, lineStart, lineEnd):	
	hovered = viz.intersect(lineStart, lineEnd)
	#if hovered.valid:
		#hovered.object.color(viz.BLUE)
		#hovered.object.setParent(parent)