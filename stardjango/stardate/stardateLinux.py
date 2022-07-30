def StarDateFunction(dob, btime, latitude, longitude, steps, timezoneid, orb, username):

    import subprocess
    import csv
    import time
    import psycopg2
    from io import BytesIO
    from datetime import datetime
    import pandas as pd
    import os

   
    dsn = "host='localhost' dbname='stardate' user='stardatepeter' password='stardatepeter'";
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    table_name = "starapp_sdate"
    # cur.execute('DROP TABLE IF EXISTS "consolidated_aspects"')
    

    #REMOVE THIS LINE BEFORE GOING TO PRODUCTION
 #   cur.execute('DELETE FROM starapp_sdate;')

    # cur.execute("""
    # CREATE TABLE consolidated_aspects(
    # id int PRIMARY KEY,
    # date timestamptz,
    # aspects text)
    # """)

    orb = int(orb)


    t0=time.process_time()
    cmd = "../../../swisseph/swetest -b" + dob + " -g, -ut" + btime + " -lat -geopos" + latitude + "," + longitude + ",65  -head -fTplZ -eswe -n" + steps + " -p0123456789"

    number_of_planets = 10
    number_of_aspects = 5
    output = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    #debugging tool
    #print(output)
    #Write to file
    path = 'astrofile.txt'


    with open(path, 'wb') as astro_file:
        astro_file.write(output)

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
        temp4.append(temp[i][0])
        while i < (number_of_planets * j) :
            temp4.append(temp[i][1])
            temp4.append(float(temp[i][2]))
            #adding signs
            temp4.append(temp[i][3].replace('\n',''))
            i = i + 1
        sorted_data.append(temp4)
        j = j + 1
    #print(sorted_data)
    #run calculations
    #revised from 2,4,6 to incorporate signs
    natal_sun = sorted_data[1][2]
    natal_moon = sorted_data[1][5]
    natal_mercury = sorted_data[1][8]
    natal_venus = sorted_data[1][11]
    natal_mars = sorted_data[1][14]
    natal_jupiter = sorted_data[1][17]
    natal_saturn = sorted_data[1][20]
    natal_uranus = sorted_data[1][23]
    natal_neptune = sorted_data[1][26]
    natal_pluto = sorted_data[1][29]
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

    def aspect_name(planet_delta_temp):
        global aspect
        #conjunction
        if  (orb * -1) <= planet_delta_temp <= orb:
            aspect = "Conjuncts"
            return aspect
        #sextile
        elif ((60 - orb) <= planet_delta_temp <= (60 + orb)) or ((-60 - orb) <= planet_delta_temp <= (-60 + orb)):
            aspect = "Sextiles"
            return aspect
        #square
        elif ((90 - orb) <= planet_delta_temp <= (90 + orb)) or ((-90 - orb) <= planet_delta_temp <= (-90 + orb)):
            aspect = "Squares"
            return aspect
        #trine
        elif ((120 - orb) <= planet_delta_temp <= (120 + orb)) or ((-120 - orb) <= planet_delta_temp <= (-120 + orb)):
            aspect = "Trines"
            return aspect
        #opposition
        elif ((180 - orb) <= planet_delta_temp <= (180 + orb)) or ((-180 - orb) <= planet_delta_temp <= (-180 + orb)):
            aspect = "Oppositions"
            return aspect
        else:
            return False


    def p1_name(m):
        global p1
        if m == 2:
            p1 ="Natal Sun "
            return p1
        elif m == 5:
            p1="Natal Moon "
            return p1
        elif m == 8:
            p1="Natal Mercury "
            return p1
        elif m == 11:
            p1="Natal Venus "
            return p1
        elif m == 14:
            p1="Natal Mars "
            return p1
        elif m == 17:
            p1="Natal Jupiter "
            return p1
        elif m == 20:
            p1="Natal Saturn "
            return p1
        elif m == 23:
            p1="Natal Uranus "
            return p1
        elif m == 26:
            p1 = "Natal Neptune "
            return p1
        elif m == 29:
            p1 = "Natal Pluto "
            return p1


    def p2_name(j):
        global p2
        if j == 2:
            p2="transiting Sun at "
            return p2
        elif j == 5:
            p2="transiting Moon at "
            return p2
        elif j == 8:
            p2="transiting Mercury at "
            return p2
        elif j == 11:
            p2="transiting Venus at "
            return p2
        elif j == 14:
            p2="transiting Mars at "
            return p2
        elif j == 17:
            p2="transiting Jupiter at "
            return p2
        elif j == 20:
            p2="transiting Saturn at "
            return p2
        elif j == 23:
            p2="transiting Uranus at "
            return p2
        elif j == 26:
            p2 = "transiting Neptune at "
            return p2
        elif j == 29:
            p2 = "transiting Pluto at "
            return p2

    master_delta_array = [['Date','NSun.V.Sun','NSun.v.Moon','NSun.V.Mercury','NSun.V.Venus','NSun.V.Mars','NSun.V.Jupiter','NSun.V.Saturn','NSun.V.Uranus','NSun.V.Neptune','NSun.V.Pluto','NMoon.V.Sun','NMoon.v.Moon','NMoon.V.Mercury','NMoon.V.Venus','NMoon.V.Mars','NMoon.V.Jupiter','NMoon.V.Saturn','NMoon.V.Uranus','NMoon.V.Neptune','NMoon.V.Pluto','NMercury.V.Sun','NMercury.v.Moon','NMercury.V.Mercury','NMercury.V.Venus','NMercury.V.Mars','NMercury.V.Jupiter','NMercury.V.Saturn','NMercury.V.Uranus','NMercury.V.Neptune','NMercury.V.Pluto','NVenus.V.Sun','NVenus.v.Moon','NVenus.V.Mercury','NVenus.V.Venus','NVenus.V.Mars','NVenus.V.Jupiter','NVenus.V.Saturn','NVenus.V.Uranus','NVenus.V.Neptune','NVenus.V.Pluto','NMars.V.Sun','NMars.v.Moon','NMars.V.Mercury','NMars.V.Venus','NMars.V.Mars','NMars.V.Jupiter','NMars.V.Saturn','NMars.V.Uranus','NMars.V.Neptune','NMars.V.Pluto','NJupiter.V.Sun','NJupiter.v.Moon','NJupiter.V.Mercury','NJupiter.V.Venus','NJupiter.V.Mars','NJupiter.V.Jupiter','NJupiter.V.Saturn','NJupiter.V.Uranus','NJupiter.V.Neptune','NJupiter.V.Pluto','NSaturn.V.Sun','NSaturn.v.Moon','NSaturn.V.Mercury','NSaturn.V.Venus','NSaturn.V.Mars','NSaturn.V.Jupiter','NSaturn.V.Saturn','NSaturn.V.Uranus','NSaturn.V.Neptune','NSaturn.V.Pluto','NUranus.V.Sun','NUranus.v.Moon','NUranus.V.Mercury','NUranus.V.Venus','NUranus.V.Mars','NUranus.V.Jupiter','NUranus.V.Saturn','NUranus.V.Uranus','NUranus.V.Neptune','NUranus.V.Pluto','NNeptune.V.Sun','NNeptune.v.Moon','NNeptune.V.Mercury','NNeptune.V.Venus','NNeptune.V.Mars','NNeptune.V.Jupiter','NNeptune.V.Saturn','NNeptune.V.Uranus','NNeptune.V.Neptune','NNeptune.V.Pluto','NPluto.V.Sun','NPluto.v.Moon','NPluto.V.Mercury','NPluto.V.Venus','NPluto.V.Mars','NPluto.V.Jupiter','NPluto.V.Saturn','NPluto.V.Uranus','NPluto.V.Neptune','NPluto.V.Pluto']]
    consolidated_aspects = []

    def astrology_array():
        count = 0
        i = 0
        while i < len(sorted_data):
            m = 2
            temp_data = []
            temp_aspect = []
            temp_aspect_start = '\n'
            temp_aspect.append(username)
            time_str = str(sorted_data[i][0])
