from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
import MysqlUtil
import random
import string
from hashlib import sha512

sqlUtil = MysqlUtil.MysqlUtil(app)
sqlUtil.use_account('developer')
sqlUtil.use_database('SETest')

SIMPLE_CHARS = string.ascii_letters + string.digits
def getRandomString(length=24):
    return ''.join(random.choice(SIMPLE_CHARS) for i in xrange(length))
def getRandomHash(length=24):
    hash = sha512()
    hash.update(getRandomString())
    return hash.hexdigest()[:length]


dic={1:'Aerospace Engineering Sciences', 2:'Applied Math', 3: 'Chemical & Biological Engineering', \
4: 'Civil, Environmental and Architectural Engineering', 5: 'Computer Science', 6: 'Electrical, Computer and Energy Engineering', \
7: 'Physics', 8: 'Environmental Engineering', 9: 'Mechanical Engineering', \
10: 'Colorado Space Grant', 11: 'Engineering Education', 12: 'ATLAS'}
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/student')
def student():
    app.logger.info('waiting for input in student page')
    data = sqlUtil.select_all("SELECT * FROM `project`")
    return render_template("student.html", data=data)


@app.route('/project', methods=['GET'])
def project():
    data=[]
    # cursor.execute("SELECT * FROM `project`")
    # projects = cursor.fetchall()
    projects = sqlUtil.select_all("SELECT * FROM `project`")
    app.logger.info(projects)
    for pid, pn, major, prid, link, des, req1, req2, req3, req4, req5 in projects:
        # cursor.execute("SELECT `name1`, `program1` FROM `faculty` WHERE `id`='{prid}'".format(prid=prid))
        # professorName, department = cursor.fetchone()
        professorName, department = sqlUtil.select_one("SELECT `name`, `dept` FROM `faculty` WHERE `id`='{prid}'".format(prid=prid))
        professorName, department = str(professorName), dic[int(department)]
        req = ''
        for i, r in enumerate((str(req1),str(req2),str(req3),str(req4),str(req5))):
            if r!='null':
                if i==0:
                    req+=r
                else:
                    req+', '+r

        data.append([str(pn), professorName, department,str(major),str(link),str(des),req])
        app.logger.info(data)
    return render_template("project.html", data=json.dumps(data))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    sqlUtil.batch_insert_push({
        'name':             request.form['name'],
        'gender':           request.form['gender'],
        'origin':           request.form['origin'],
        'race':             request.form['race'],
        'phoneNumber':      request.form['phone'],
        'email':            request.form['email'],
        'Address':          request.form['address'],
        'Major':            request.form['major'],
        'studentNumber':    request.form['SN'],
        'GPA':              request.form['GPA'],
        'level':            request.form['level'],
        # 'Date':             request.form['date'],
        # 'experience':       request.form['experience'],
        # 'Apply':            request.form['apply'],
    })

    sqlUtil.insert_execute('student')
    sqlUtil.clear()

    sqlUtil.insert_push('Sid', request.form['SN'])
    for i, p in enumerate(['p1', 'p2', 'p3', 'p4', 'p5']):
        sqlUtil.batch_insert_push({'Priority': i+1, 'ProjectID': (request.form[p])[0]})
        sqlUtil.insert_execute('application')
        # Don clear, since we need to reuse 'Sid' field
    sqlUtil.clear()

    return json.dumps({'message': 'Student info saved successfully !'})


@app.route('/faculty')
def faculty():
    app.logger.info('waiting for input in teacher page')
    return render_template("faculty.html")


@app.route('/fsubmit', methods=['GET', 'POST'])
def f_submit():
    print("Enter f_submit")

    specialReq1 = request.form.get('specialReq1', None)
    if specialReq1 is None:
        specialReq1 = "null"
    specialReq2 = request.form.get('specialReq2', None)
    if specialReq2 is None:
        specialReq2 = "null"
    specialReq3 = request.form.get('specialReq3', None)
    if specialReq3 is None:
        specialReq3 = "null"
    specialReq4 = request.form.get('specialReq4', None)
    if specialReq4 is None:
        specialReq4 = "null"
    specialReq5 = request.form.get('specialReq5', None)
    if specialReq5 is None:
        specialReq5 = "null"

    sqlUtil.batch_insert_push({
        'name':             request.form['name1'],
        'phone':           request.form['phone1'],
        'email':           request.form['email1'],
        'dept':             request.form['program1'],
        'EngineerFocus':      request.form['optradio'],
        'name2':            request.form['name2'],
        'phone2':          request.form['phone2'],
        'email2':            request.form['email2'],
        'dept2':    request.form['program2'],
        'sName':              request.form['name3'],
        'sPhone':            request.form['phone3'],
        'sEmail':             request.form['email3'],
        'title':       request.form['projectTitle'],
        'website':            request.form['projectLink'],
        'specReq': specialReq1,
        'specReq2': specialReq2,
        'specReq3': specialReq3,
        'specReq4': specialReq4,
        'specReq5': specialReq5,
        'description': request.form['projectDesc'],
        'majorReq': request.form.getlist('majorReq'),
        'supervision': request.form['optradio1'],
        'supervisionSource': request.form['optradio2'],
        'nature': request.form['optradio3'],
        'workAmount': request.form['optradio4'],
        'preselectStudent': request.form['preselectStudent'],
        'speedType': request.form['f1'],
        'accounting': request.form['f2'],
        'supervisedExp': request.form['optradio5'],
    })
    sqlUtil.insert_execute('faculty')
    sqlUtil.clear()

    app.logger.info('is sucessfully submitted')

    print("check")

    fName = request.form['name1']
    profId = sqlUtil.select_one("SELECT `id` FROM `faculty` WHERE `name` = \"fName\"")
    print(profId)
    sqlUtil.batch_insert_push({
        'projectName':             request.form['projectTitle'],
        'ProfessorID':           profId,
        'webLink':           request.form['projectLink'],
        'completeDescription':             request.form['projectDesc'],
        'req1':      specialReq1,
        'req2':            specialReq2,
        'req3':          specialReq3,
        'req4':          specialReq4,
        'req5':    specialReq5
    })

    sqlUtil.insert_execute('project')
    sqlUtil.clear()

    return json.dumps({'message': 'Faculty info saved successfully !'})
