import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

#viz.setMultiSample(4)
viz.fov(80)
viz.go()

#variable for toggling door
isDoor = False

# Set up room and put up walls
room = viz.addChild('lab.osgb')

# Add table
table = viz.addChild('CustomModels/table1.osgb')
table.setScale([0.01, 0.015, 0.01])
table.setPosition([3, 0, 3])

#
dog = viz.addChild('CustomModels/shiba.glb.')
dog.setScale([0, 0, 0])
dog.setPosition([0, 0, 0])

# Add Shelf
shelf = viz.addChild('CustomModels/shelf.fbx')
shelf.setScale([.01, .01, .01])
shelf.setPosition([-3, 0, -3])

# Create Wall 1 with door
# The wall consists of three parts, left of the door, above the door, and right of the door
# Alternatively door could be overlaid on a singular instance of the wall, however this gives the option to have 
	# an event derender the door and create an openning to pass to another room

if isDoor: 
	door = viz.addTexQuad()
	door.setScale([1.5,3,1])
	door.setPosition([0,1.5,5])
	doorCover = viz.addTexture('CustomImages/door.jpg')
	door.texture(doorCover)

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

viz.MainView.collision(viz.ON)