from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL


mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abs234grj2345'
app.config['MYSQL_DATABASE_DB'] = 'sedb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/student')
def student():
    app.logger.info('waiting for input in student page')
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `project`")
    data = cursor.fetchall()

    return render_template("student.html", data=data)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    name = request.form['name']
    gender = request.form['optradio']
    origin = request.form['optionsRadios']
    race = request.form.getlist('hello')
    phoneNumber = request.form.getlist('phone')
    email = request.form.getlist('email')
    Address = request.form.getlist('address')
    Major = request.form.getlist('major')
    studentNumber = request.form.getlist('SN')
    GPA = request.form.getlist('GPA')
    level = request.form.getlist('level')
    Date = request.form.getlist('date')
    experience = request.form.getlist('experience')
    Apply = request.form.getlist('apply')
    p1 = request.form.getlist('p1')
    p2 = request.form.getlist('p2')
    p3 = request.form.getlist('p3')
    app.logger.info(p1[0])
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO `student` (`name`, `gender`, `origin`, `race`,`phoneNumber`,`email`,`Address`,`Major`,`studentNumber`,`GPA`,`level`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(query,(name,gender,origin,race,phoneNumber,email,Address,Major,studentNumber,GPA,level))
    query2 = "INSERT INTO `application` (`Sid`, `P1id`, `P2id`, `P3id`) VALUES (%s,%s,%s,%s);"
    cursor.execute(query2,(studentNumber,p1[0],p2[0],p3[0]))
    # app.logger.info(name+'is sucessfully submitted')
    conn.commit()
    # cursor.callproc('sp_createUser', (_name, _gender, _origin, _race))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps({'message':'User created successfully !'})


@app.route('/faculty')
def faculty():
    app.logger.info('waiting for input in teacher page')
    return render_template("faculty.html")