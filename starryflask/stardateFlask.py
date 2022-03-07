from flask import Flask, request, render_template, url_for, flash, redirect, session
import psycopg2
import subprocess
import time
import psycopg2
from datetime import datetime
import datecalc as datecalc
from tzconversion import tzconvert

#try:
#    conn = psycopg2.connect(database="stardate", user="stardatepeter", password="stardatepeter", host="localhost")
#    print("connected")
#except:
#    print("I can't connect")
#mycursor = conn.cursor()
#mycursor.execute('DROP TABLE IF EXISTS "consolidated_aspects"')
#conn.commit()
app = Flask(__name__)
app.config['SECRET_KEY'] = '02aee329ea5b76b8234c6d2885356b6cf445c21daa426a2c'


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        dob = request.form['dob']
        btime = request.form['btime']
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        orb = request.form['orb']
        
        steps = str(datecalc.calc(dob,enddate))
        tzconvert(dob,btime,latitude,longitude,steps,orb)
        session['startdate'] = request.form['startdate']
        #cmd = "python3 stardateLinux.py " + dob + " " + btime + " " + latitude + " " + longitude + " " + steps
        #subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
        return redirect(url_for('consolidated_aspects'))

    return render_template('index.html')

@app.route('/consolidated_aspects')
def consolidated_aspects():
    startdate = session.pop('startdate', None)
    sqlstartdate = datetime.strptime(startdate,"%Y-%m-%d")

    sqlstartdate = sqlstartdate.strftime("%Y%m%d")
    conn = psycopg2.connect(database="stardate", user="stardatepeter", password="stardatepeter", host="localhost")
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM consolidated_aspects WHERE date > '" + sqlstartdate + "'  ORDER BY id;")
    data = mycursor.fetchall()
    return render_template('consolidated_aspects.html', data=data)
    conn.close()