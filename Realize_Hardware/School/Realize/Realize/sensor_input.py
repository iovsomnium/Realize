from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#laser
GPIO.setup(8, GPIO.IN) #2-1 back
GPIO.setup(10, GPIO.IN) #2-1 front
GPIO.setup(12, GPIO.IN) #2-2 back
GPIO.setup(16, GPIO.IN) #2-2 front
GPIO.setup(18, GPIO.IN) #2-3 back
GPIO.setup(22, GPIO.IN) #2-3 front
GPIO.setup(24, GPIO.IN) #2-4 back
GPIO.setup(26, GPIO.IN) #2-4 front
#shake
GPIO.setup(32, GPIO.IN) #2-1
GPIO.setup(36, GPIO.IN) #2-2
GPIO.setup(38, GPIO.IN) #2-3
GPIO.setup(40, GPIO.IN) #2-4

def foo(request):
    try:
        laser_11 = GPIO.input(8)
        laser_12 = GPIO.input(10)
        laser_21 = GPIO.input(12)
        laser_22 = GPIO.input(16)
        laser_31 = GPIO.input(18)
        laser_32 = GPIO.input(22)
        laser_41 = GPIO.input(24)
        laser_42 = GPIO.input(26)
        shake_1 = GPIO.input(32)
        shake_2 = GPIO.input(36)
        shake_3 = GPIO.input(38)
        shake_4 = GPIO.input(40)
        
        #2-1
        if shake_1 == 1:
            if (laser_11 == 1 | laser_12 == 1):
                return HttpResponse("Please check 2-1\n")
            
            else:
                return HttpResponse("2-1 open door but not exit")
        #2-2
        elif shake_2 == 1:
            if (laser_21 == 1 | laser_22 == 1):
                return HttpResponse("Please check 2-2\n")
            
            else:
                return HttpResponse("2-2 open door but not exit")
        #2-3
        elif shake_3 == 1:
            if (laser_31 == 1 | laser_32 == 1):
                return HttpResponse("Please check 2-3\n")
            
            else:
                return HttpResponse("2-3 open door but not exit")
        #2-4
        elif shake_4 == 1:
            if (laser_41 == 1 | laser_42 == 1):
                return HttpResponse("Please check 2-4\n")
            
            else:
                return HttpResponse("2-4 open door but not exit")
        else:
            return HttpResponse("Stay")
    except:
        return HttpResponse(status=500)
    
