import glob
import os

search_dir = "/home/pi/Desktop/Project/foggyimagecf_nb/picamera/"

files = list(filter(os.path.isfile, glob.glob(search_dir + "*.jpg")))
files.sort(key=lambda x: os.path.getmtime(x))
img = files[-1]

def storeimage():
    #f = open('./picamera/sample_test.txt', 'w')
    #print('\n' + img, file = f)
    #f.close()

    print('Images added to test data.')
    
storeimage()