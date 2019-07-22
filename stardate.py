import subprocess

cmd = "C:\\Users\\palbe\\Documents\\software\\sweph\\sweph\\bin\\swetest -b23.12.1991 -g, -ut3:44:00 -lat -geopos41.2,-73.47,65  -head -fJplZ -eswe -n5 -p0123456789"

number_of_planets = 10
orb = 15
output = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
#debugging tool
print output
#Write to file
path = 'c:\\users\\palbe\\desktop\\astrofile.txt'

astro_file = open(path,'w')

astro_file.write(output)
astro_file.close()
#Write file to array
planet_date_array = []

with open(path,'r') as f:
	for line in f:
		planet_date_array.append(line)
#Test that planets are printing
#print planet_date_array

#Clean Data

#Nest arrays; planet & positions for each date
#arr0=first day, arr1=second day
#debugging tool
#print(len(planet_date_array))

number_of_days = len(planet_date_array) / number_of_planets
#debugging tool
#print number_of_days

temp=[]
for elem in planet_date_array:
	temp2 = elem.split(',')
	temp.append((temp2))
#debugging tool
#print temp
#debugging tool
#print len(temp)

sorted_data = []
j = 1
i = 0

number_of_steps = len(temp) / number_of_planets
while j <= number_of_steps:
	temp4 = []
	temp4.append(float(temp[i][0]))
	while i < (number_of_planets * j) :
		temp4.append(temp[i][1])
		temp4.append(float(temp[i][2]))
		i = i + 1
	sorted_data.append(temp4)
	j = j + 1
print sorted_data

#run calculations

#sunDatesMatrix = [[0]*(number_of_planets+1)]*number_of_days
#print sunDatesMatrix
#moonDatesMatrix = [number_of_planets]*[number_of_days]
#mercuryDatesMatrix = [number_of_planets]*[number_of_days]
#marsDatesMatrix = [number_of_planets]*[number_of_days]
#jupiterDatesMatrix = [number_of_planets]*[number_of_days]
#saturnDatesMatrix = [number_of_planets]*[number_of_days]
#uranusDatesMatrix = [number_of_planets]*[number_of_days]
#neptuneDatesMatrix = [number_of_planets]*[number_of_days]
#plutoDatesMatrix = [number_of_planets]*[number_of_days]
natal_sun = sorted_data[1][2]
natal_moon = sorted_data[1][4]
natal_mercury = sorted_data[1][6]
natal_venus = sorted_data[1][8]
natal_mars = sorted_data[1][10]
natal_jupiter = sorted_data[1][12]
natal_saturn = sorted_data[1][14]
natal_uranus = sorted_data[1][16]
natal_neptune = sorted_data[1][18]
natal_pluto = sorted_data[1][20]
print("natal planetary degrees with 0 as 0 degrees Aries")
print("sun",natal_sun)
print("moon",natal_moon)
print("mercury",natal_mercury)
print("venus",natal_venus)
print("mars",natal_mars)
print("jupiter",natal_jupiter)
print("saturn",natal_saturn)
print("uranus",natal_uranus)
print("neptune",natal_neptune)
print("pluto",natal_pluto)


#planetary_matrix = []
#for item in sorted_data:
sun_delta_matrix = []
print(len(sorted_data[1]))
'''
i=0
j=2
while i < len(sorted_data):
	temp_calculations = []
	temp_calculations.append(sorted_data[i][0])
	while j < len(sorted_data[i]):
		temp_calculations.append(abs(sorted_data[0][2] - sorted_data[i][j]))
		j = j + 2
	sun_delta_matrix.append(temp_calculations)
	i = i + 1
	j = 2
'''

i=0
j=2
sun_delta_matrix = []

natal_sun_sun_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_moon_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_mercury_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_venus_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_mars_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_jupiter_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_saturn_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_uranus_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_neptune_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_sun_pluto_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]

while i < len(sorted_data):
	temp_calculations = []
	temp_calculations.append(sorted_data[i][0])
	natal_sun_sun_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_moon_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_mercury_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_venus_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_mars_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_jupiter_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_saturn_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_neptune_aspect_matrix[i][0] = sorted_data[i][0]
	natal_sun_pluto_aspect_matrix[i][0] = sorted_data[i][0]
	while j <= len(sorted_data[i]):
		sun_delta = abs(sorted_data[0][2] - sorted_data[i][j])
		temp_calculations.append(sun_delta)
		#sun
		if j == 2:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_sun_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_sun_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_sun_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_sun_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_sun_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#moon
		elif j == 4:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_moon_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_moon_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_moon_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_moon_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_moon_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#mercury
		elif j == 6:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_mercury_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_mercury_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_mercury_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_mercury_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_mercury_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#venus
		elif j == 8:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_venus_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_venus_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_venus_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_venus_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_venus_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#mars
		elif j == 10:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_mars_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_mars_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_mars_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_mars_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_mars_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#jupiter
		elif j == 12:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_jupiter_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_jupiter_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_jupiter_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_jupiter_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_jupiter_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#saturn
		elif j == 14:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_saturn_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_saturn_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_saturn_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_saturn_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_saturn_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#uranus
		elif j == 16:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_uranus_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_uranus_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_uranus_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_uranus_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_uranus_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#neptune
		elif j == 18:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_neptune_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_neptune_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_neptune_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_neptune_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_neptune_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2
		#pluto
		elif j == 20:
			#conjunction
			if  sun_delta <= orb:
				natal_sun_pluto_aspect_matrix[i][1] = sun_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= sun_delta <= (60 + orb):
				natal_sun_pluto_aspect_matrix[i][2] = sun_delta
				j = j + 2
			#square
			elif (90 - orb) <= sun_delta <= (90 + orb):
				natal_sun_pluto_aspect_matrix[i][3] = sun_delta
				j = j + 2
			#trine
			elif (120 - orb) <= sun_delta <= (120 + orb):
				natal_sun_pluto_aspect_matrix[i][4] = sun_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= sun_delta <= (180 + orb):
				natal_sun_pluto_aspect_matrix[i][5] = sun_delta
				j = j + 2
			else:
				j = j + 2

		else:
			j = j + 2


	sun_delta_matrix.append(temp_calculations)
	i = i + 1
	j = 2

