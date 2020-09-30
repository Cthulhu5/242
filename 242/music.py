import time
import os
 
music_path = '/home/pi/Desktop/k.wav'
 
os.system('mplayer %s' % music_path )

time.sleep(60)