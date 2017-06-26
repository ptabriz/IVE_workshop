#filename        :IVE_VIDEO_Template
#description     :This python file runs in World vizard to display 360 images in a folder on Oculus headset
#author          :Payam Tabrizian
#date            :15.6.2017
#usage           :World Vizard 
#python_version  :2.7 
#==============================================================================


import sys
import viz
import vizact
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
viz.mouse.setOverride(viz.ON) 

env_map_namelist = []
for im_name in os.listdir(IMAGE_PATH):
  if im_name.endswith('_negx.png'):
   env_map_name = im_name[:-9] + '.png'
   env_map_namelist.append(env_map_name)

#Initiate Env# 
viz.setMultiSample(4)
viz.fov(60)
viz.go()

# define window operations #
def MaximizeWindow():
  viz.window.setFullscreenRectangle([0,0,1920,1080])
  viz.window.setFullscreen(1)

def RestoreWindow():
	win32gui.ShowWindow(viz.window.getHandle(),win32con.SW_RESTORE)

###Playback procedure###

def Loop():

 hmd = oculus.Rift()
 link=viz.link(hmd.getSensor(), viz.MainView)
 for x in range (0,len(env_map_namelist)):
   env = viz.addEnvironmentMap(IMAGE_PATH+"/"+env_map_namelist[x])
   sky = viz.addCustomNode('skydome.dlc')
   sky.texture(env)
   viz.setOption(env_map_namelist[x],viz.FREE_TEXTURE_MEMORY_HINT)
   yield viztask.waitKeyDown(" ")
   sky.remove()  
 link.remove() 

def run():
 yield Loop()
 
viztask.schedule(run())



