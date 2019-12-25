from django.shortcuts import render
from django.http import HttpResponse

import wiringpi2 as wiringpi
import time

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(32,1)
wiringpi.pinMode(36,1)
wiringpi.pinMode(38,1)

def sensor(request):
	if 'on' in requset.POST:
		wiringpi.digitalWrite(32,1)
		wiringpi.digitalWrite(36,1)
		wiringpi.digitalWrite(38,1)
	elif 'off' in request.PORT:
		wiringpi.digitalWrite(32,0)
		wiringpi.digitalWrite(36,0)
		wiringpi.digitalWrite(38,0)
	return render(requset, 'control.html')
