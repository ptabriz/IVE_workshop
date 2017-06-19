import sys
import viz
import viztask
import os
import vizshape
import oculus
import win32con
import win32gui
#import oculus_08 as oculus #for oculus DK2 with runtime .08

VIDEO_PATH = os.path.join(os.getcwd(), "ENV")
env_map_namelist = [video for video in os.listdir(VIDEO_PATH)]
viz.go()

def MaximizeWindow():
  win32gui.ShowWindow(viz.window.getHandle(),win32con.SW_MAXIMIZE)
  #viz.window.setFullscreenRectangle([0,0,1920,1080])
  viz.window.setFullscreen(1)
  
def Loop():
 ''' loop through the ENV directory and play videos '''
 hmd = oculus.Rift()

 link = viz.link(hmd.getSensor(), viz.MainView)
 for x in range (0, len(env_map_namelist)):

   VIDEO_FILE = VIDEO_PATH + "/" + env_map_namelist[x]
   video = viz.addVideo(VIDEO_FILE)
   sphere = vizshape.addSphere(radius=10000, flipFaces=True)
   sphere.texture(video)
   sphere.drawOrder(-100)
   video.play() 
   sphere.disable(viz.DEPTH_TEST)
   sphere.drawOrder(-100)
   viz.setOption(VIDEO_FILE, viz.FREE_TEXTURE_MEMORY_HINT)
   
   # Wait for the space button to change video #
   yield viztask.waitKeyDown(" ")
   video.remove()
   sphere.remove()  
 link.remove() 

def run():

 MaximizeWindow()
 yield Loop()

viztask.schedule(run())

