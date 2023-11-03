import viz
import vizshape
import viztask
import vizmat

viz.go()

viz.clearcolor(viz.GRAY)

#Load Textures
tex0 = viz.addTexture('CustomTextures/timer/0.png')
tex1 = viz.addTexture('CustomTextures/timer/1.png')
tex2 = viz.addTexture('CustomTextures/timer/2.png')
tex3 = viz.addTexture('CustomTextures/timer/3.png')
tex4 = viz.addTexture('CustomTextures/timer/4.png')
tex5 = viz.addTexture('CustomTextures/timer/5.png')
tex6 = viz.addTexture('CustomTextures/timer/6.png')
tex7 = viz.addTexture('CustomTextures/timer/7.png')
tex8 = viz.addTexture('CustomTextures/timer/8.png')
tex9 = viz.addTexture('CustomTextures/timer/9.png')
colon = viz.addTexture('CustomTextures/timer/colon.png')
white1 = viz.addTexture('CustomTextures/timer/white1.jpg')

#Add textures to an array, array numbers correspond with Quad# (3 is colon)
countUp1 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex0])
countUp2 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex0])
countUp4 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex0])
countUp5 = viz.cycle([tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex0])

#Add a background to mount the clock on 
back = viz.addTexQuad()
back.setScale([3,1,0.5])
back.setPosition([0, 2, 6.001])  # Put quad in view
#Start digit at 0
back.texture(white1)

#Ones seconds digit
quad1 = viz.addTexQuad()
quad1.setScale([0.5,0.5,0.5])
quad1.setPosition([1, 2, 6])  # Put quad in view
#Start digit at 0
quad1.texture(tex0)

#Tens seconds digit
quad2 = viz.addTexQuad()
quad2.setScale([0.5,0.5,0.5])
quad2.setPosition([0.5, 2, 6])  # Put quad in view
#Start digit at 0
quad2.texture(tex0)

#Colon
quad3 = viz.addTexQuad()
quad3.setScale([0.5,0.5,0.5])
quad3.setPosition([0, 2, 6])  # Put quad in view
quad3.texture(colon)

#Ones minutes digit
quad4 = viz.addTexQuad()
quad4.setScale([0.5,0.5,0.5])
quad4.setPosition([-0.5, 2, 6])  # Put quad in view
#Start digit at 0
quad4.texture(tex0)

#Tens minutes digit
quad5= viz.addTexQuad()
quad5.setScale([0.5,0.5,0.5])
quad5.setPosition([-1, 2, 6])  # Put quad in view
#Start digit at 0
quad5.texture(tex0)
	
def swap_timer_tex(a1, q1, a2, q2, a3, q3, a4, q4):
	counter = 0
	while True:
		yield viztask.waitTime(1)
		counter = counter + 1
		#print(counter)
		
		#increment ones digit of seconds
		q1.texture(a1.next())
		
		#increment tens digits of seconds
		if(counter % 10 == 0):
			q2.texture(a2.next())
		
		#increment ones digit of minutes
		if(counter % 60 == 0):
			q3.texture(a3.next())
		
		#increment tens digit of minutes
		if(counter % 600 == 0):
			q4.texture(a4.next())
		
timer = viztask.schedule( swap_timer_tex(countUp1, quad1, countUp2, quad2, countUp4, quad4, countUp5, quad5) )

