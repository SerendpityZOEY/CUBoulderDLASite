from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'SEDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/student')
def student():
    return render_template("student.html")


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    name = request.form['name']
    gender = request.form['optradio']
    origin = request.form['optionsRadios']
    race = request.form.getlist('hello')

    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO `Demographic` (`name`, `gender`, `origin`, `race`) VALUES (%s,%s,%s,%s);"
    print(race)
    print(query)
    cursor.execute(query,(name,gender,origin,race))
    conn.commit()
    # cursor.callproc('sp_createUser', (_name, _gender, _origin, _race))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps({'message':'User created successfully !'})


@app.route('/faculty')
def faculty():
    return render_template("faculty.html")