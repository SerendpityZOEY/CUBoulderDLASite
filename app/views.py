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
    app.logger.info('waiting for input in student page')
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
    # print(race)
    # print(query)
    app.logger.info(name + 'is sucessfully submitted')
    cursor.execute(query, (name, gender, origin, race))
    conn.commit()
    # cursor.callproc('sp_createUser', (_name, _gender, _origin, _race))
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
    query = "INSERT INTO `faculty` (`name1`, `phone1`, `email1`, `program1`, `radio0`, `name2`,  \
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
