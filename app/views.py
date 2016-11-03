from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
import MysqlUtil

sqlUtil = MysqlUtil.MysqlUtil(app)
sqlUtil.use_account('developer')
sqlUtil.use_database('SETest')


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
          cursor.execute("SELECT name1, program1 FROM faculty WHERE id='%s'"%(prid))
          self.cursor.execute("UPDATE urls SET state=%d,content='%s' WHERE url='%s'"%(state,self.conn.escape_string(content),url))
          professorName, department = cursor.fetchone()
        # professorName, department = sqlUtil.select_one("SELECT `name1`, `program1` FROM `faculty` WHERE `id`='{prid}'".format(prid=prid))
        # professorName, department = str(professorName), dic[int(department)]
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

    sqlUtil.insert_execute('student');
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
    fName = request.form['name1']
    print("check 1")
    phone1 = request.form['phone1']
    print("check 2")

    email1 = request.form['email1']
    print("check 3")

    program1 = request.form['program1']  # int
    print("check 4")

    radio0 = request.form['optradio']  # string
    print("check 5")

    name2 = request.form['name2']
    print("check 6")

    phone2 = request.form['phone2']
    print("check 7")

    email2 = request.form['email2']
    print("check 8")

    program2 = request.form['program2']  # int
    print("check 9")

    name3 = request.form['name3']
    print("check 10")

    phone3 = request.form['phone3']
    print("check 11")

    email3 = request.form['email3']
    print("check 12")

    projectTitle = request.form['projectTitle']
    print("check 13")

    projectLink = request.form['projectLink']
    print("check 14")

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


    projectDesc = request.form['projectDesc']
    print("check 16")

    majorReq = request.form.getlist('majorReq')
    print("check 17")

    radio1 = request.form['optradio1']
    print("check 18")

    radio2 = request.form['optradio2']
    print("check 19")

    radio3 = request.form['optradio3']
    print("check 20")

    radio4 = request.form['optradio4']
    print("check 21")

    preselectStudent = request.form['preselectStudent']
    print("check 22")

    f1 = request.form['f1']
    print("check 23")

    f2 = request.form['f2']
    print("check 24")

    radio5 = request.form['optradio5']
    print("check 25")

    conn = mysql.connect()
    cursor = conn.cursor()
    print(fName, phone1, email1, program1, radio0, name2, phone2, email2, program2, name3, phone3, email3,
          projectTitle, projectLink, specialReq1, projectDesc, majorReq, radio1, radio2, radio3, radio4,
          preselectStudent, f1, f2, radio5)
    query = "INSERT INTO `faculty` (`name`, `phone`, `email`, `dept`, `EngineerFocus`, `name2`, \
            `phone2`, `email2`, `dept2`, `sName`, `sPhone`, `sEmail`, `title`, `website`, \
            `specReq`, `specReq2`, `specReq3`, `specReq4`, `specReq5`, `description`, `majorReq`, `supervision`, \
            `supervisionSource`, `nature`, `workAmount`, `preselectStudent`, \
            `speedType`, `accounting`, `supervisedExp`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"


    app.logger.info('is sucessfully submitted')
    cursor.execute(query,
                   (fName, phone1, email1, program1, radio0, name2, phone2, email2, program2, name3, phone3, email3,
                    projectTitle, projectLink, specialReq1, specialReq2, specialReq3, specialReq4, specialReq5,
                    projectDesc, majorReq, radio1, radio2, radio3, radio4,
                    preselectStudent, f1, f2, radio5))
    conn.commit()
    #submit to project table
    # fetch_id = "SELECT `id` FROM `faculty` WHERE `name` = \"fName\""
    # profId = cursor.execute(fetch_id)
    profId = sqlUtil.select_all("SELECT `id` FROM `faculty` WHERE `name` = \"fName\"")
    ProfessorID = int(profId)
    projectName = projectTitle
    webLink = projectLink
    req1 = specialReq1
    completeDescription = projectDesc
    req2 = specialReq2
    req3 = specialReq3
    req4 = specialReq4
    req5 = specialReq5
    project_query = "INSERT INTO `project` (`projectName`, `ProfessorID`, `webLink`, \
                    `completeDescription`, `req1`, `req2`, `req3`, `req4`, `req5`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    print(ProfessorID)
    cursor.execute(project_query, (projectName, int(ProfessorID), webLink,\
                    completeDescription, req1, req2, req3, req4, req5))
    conn.commit()

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps({'message': 'Faculty info saved successfully !'})
