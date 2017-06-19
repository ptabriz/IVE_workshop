import sys
import viz
import vizact
import viztask
import vizinput
import os
import oculus
import win32con
import win32gui
import vizshape
import oculus
#import oculus_08 as oculus


# Define global Variables#
IMAGE_PATH = os.path.join(os.getcwd(),"ENV")
FILE_PATH = os.getcwd()
fileList = os.listdir(IMAGE_PATH)
env_map_namelist = []
prompt=''
text = viz.addText(prompt,viz.SCREEN)
#videoFrame = vizshape.addBox(size=(10.5,5,0))
viz.mouse.setOverride(viz.ON) 
view = viz.MainView
view.eyeheight=14

for im_name in fileList:
  if im_name.endswith('_negx.png'):
   env_map_name = im_name[:-9] + '.png'
   env_map_namelist.append(env_map_name)

listLenght= len(env_map_namelist)

#Initiate Env# 
viz.setMultiSample(4)
viz.fov(60)
viz.go()

# define window operations #
def MaximizeWindow():
	#win32gui.ShowWindow(viz.window.getHandle(),win32con.SW_MAXIMIZE)
  viz.window.setFullscreenRectangle([0,0,1920,1080])
  viz.window.setFullscreen(1)

def RestoreWindow():
	win32gui.ShowWindow(viz.window.getHandle(),win32con.SW_RESTORE)


#initialize the cover page
botImage= viz.add('Bottom_ribbon.png')
topImage= viz.add('Top_ribbon.png')
midImage= viz.add('main_middle.png')

midRibbon.texture(midImage)
topRibbon.texture(topImage)
botRibbon.texture(botImage)

###Playback procedure###

def Loop():

 hmd = oculus.Rift()
 link=viz.link(hmd.getSensor(), viz.MainView)
 for x in range (0,listLenght):
   a=env_map_namelist[x]
   env = viz.addEnvironmentMap(IMAGE_PATH+"/"+a)
   sky = viz.addCustomNode('skydome.dlc')
   sky.texture(env)
   viz.setOption(a,viz.FREE_TEXTURE_MEMORY_HINT)
   yield viztask.waitKeyDown(" ")
   sky.remove()  
 link.remove() 

 #link=viz.link(subWindow, viz.MainView)
def run():
 yield Loop()
 #yield finale()
 
viztask.schedule(run())



