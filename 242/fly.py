import  wave
import  numpy as np
import  os
from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 100)
pwm.start(0)

f  =  wave. open('/home/pi/Desktop/k.wav')
params  =  f.getparams()
nchannels, sampwidth, framerate, nframes  =  params[: 4 ]

strData  =  f.readframes(nframes)
waveData  =  np.frombuffer(strData,dtype = np.int16)
waveData  =  waveData * 1.0 / ( max ( abs (waveData)))

for i in range(0,int(nframes)):
    sleep(1/framerate)
    if(abs(waveData[i]*100 >= 100)):
       pwm.ChangeDutyCycle(90)
    else:
       pwm.ChangeDutyCycle(abs(waveData[i]*90))
pwm.ChangeDutyCycle(10)
