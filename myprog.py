from flask import Flask, render_template 
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mullahoran98'
app.config['MYSQL_DB'] = 'list'
app.config['MYSQL_HOST'] = 'http://35.195.161.180'
mysql.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM tasks''')
    rv = cur.fetchall()
    return(rv)

if __name__ == "_main_":
    app.run(host='0.0.0.0',port='5000')
