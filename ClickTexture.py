"""  
Click on the tile to cycle through the 7 logic gate symbols.
In order, the symbols are AND, NAND, NOR, NOT, OR, XOR, XNOR
""" 

import viz
import vizact
import vizinfo
import vizmat

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Add instructions
vizinfo.InfoPanel()

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
colors1 =  viz.cycle([andImage, nandImage, norImage, notImage, orImage, xorImage, xnorImage])

# Create surface to wrap the texture on
quad1 = viz.addTexQuad()
quad1.setScale([1.5,1,1])
quad1.setPosition([0, 2, 3])  # Put quad in view

# Wrap initial texture on quad
quad1.texture(andImage)

def changeTexture(texArr, texQuad):
    object = viz.pick()
    if object.valid():
        texQuad.texture(texArr.next())

# Callback for mouse clicks
# First argument can be viz.MOUSEBUTTON_LEFT, viz.MOUSEBUTTON_RIGHT, or viz.MOUSEBUTTON_MIDDLE
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, lambda: changeTexture(colors1, quad1))

