import viz
import vizconnect
import vizmat

def boxCallback(item):
	userPosition = viz.MainView.getPosition()
	itemPosition = item.getPosition()
	if userPosition[0] > itemPosition[0] - 1 and userPosition[0] > itemPosition[0] + 1:
		if userPosition[2] > itemPosition[2] - 1 and userPosition[2] > itemPosition[2] + 1:
			if joystickTracker.isButtonDown(0):
				tool.grabAndHold()
			
def cubeCallback(item):
	userPosition = viz.MainView.getPosition()
	itemPosition = item.getPosition()
	if userPosition[0] > itemPosition[0] - 0.5 and userPosition[0] > itemPosition[0] + 0.5:
		if userPosition[2] > itemPosition[2] - 0.5 and userPosition[2] > itemPosition[2] + 0.5:
			if joystickTracker.isButtonDown(0):
				tool.grabAndHold()