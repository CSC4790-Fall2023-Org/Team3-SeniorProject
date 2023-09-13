import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

#viz.setMultiSample(4)
viz.fov(60)
viz.go()

# Set up room and put up walls
room = viz.addChild('lab.osgb')

# Create Wall 1 with door
# The wall consists of three parts, left of the door, above the door, and right of the door
# Alternatively door could be overlaid on a singular instance of the wall, however this gives the option to have 
	# an event derender the door and create an openning to pass to another room

# Add door

door = viz.addTexQuad()
door.setScale([1.5,3,1])
door.setPosition([0,1.5,5])


# Fill in wall around door
wallOneLeft = viz.addTexQuad()
wallOneRight = viz.addTexQuad()
wallOneAbove = viz.addTexQuad()

wallOneLeft.setPosition([-2.875,2.5,5])
wallOneRight.setPosition([2.875,2.5,5])
wallOneAbove.setPosition([0,4,5])

wallOneLeft.setScale([4.25,5,1])
wallOneRight.setScale([4.25,5,1])
wallOneAbove.setScale([1.5,2,1])

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
ceiling.setPosition([0,5,0])
ceiling.setEuler([0,90,0])
ceiling.setScale([10,10,10])
floor = viz.addTexQuad()
floor.setPosition([0,0.001,0])
floor.setEuler([0,90,0])
floor.setScale([10,10,10])


# Create textures
wallCover = viz.addTexture('images/tile_slate.jpg')
floorCover = viz.addTexture('CustomImages/wood.jpg')
doorCover = viz.addTexture('CustomImages/door.jpg')

# Cover walls with texture

wallOneLeft.texture(wallCover)
wallOneRight.texture(wallCover)
wallOneAbove.texture(wallCover)
wallTwo.texture(wallCover)
wallThree.texture(wallCover)
wallFour.texture(wallCover)
ceiling.texture(wallCover)

# Cover floor with texture
floor.texture(floorCover)

# Cover door with texture
door.texture(doorCover)

viz.MainView.collision(viz.ON)