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
wallOne = viz.addTexQuad()
wallOne.setPosition([0,2.5,5])
wallOne.setScale([10,5,10])
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

# Cover walls with texture
wallCover = viz.addTexture('images/tile_slate.jpg')
wallOne.texture(wallCover)
wallTwo.texture(wallCover)
wallThree.texture(wallCover)
wallFour.texture(wallCover)
ceiling.texture(wallCover)

viz.MainView.collision(viz.ON)