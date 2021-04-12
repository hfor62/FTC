import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    #camera.start_preview(fullscreen=False, window=(100,100,256,192))
    #time.sleep(10)
    #camera.preview.window=(200,200,256,192)
    #time.sleep(10)
    camera.start_preview(fullscreen=False, window=(50,50,1280,960))
    time.sleep(300)