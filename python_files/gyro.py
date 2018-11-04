#!/usr/bin/python
from mpu6050 import mpu6050
import time
import tweepy
import random
import requests


CONSUMER_KEY =""
CONSUMER_SECRET = ""   
ACCESS_KEY = ""    
ACCESS_SECRET = ""


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def get_value(sensor):
	return sensor.get_accel_data()


def calibrate(cycles, delta_thresh,sleep_per_cycle,sensor):
	stable = False
	x_mean = x_mean_old = 0
	y_mean = y_mean_old = 0
	z_mean = y_mean_old = 0
	count = 0
	while stable != True:
		value = get_value(sensor)
		x = value['x']
		y = value['y']
		z = value['z']
		x_mean_old = x_mean
		y_mean_old = y_mean
		z_mean_old = x_mean
		x_diff = abs(x_mean - x)
		y_diff = abs(y_mean - y)
		z_diff = abs(z_mean - z)
		if (x_diff > delta_thresh or y_diff > delta_thresh or z_diff > delta_thresh) and count != 0:
			print("Hold Still")
			count = 0
			x_mean = x_mean_old = 0
        		y_mean = y_mean_old = 0
        		z_mean = y_mean_old = 0
		elif count != 0:
			x_mean += (x - x_mean) / count
	 		y_mean += (y - y_mean) / count
			z_mean += (z - z_mean) / count
			if(count > cycles):
				stable = True
			else:
				count += 1
				time.sleep(sleep_per_cycle)
		else:
			x_mean = x
			y_mean = y
			z_mean = z
			count += 1
	return x_mean, y_mean, z_mean

sensor = mpu6050(0x68)
value = get_value(sensor)
x_mean,y_mean,z_mean = calibrate(10,.4,.1,sensor)
delta_thresh = .5
print("calibrated")
count = 0

while True:
	value = get_value(sensor)
	x = value['x']
	y = value['y']
	z = value['z']
	x_diff = abs(x_mean - x)
        y_diff = abs(y_mean - y)
        z_diff = abs(z_mean - z)
	if (x_diff > delta_thresh or y_diff > delta_thresh or z_diff > delta_thresh):
		print('Moved')

		requests.post("https://a490f171.ngrok.io", data={'beacon': 'A new hand touches the beacon.'})
		x_mean,y_mean,z_mean = calibrate(10,.4,.1,sensor)

		s = '!'

		for x in range(0,random.randint(0,7)):
        		s += '!'

		api.update_status('A new hand touches the beacon'+s)

	time.sleep(.1)
	if count >= 100:
		x_mean,y_mean,z_mean = calibrate(10,.4,0,sensor)
		count = 0
	count += 1
