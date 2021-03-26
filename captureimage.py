from picamera import PiCamera
from time import sleep
from latestimage import storeimage

def captureimage():
    camera = PiCamera()

    for i in range(5):
        print ("Capturing images...")
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/Project/foggyimagecf_nb/picamera/image%s.jpg' % i)
        camera.stop_preview()
        print ('Image ' + str(i) + ' captured.')

    print ('All images captured.')
    storeimage()

captureimage()