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


dic={1:'Aerospace Engineering', 2:'Applied Math', 3: 'Chemical & Biological Engineering', \
4: 'Civil, Environmental and Architectural Engineering', 5: 'Computer Science', 6: 'Electrical, Computer and Energy Engineering', \
7: 'Physics', 8: 'Environmental Engineering', 9: 'Mechanical Engineering', \
10: 'Colorado Space Grant', 11: 'Engineering Education', 12: 'ATLAS'}

majordict = {0:'Aerospace Engineering', 1:'Applied Math', 2:'Architectural Engineering', 3: 'Chemical Engineering', \
4: 'Chemical & Biological Engineering', 5: 'Civil Engineering', 6: 'Computer Science', \
7: 'Electrical Engineering', 8: 'Electrical and Computer Engineering', 9: 'Engineering Physics', \
10: 'Environmental Engineering', 11: 'Engineering Plus', 12: 'Mechanical Engineering', 13: 'Technology, Arts and Media'}
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/student')
def student():
    app.logger.info('waiting for input in student page')
    data = sqlUtil.select_all("SELECT `P_Id`,`ProjName` FROM `PROJECT_INFO`")
    return render_template("student.html", data=data)


@app.route('/project', methods=['GET'])
def project():
    data=[]
    # cursor.execute("SELECT * FROM `project`")
    # projects = cursor.fetchall()
    projects = sqlUtil.select_all("SELECT `PFName`,`PFPhone`,`PFEmail`,`PFDept`,`SFName`,`SFPhone`,`SFEmail`,`GradName`,`GradPhone`,`GradEmail`,`ProjName`,`LongDesc`,`WebLink`,`ManReqs`,`OptReqs`,`StuMajors` FROM `PROJECT_INFO`")
    # app.logger.info(projects)
    for PFName, PFPhone, PFEmail, PFDept, SFName, SFPhone, SFEmail,GradName, GradPhone, GradEmail, ProjName, LongDesc, WebLink, ManReqs, OptReqs, StuMajors in projects:
        # cursor.execute("SELECT `name1`, `program1` FROM `faculty` WHERE `id`='{prid}'".format(prid=prid))
        # professorName, department = cursor.fetchone()
        contact = PFName+':'+PFPhone+'\n'+PFEmail+'\n'
        if SFName:
            if SFPhone and SFEmail:
                contact += SFName+':'+SFPhone+'\n'+SFEmail+'\n'
            elif SFPhone and not SFEmail:
                contact += SFName+':'+SFPhone+'\n'
            elif not SFPhone and SFEmail:
                contact += SFName+':'+SFEmail+'\n'
        if GradName:
            if GradPhone and GradEmail:
                contact += GradName+':'+GradPhone+'\n'+GradEmail+'\n'
            elif GradPhone and not GradEmail:
                contact += GradName+':'+GradPhone+'\n'
            elif GradPhone and not GradEmail:
                contact += GradName+':'+GradEmail+'\n'
        Req = ''
        for i, r in enumerate(ManReqs.rstrip(';').split(';')):
            Req=Req+str(i+1)+'.'+r+'\n'
        if OptReqs:
            Req+='Nice to have:\n'
            for i, r in enumerate(OptReqs.rstrip(';').split(';')):
                Req=Req+str(i+1)+'.'+r+'\n'
        app.logger.info(StuMajors)
        Maj = ''
        for i, m in enumerate(StuMajors.split(';')):
            Maj=Maj+majordict[int(m)]+','
        data.append([str(ProjName), contact, dic[int(PFDept)], str(WebLink) if WebLink is not None else "",str(LongDesc),Req, Maj])
        #app.logger.info(data)
    return render_template("project.html", data=json.dumps(data))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    sn =  request.form['SN']
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

@app.route('/navigation')
def navigation():
    app.logger.info('waiting for input for student id')
    return render_template("navigation.html")

