import sys
import requests
import json 
from datetime import datetime
import pandas as pd
import stardateLinux as SDL

def tzconvert(dob, btime, latitude, longitude, steps, orb):

    date = dob + " " + btime
    newdatetime = pd.to_datetime(date)
    #newerdatetime = newdatetime.strftime('%d.%m.%Y')
    #print(newdatetime)


    #Format Date Below...


    #Google Time Zone Conversions & DST Conversions.
    """
    Timezone notes:  The desired time as seconds since midnight, January 1, 1970 UTC. The Time Zone API uses the timestamp to determine whether or not Daylight Savings should be applied, based on the time zone of the location.

    Note that the API does not take historical time zones into account. That is, if you specify a past timestamp, the API does not take into account the possibility that the location was previously in a different time zone. 
    """

    url = "https://maps.googleapis.com/maps/api/timezone/json?location=" + str(latitude) + "%2C" + str(longitude) + "&timestamp=1331161200&key=AIzaSyCmB25VRrXjHU4tfIjCyO_2cF7MGgTa37A"


    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    json_array = response.text
    python_array = json.loads(json_array)
    print(python_array)
    #rawoffset= python_array['rawOffset']
    #dstoffset= python_array['dstOffset']
    timezoneid = python_array['timeZoneId']
    timezonename = python_array['timeZoneName']

    #houroffset = int(rawoffset / 60 / 60)
    #print(houroffset)


    #Convert to UTC & DST based on date
    newerdatetime = newdatetime.tz_localize(timezoneid).tz_convert("UTC")
    print(newerdatetime)

    dob = newerdatetime.strftime("%d.%m.%Y")
    btime = newerdatetime.strftime("%H:%M:%S")
    print(dob)
    print(btime)



    SDL.StarDateFunction(dob,btime,latitude,longitude, steps, timezoneid, orb)
    #print(response.text)

if __name__ == '__main__':
    tzconvert(dob, btime, latitude, longitude, steps, orb)