i=0
j=2
moon_delta_matrix = []
natal_moon_sun_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_moon_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_mercury_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_venus_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_mars_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_jupiter_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_saturn_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_uranus_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_neptune_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
natal_moon_pluto_aspect_matrix = [[-1] * 6 for item in range(number_of_days)]
while i < len(sorted_data):
	temp_calculations = []
	temp_calculations.append(sorted_data[i][0])
	natal_moon_sun_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_moon_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_mercury_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_venus_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_mars_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_jupiter_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_saturn_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_neptune_aspect_matrix[i][0] = sorted_data[i][0]
	natal_moon_pluto_aspect_matrix[i][0] = sorted_data[i][0]
	while j <= len(sorted_data[i]):
		moon_delta = abs(sorted_data[0][4] - sorted_data[i][j])
		temp_calculations.append(moon_delta)
		#sun
		if j == 2:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_sun_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_sun_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_sun_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_sun_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_sun_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#moon
		elif j == 4:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_moon_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_moon_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_moon_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_moon_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_moon_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#mercury
		elif j == 6:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_mercury_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_mercury_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_mercury_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_mercury_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_mercury_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#venus
		elif j == 8:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_venus_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_venus_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_venus_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_venus_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_venus_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#mars
		elif j == 10:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_mars_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_mars_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_mars_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_mars_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_mars_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#jupiter
		elif j == 12:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_jupiter_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_jupiter_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_jupiter_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_jupiter_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_jupiter_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#saturn
		elif j == 14:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_saturn_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_saturn_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_saturn_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_saturn_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_saturn_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#uranus
		elif j == 16:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_uranus_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_uranus_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_uranus_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_uranus_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_uranus_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#neptune
		elif j == 18:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_neptune_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_neptune_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_neptune_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_neptune_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_neptune_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2
		#pluto
		elif j == 20:
			#conjunction
			if  moon_delta <= orb:
				natal_moon_pluto_aspect_matrix[i][1] = moon_delta
				j = j + 2
			#sextile
			elif (60 - orb) <= moon_delta <= (60 + orb):
				natal_moon_pluto_aspect_matrix[i][2] = moon_delta
				j = j + 2
			#square
			elif (90 - orb) <= moon_delta <= (90 + orb):
				natal_moon_pluto_aspect_matrix[i][3] = moon_delta
				j = j + 2
			#trine
			elif (120 - orb) <= moon_delta <= (120 + orb):
				natal_moon_pluto_aspect_matrix[i][4] = moon_delta
				j = j + 2
			#opposition
			elif  (180 - orb) <= moon_delta <= (180 + orb):
				natal_moon_pluto_aspect_matrix[i][5] = moon_delta
				j = j + 2
			else:
				j = j + 2

		else:
			j = j + 2


	moon_delta_matrix.append(temp_calculations)
	i = i + 1
	j = 2
print('sun aspects')
print(sun_delta_matrix)
print(natal_sun_sun_aspect_matrix)
print(natal_sun_moon_aspect_matrix)
print(natal_sun_mercury_aspect_matrix)
print(natal_sun_venus_aspect_matrix)
print(natal_sun_mars_aspect_matrix)
print(natal_sun_saturn_aspect_matrix)
print(natal_sun_neptune_aspect_matrix)
print(natal_sun_uranus_aspect_matrix)
print(natal_sun_pluto_aspect_matrix)
print('moon aspects')
print(moon_delta_matrix)
print(natal_moon_sun_aspect_matrix)
print(natal_moon_moon_aspect_matrix)
print(natal_moon_mercury_aspect_matrix)
print(natal_moon_venus_aspect_matrix)
print(natal_moon_mars_aspect_matrix)
print(natal_moon_saturn_aspect_matrix)
print(natal_moon_neptune_aspect_matrix)
print(natal_moon_uranus_aspect_matrix)
print(natal_moon_pluto_aspect_matrix)
