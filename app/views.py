from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
import random
import string
from hashlib import sha512

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abs234grj2345'
app.config['MYSQL_DATABASE_DB'] = 'SEDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

SIMPLE_CHARS = string.ascii_letters + string.digits

def getRandomString(length=24):
    return ''.join(random.choice(SIMPLE_CHARS) for i in xrange(length))

def getRandomHash(length=24):
    hash = sha512()
    hash.update(getRandomString())
    return hash.hexdigest()[:length]


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
    race = request.form['hello']
    phoneNumber = request.form['phone']
    email = request.form['email']
    Address = request.form['address']
    Major = request.form['major']
    studentNumber = int(request.form['SN'])
    GPA = float(request.form['GPA'])
    level = request.form['level']
    Date = request.form['date']
    experience = request.form['experience']
    Apply = request.form['apply']
    p1 = request.form['p1']
    p2 = request.form['p2']
    p3 = request.form['p3']
    p4 = request.form['p4']
    p5 = request.form['p5']
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO `student` (`name`, `gender`, `origin`, `race`,`phoneNumber`,`email`,`Address`,`Major`,`studentNumber`,`GPA`,`level`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(query,(name,gender,origin,race,phoneNumber,email,Address,Major,studentNumber,GPA,level))
    query2 = "INSERT INTO `application` (`Sid`, `Priority`, `ProjectID`) VALUES (%s,%s,%s);"
    cursor.execute(query2,(studentNumber,1,p1[0]))
    cursor.execute(query2,(studentNumber,2,p2[0]))
    cursor.execute(query2,(studentNumber,3,p3[0]))
    cursor.execute(query2,(studentNumber,4,p4[0]))
    cursor.execute(query2,(studentNumber,5,p5[0]))
    print(race)
    print(query)
    app.logger.info(name + 'is sucessfully submitted')
    conn.commit()
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps({'message': 'Student info saved successfully !'})


@app.route('/faculty')
def faculty():
    app.logger.info('waiting for input in teacher page')
    return render_template("faculty.html")


@app.route('/fsubmit', methods=['GET', 'POST'])
def f_submit():
    print("Enter f_submit")
    name1 = request.form['name1']
    phone1 = request.form['phone1']
    email1 = request.form['email1']
    program1 = request.form['program1']  # int
    radio0 = request.form['optradio']  # string
    name2 = request.form['name2']
    phone2 = request.form['phone2']
    email2 = request.form['email2']
    program2 = request.form['program2']  # int
    name3 = request.form['name3']
    phone3 = request.form['phone3']
    email3 = request.form['email3']
    field1 = request.form['field1']
    field2 = request.form['field2']
    field3 = request.form['field3']
    field4 = request.form['field4']
    major = request.form.getlist('field5')  # int
    radio1 = request.form['optradio1']  # int
    radio2 = request.form['optradio2']  # int
    radio3 = request.form['optradio3']  # int
    radio4 = request.form['optradio4']  # int
    field6 = request.form['field6']
    f1 = request.form['f1']  # int
    f2 = request.form['f2']  # int
    radio5 = request.form['optradio5']
    conn = mysql.connect()
    cursor = conn.cursor()
    print(name1, phone1, email1, program1, radio0, name2, phone2, email2, program2, name3, phone3, email3,
          field1, field2, field3, field4, major, radio1, radio2, radio3, radio4, field6, f1, f2, radio5)
    query = "INSERT INTO `faculty` (`name1`, `phone1`, `email1`, `program1`, `radio0`, `name2`, \
            `phone2`, `email2`, `program2`, `name3`, `phone3`, `email3`, `field1`, `field2`, \
            `field3`, `field4`, `major`, `radio1`, `radio2`, `radio3`, `radio4`, `field6`, \
            `f1`, `f2`, `radio5`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
            "%s,%s,%s,%s);"
    app.logger.info('is sucessfully submitted')
    cursor.execute(query,
                   (name1, phone1, email1, program1, radio0, name2, phone2, email2, program2, name3, phone3, email3,
                    field1, field2, field3, field4, major, radio1, radio2, radio3, radio4, field6, f1, f2, radio5))
    conn.commit()
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps({'message': 'Faculty info saved successfully !'})
