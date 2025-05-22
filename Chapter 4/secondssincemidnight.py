def seconds_since_midnight(num1,num2,num3):
	hour_in_seconds = num1 * 3600
	minute_in_seconds = num2 * 60
	return hour_in_seconds + minute_in_seconds + num3
	
print(seconds_since_midnight(1,30,45))