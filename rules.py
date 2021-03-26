


def rules():
	if temp < 30 and hum >= 50 and vis == 'notclear':
	    lcd.message('Cloudy - Fog')
	elif temp >= 30 and hum < 50 and vis == 'clear':
	    lcd.message('Hot and Dry')
	elif temp >= 30 and hum >= 50 and vis == 'clear':
	    lcd.message('Hot and Humid')
	elif temp < 30 and hum < 50 and vis == 'clear':
	    lcd.message('Cold and Dry')
	elif temp >= 30 and hum >= 50 and vis == 'notclear':
	    lcd.message('Humid - Fog')
	elif temp < 30 and hum < 50 and vis == 'notclear':
	    lcd.message('Smog - Air Pol.')
	elif temp >= 30 and hum < 50 and vis == 'notclear':
	    lcd.message('Smog - Air Pol.')
	elif temp < 30 and hum >= 50 and vis == 'clear':
	    lcd.message('Cold and Windy')
	else:
	    lcd.message("Data Error")
