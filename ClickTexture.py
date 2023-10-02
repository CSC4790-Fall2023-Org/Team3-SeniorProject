import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

# Disable mouse navigation
viz.mouse(viz.OFF)

viz.clearcolor(viz.SKYBLUE)

#added Image after each texture name to prevent overlap with keywords
andImage = viz.addTexture('CustomTextures/and.png')
nandImage = viz.addTexture('CustomTextures/nand.png')
norImage = viz.addTexture('CustomTextures/nor.png')
notImage = viz.addTexture('CustomTextures/not.png')
orImage = viz.addTexture('CustomTextures/or.png')
xorImage = viz.addTexture('CustomTextures/xor.png')
xnorImage = viz.addTexture('CustomTextures/xnor.png')

# Variable declarations
counter = 0
colors = [andImage, nandImage, norImage, notImage, orImage, xorImage, xnorImage]

# Create surface to wrap the texture on
quad = viz.addTexQuad()
quad.setPosition([0, 2, 3])  # Put quad in view

# Wrap initial texture on quad
quad.texture(andImage)

def changeTexture():
    global counter  # Declare counter as global
    object = viz.pick()
    if object.valid():
        counter += 1  # Increment the global counter
        quad.texture(colors[counter % 7])
    # print(counter) 

# Callback for mouse clicks
# First argument can be viz.MOUSEBUTTON_LEFT, viz.MOUSEBUTTON_RIGHT, or viz.MOUSEBUTTON_MIDDLE
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, changeTexture)