@app.route('/lookup', methods = ['GET', 'POST'])
def lookup():
    studentID = request.form['studentID']
    print("The student ID '" + studentID + "'")

    data=[]

    studentID, studentName, gender, origin, race, phoneNumber, email, address, major, studentNumber, GPA, level, graduateDate, researchExperience, appliedBefore = sqlUtil.select_one("SELECT * FROM `student` WHERE `studentID`='{studentID}'".format(studentID=studentID))
    projectTitles = sqlUtil.select_all("SELECT * FROM `application` WHERE `Sid`='{studentID}'".format(studentID=studentID))

    project_list = []

    for Aid, Sid, Priority, P_Id in projectTitles:

        project_title = sqlUtil.select_one("SELECT `ProjName` FROM `PROJECT_INFO` WHERE `P_Id`='{P_Id}'".format(P_Id=P_Id))
        project_list.append("{}+{}".format(project_title, Priority))
    print("Project_list: {}".format(project_list))
    data.append([studentName, gender, origin, race, phoneNumber, email, address, major, studentNumber, GPA, level, graduateDate, researchExperience, appliedBefore, project_list])

    return render_template("display.html", data=json.dumps(data))

@app.route('/fsubmit', methods=['GET', 'POST'])
def f_submit():
    print("Enter f_submit")

    specialReq1 = request.form.get('specialReq1', None)
    if specialReq1 is None:
        specialReq1 = ""
    specialReq2 = request.form.get('specialReq2', None)
    if specialReq2 is None:
        specialReq2 = ""
    specialReq3 = request.form.get('specialReq3', None)
    if specialReq3 is None:
        specialReq3 = ""
    specialReq4 = request.form.get('specialReq4', None)
    if specialReq4 is None:
        specialReq4 = ""
    specialReq5 = request.form.get('specialReq5', None)
    if specialReq5 is None:
        specialReq5 = ""
    Manreqs = specialReq1+';'+specialReq2+';'+specialReq3+';'+specialReq4+';'+specialReq5
    sqlUtil.batch_insert_push({
        'PFName':             str(request.form['name1']),
        'PFPhone':           str(request.form['phone1']),
        'PFEmail':           str(request.form['email1']),
        'PFDept':             str(request.form['program1']),
        'HasFocus':      str(request.form['optradio']),
        'SFName':            str(request.form['name2']),
        'SFPhone':          str(request.form['phone2']),
        'SFEmail':            str(request.form['email2']),
        'GradName':              str(request.form['name3']),
        'GradPhone':            str(request.form['phone3']),
        'GradEmail':             str(request.form['email3']),
        'ProjName':       str(request.form['projectTitle']),
        'LongDesc': str(request.form['projectDesc']),
        'WebLink':            str(request.form['projectLink']),
        'ManReqs':            str(Manreqs),
        'StuMajors': ';'.join(request.form.getlist('majorReq')),
        'AmtOfSup': request.form['optradio1'],
        'SupBy': request.form['optradio2'],
        'NatureOfWork': request.form['optradio3'],
        'AmtOfPreWork': request.form['optradio4'],
        'RevStus': str(request.form['preselectStudent']),
        'SpeedType': str(request.form['f1']),
        'AcctContace': str(request.form['f2']),
        'DidSup': request.form['optradio5']
    })
    sqlUtil.insert_execute('PROJECT_INFO')
    sqlUtil.clear()

    app.logger.info('is sucessfully submitted')


    # print("check")

    # fName = request.form['name1']
    # profId = sqlUtil.select_one('id', 'faculty', 'name', fName)
    # print(profId)
    # sqlUtil.batch_insert_push({
    #     'projectName':             request.form['projectTitle'],
    #     'ProfessorID':           profId,
    #     'webLink':           request.form['projectLink'],
    #     'completeDescription':             request.form['projectDesc'],
    #     'req1':      specialReq1,
    #     'req2':            specialReq2,
    #     'req3':          specialReq3,
    #     'req4':          specialReq4,
    #     'req5':    specialReq5
    # })

    # sqlUtil.insert_execute('project')
    # sqlUtil.clear()

    return json.dumps({'message': 'Faculty info saved successfully !'})
