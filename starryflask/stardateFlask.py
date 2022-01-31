from flask import Flask, request, render_template
import psycopg2
try:
    conn = psycopg2.connect(database="stardate", user="stardatepeter", password="stardatepeter", host="localhost")
    print("connected")
except:
    print("I can't connect")
mycursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consolidated_aspects')
def consolidated_aspects():
    mycursor.execute("SELECT * FROM consolidated_aspects WHERE date > CURRENT_DATE ORDER BY date;")
    data = mycursor.fetchall()
    return render_template('consolidated_aspects.html', data=data)

