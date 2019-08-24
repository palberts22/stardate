import subprocess

cmd = "C:\\Users\\palbe\\Documents\\software\\sweph\\sweph\\bin\\swetest -b23.12.1991 -g, -ut3:44:00 -lat -geopos41.2,-73.47,65  -head -fJplZ -eswe -n5 -p0123456789"

number_of_planets = 10
orb = 7
number_of_aspects = 5
output = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
#debugging tool
print(output)
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

#Clean Data
#Nest arrays; planet & positions for each date
#arr0=first day, arr1=second day

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
print(sorted_data)

#run calculations
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

sun_delta_matrix = []
print(len(sorted_data[1]))

i=0
j=2
sun_delta_matrix = []
moon_delta_matrix = []
mercury_delta_matrix = []
venus_delta_matrix = []
mars_delta_matrix = []
jupiter_delta_matrix = []
saturn_delta_matrix = []
uranus_delta_matrix = []
neptune_delta_matrix = []
pluto_delta_matrix = []

sun_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
moon_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
mercury_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
venus_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
mars_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
jupiter_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
saturn_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
uranus_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
neptune_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]
pluto_aspect_matrix = [[-1] * ((number_of_aspects * number_of_planets) + 1) for item in range(number_of_days)]

sun_aspect_matrix[i][0] = sorted_data[i][0]
moon_aspect_matrix[i][0] = sorted_data[i][0]
mercury_aspect_matrix[i][0] = sorted_data[i][0]
venus_aspect_matrix[i][0] = sorted_data[i][0]
mars_aspect_matrix[i][0] = sorted_data[i][0]
jupiter_aspect_matrix[i][0] = sorted_data[i][0]
saturn_aspect_matrix[i][0] = sorted_data[i][0]
neptune_aspect_matrix[i][0] = sorted_data[i][0]
pluto_aspect_matrix[i][0] = sorted_data[i][0]

def astrology_array(planet_delta, aspect_matrix, l):
	i = 0
	while i < len(sorted_data):
		j = 2
		while j < len(sorted_data[i]):
			temp_calculations = []
			temp_calculations.append(sorted_data[i][0])
			aspect_matrix[i][0] = sorted_data[i][0]
			k = 0
			while k < number_of_planets:
				planet_delta_temp = round(sorted_data[0][l] - sorted_data[i][j], 3)
				temp_calculations.append(planet_delta_temp)
				aspect(planet_delta_temp, aspect_matrix, i, j, k)
				k = k + 1
				j = j + 2
			planet_delta.append(temp_calculations)
		i = i + 1
	print(planet_delta)
	print(aspect_matrix)

def aspect(planet_delta, aspect_matrix, i, j, k,):
	#conjunction
	if  (orb * -1) <= planet_delta <= orb:
		aspect_matrix[i][1 + (k * number_of_aspects)] = planet_delta
	#sextile
	elif ((60 - orb) <= planet_delta <= (60 + orb)) or ((-60 - orb) <= planet_delta <= (-60 + orb)):
		aspect_matrix[i][2 + (k * number_of_aspects)] = planet_delta
	#square
	elif ((90 - orb) <= planet_delta <= (90 + orb)) or ((-90 - orb) <= planet_delta <= (-90 + orb)):
		aspect_matrix[i][3 + (k * number_of_aspects)] = planet_delta
	#trine
	elif ((120 - orb) <= planet_delta <= (120 + orb)) or ((-120 - orb) <= planet_delta <= (-120 + orb)):
		aspect_matrix[i][4 + (k * number_of_aspects)] = planet_delta
	#opposition
	elif ((180 - orb) <= planet_delta <= (180 + orb)) or ((-180 - orb) <= planet_delta <= (-180 + orb)):
		aspect_matrix[i][5 + (k * number_of_aspects)] = planet_delta

astrology_array(sun_delta_matrix,sun_aspect_matrix,2)
astrology_array(moon_delta_matrix,moon_aspect_matrix,4)
astrology_array(mercury_delta_matrix,mercury_aspect_matrix,6)
astrology_array(venus_delta_matrix,venus_aspect_matrix,8)
astrology_array(mars_delta_matrix,mars_aspect_matrix,10)
astrology_array(jupiter_delta_matrix,jupiter_aspect_matrix,12)
astrology_array(saturn_delta_matrix,saturn_aspect_matrix,14)
astrology_array(uranus_delta_matrix,uranus_aspect_matrix,16)
astrology_array(neptune_delta_matrix,neptune_aspect_matrix,18)
astrology_array(pluto_delta_matrix,pluto_aspect_matrix,20)