#Convert UTC TimeStamps to Localtime
            time_stampUTC = pd.to_datetime(time_str, dayfirst = True, utc=True)
            time_obj = time_stampUTC.tz_convert(timezoneid)
            #time_obj = time_stamp.date()
            temp_aspect.append(time_obj)
            temp_data.append(time_obj)
            while m < 31:
                j = 2
                while j < 31:
                    planet_delta_temp = round(sorted_data[0][m] - sorted_data[i][j], 3)
                    temp_data.append(planet_delta_temp)
                    a = aspect_name(planet_delta_temp)
                    if a != False:
                        p1 = p1_name(m)
                        p2 = p2_name(j)
                        aspect_str = str(p1) + "at " + str(sorted_data[0][m+1]) + " "  + str(a) + " " + str(p2) + "at " + str(sorted_data[i][j+1]) + ". Angle is " + str(planet_delta_temp) + " degrees;\n" 
                        temp_aspect_start +=  aspect_str
                    count = count + 1
                    j = j + 3
                m = m + 3
            #temp_aspect_start += "'"    
            temp_aspect.append(temp_aspect_start)
            print(temp_aspect)
            consolidated_aspects.append(temp_aspect)
            print(temp_aspect[2])
            # cur.execute("INSERT INTO consolidated_aspects VALUES (%s, %s, %s)",(temp_aspect))
            #tablename hardcoded
            cur.execute("INSERT INTO starapp_sdate (user_id, date, aspects) VALUES (%s, %s, E%s)",(temp_aspect))

            master_delta_array.append(temp_data)
            i = i + 1
            t1 = time.process_time() - t0
            print("Day: ", str(i), ", Time Elapsed: ",str(t1))

    astrology_array()
    conn.commit()
    conn.close()
    """
    with open('master_delta_array.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(master_delta_array)
    csvFile.close()

    with open('astroaspects_reduced.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(consolidated_aspects)
    csvFile.close()
    """

if __name__ == '__main__':
    StarDateFunction(dob, btime, latitude, longitude, steps, timezoneid, orb, username)
