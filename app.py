from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configuration
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'
app.config['MYSQL_DATABASE_DB'] = 'exams'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search")
def search():
    if request.method == "GET":
        title = request.args.get("title")
        number = request.args.get("number")
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * FROM 2019fall WHERE COURSE_TITLE = %s AND COURSE_NUMBER = %s", (title, number))
        data = cursor.fetchall()
        # mysql.connect().commit()
        cursor.close()
    return render_template('index.html', data=data)