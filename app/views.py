from app import app
from flask import render_template, request, json, redirect, url_for
from flaskext.mysql import MySQL
import MysqlUtil
import random
import string
import uuid
import hashlib
from hashlib import sha512

sqlUtil = MysqlUtil.MysqlUtil(app)
sqlUtil.use_account('developer')
sqlUtil.use_database('NewSE')


def hash_secret(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex[:16]
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()[:16] + salt


def check_secret(hashed_password, user_password):
    password = hashed_password[:16]
    salt = hashed_password[16:32]

    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()[:16]

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/navigation')
def navigation():
    return render_template("navigation.html")


@app.route('/student')
def student():
    app.logger.info('waiting for input in student page')
    data = sqlUtil.select_all("SELECT `PFDept`,`ProjName` FROM `PROJECT_INFO`")
    majors = sqlUtil.select_all("SELECT `M_Id`, `Acronym`, `FullName` FROM `MAJOR`")
    return render_template("student.html", data=json.dumps(data), majors=majors)


@app.route('/project', methods=['GET'])
def project():
    data = []
    dic = dict(sqlUtil.select_all("SELECT `D_Id`, `FullName` FROM `DEPT`"))
    # cursor.execute("SELECT * FROM `project`")
    # projects = cursor.fetchall()
    projects = sqlUtil.select_all(
        "SELECT `PFName`,`PFPhone`,`PFEmail`,`PFDept`,`SFName`,`SFPhone`,`SFEmail`,`GradName`,`GradPhone`,`GradEmail`,`ProjName`,`LongDesc`,`WebLink`,`ManReqs`,`OptReqs`,`StuMajors` FROM `PROJECT_INFO`")
    # app.logger.info(projects)
    for PFName, PFPhone, PFEmail, PFDept, SFName, SFPhone, SFEmail, GradName, GradPhone, GradEmail, ProjName, LongDesc, WebLink, ManReqs, OptReqs, StuMajors in projects:
        # cursor.execute("SELECT `name1`, `program1` FROM `faculty` WHERE `id`='{prid}'".format(prid=prid))
        # professorName, department = cursor.fetchone()
        contact = PFName + ':' + PFPhone + '\n' + PFEmail + '\n'
        if SFName:
            if SFPhone and SFEmail:
                contact += SFName + ':' + SFPhone + '\n' + SFEmail + '\n'
            elif SFPhone and not SFEmail:
                contact += SFName + ':' + SFPhone + '\n'
            elif not SFPhone and SFEmail:
                contact += SFName + ':' + SFEmail + '\n'
        if GradName:
            if GradPhone and GradEmail:
                contact += GradName + ':' + GradPhone + '\n' + GradEmail + '\n'
            elif GradPhone and not GradEmail:
                contact += GradName + ':' + GradPhone + '\n'
            elif GradPhone and not GradEmail:
                contact += GradName + ':' + GradEmail + '\n'
        Req = ''
        for i, r in enumerate(ManReqs.rstrip(';').split(';')):
            Req = Req + str(i + 1) + '.' + r + '\n'
        if OptReqs:
            Req += 'Nice to have:\n'
            for i, r in enumerate(OptReqs.rstrip(';').split(';')):
                Req = Req + str(i + 1) + '.' + r + '\n'
                # app.logger.info(StuMajors)
                # Maj = ''
                # for i, m in enumerate(StuMajors.split(';')):
                # Maj=Maj+majordict[int(m)]+','
        data.append(
            [ProjName, contact, dic[PFDept], WebLink if WebLink is not None else u"", LongDesc, Req])  # , Maj])
        # app.logger.info(data)
    return render_template("project.html", data=json.dumps(data))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    sqlUtil.batch_insert_push({
        'Name': None if request.form.get('name', "") == "" else request.form['name'],
        'Gender': request.form.get('gender', None),
        'Origin': request.form.get('origin', None),
        'Race': ",".join(request.form.getlist('race')) if request.form.get('race', None) is not None else None,
        'Phone': None if request.form.get('phone', "") == "" else request.form['phone'],
        'Email': None if request.form.get('email', "") == "" else request.form['email'],
        'Address': None if request.form.get('address', "") == "" else request.form['address'],
        'SumPhone': None if request.form.get('Sumphone', "") == "" else request.form['Sumphone'],
        'SumEmail': None if request.form.get('Sumemail', "") == "" else request.form['Sumemail'],
        'SumAddress': None if request.form.get('Sumaddress', "") == "" else request.form['Sumaddress'],
        'PrimaryMajor': request.form.get('major', None),
        'SecondaryMajor': None if request.form.get('major2', "") == "" else request.form['major2'],
        'studentNumber': None if request.form.get('SN', "") == "" else request.form['SN'],
        'GPA': None if request.form.get('GPA', "") == "" else request.form['GPA'],
        'level': request.form.get('level', None),
        'GraduationDate': None if request.form.get('date', "") == "" else request.form['date'] + '-01',
        'ResearchExperience': request.form.get('researchExp', None),
        'AppliedBefore': request.form.get('appliedBefore', None),
        'EmploymentPlanned': None if request.form.get('plan', "") == "" else request.form['plan'],
        'BackgroundCheck': None if request.form.get('backCheck', "") == "" else request.form['backCheck'],
        'Discrimination': request.form.get('discrimination', None),
        'SSN': None if request.form.get('SSN', "") == "" else request.form['SSN'],
        "Skills": None if request.form.get('skill1', "") == "" else "^;$".join(
            (request.form.get(field, "") for field in ("skill1", "skill2", "skill3"))),
    })

    sid = sqlUtil.insert_execute('STUDENT')
    sqlUtil.clear()
    sqlUtil.batch_insert_push({
        'S_Id': sid,
        'Pr1_P_Id': None if request.form.get('p1', "") == "" else request.form['p1'],
        'Pr2_P_Id': None if request.form.get('p2', "") == "" else request.form['p2'],
        'Pr3_P_Id': None if request.form.get('p3', "") == "" else request.form['p3'],
        'Pr4_P_Id': None if request.form.get('p4', "") == "" else request.form['p4'],
        'Pr5_P_Id': None if request.form.get('p5', "") == "" else request.form['p5'],
        'Secret': hash_secret("" if request.form.get('studentSecret', "") == "" else request.form['studentSecret'])
    })
    sqlUtil.insert_execute('APPLICATION')
    # for i, p in enumerate(['p1', 'p2', 'p3', 'p4', 'p5']):
    #     sqlUtil.batch_insert_push({'Priority': i+1, 'ProjectID': (request.form.get(p, None))[0]})
    #     sqlUtil.insert_execute('application')
    #     # Don clear, since we need to reuse 'Sid' field
    sqlUtil.clear()

    return url_for('success')


@app.route('/success')
def success():
    return render_template("Success.html")


@app.route('/error')
def error():
    return render_template("Error.html")


@app.route('/faculty')
def faculty():
    # app.logger.info('waiting for input in teacher page')
    return render_template("faculty.html")


@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    studentNumber = request.form['studentID']
    studentSecret = request.form['studentSecret']
    # print("The student ID '" + studentID + "'")
    hashed_secret = hash_secret(studentSecret)
    print("The hash '" + hashed_secret + "'")

    data = []

    studentID, studentName, gender, origin, race, phoneNumber, email, address, sumPhone, sumEmail, sumAddress, major, secondaryMajor, studentNumber, GPA, level, GraduationDate, researchExperience, appliedBefore, employmentPlanned, backgroundCheck, discrimination, ssn, skills = sqlUtil.select_one(
        "SELECT * FROM `STUDENT` WHERE `StudentNumber`='{studentNumber}'".format(studentNumber=studentNumber))
    print("graduateDate: {}".format(GraduationDate))
    #projectTitles = sqlUtil.select_all(
    #    "SELECT * FROM `APPLICATION` WHERE `S_Id`='{studentID}'".format(studentID=studentID))

    #Aid, Sid, Priority, P_Id, Secret
    A_Id, S_Id, Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id, OptReqsCheck, Secret, createdTime, lastUpdatedTime = sqlUtil.select_one(
        "SELECT * FROM `APPLICATION` WHERE `S_Id`='{studentID}'".format(studentID=studentID))

    print("lastUpdatedTime: {}".format(lastUpdatedTime))

    majors = sqlUtil.select_all("SELECT `M_Id`, `Acronym`, `FullName` FROM `MAJOR`")

    if   check_secret(Secret, studentSecret):
       print (" YaaaaaaaaaY")

       project_title1 = sqlUtil.select_one("SELECT `ProjName` FROM `PROJECT_INFO` WHERE `P_Id`='{Pr1_P_Id}'".format(Pr1_P_Id=Pr1_P_Id))
       project_title2 = sqlUtil.select_one("SELECT `ProjName` FROM `PROJECT_INFO` WHERE `P_Id`='{Pr2_P_Id}'".format(Pr2_P_Id=Pr2_P_Id))
       project_title3 = sqlUtil.select_one("SELECT `ProjName` FROM `PROJECT_INFO` WHERE `P_Id`='{Pr3_P_Id}'".format(Pr3_P_Id=Pr3_P_Id))
       project_title4 = sqlUtil.select_one("SELECT `ProjName` FROM `PROJECT_INFO` WHERE `P_Id`='{Pr4_P_Id}'".format(Pr4_P_Id=Pr4_P_Id))
       project_title5 = sqlUtil.select_one("SELECT `ProjName` FROM `PROJECT_INFO` WHERE `P_Id`='{Pr5_P_Id}'".format(Pr5_P_Id=Pr5_P_Id))



       data.append([studentName, gender, origin, race, phoneNumber, email, address, sumPhone, sumEmail, sumAddress, major, secondaryMajor,  studentNumber, GPA, level, GraduationDate, researchExperience, appliedBefore, employmentPlanned, backgroundCheck, discrimination, ssn, skills, project_title1, project_title2, project_title3, project_title4, project_title5])
       return render_template("display.html", data=json.dumps(data), majors=json.dumps(majors))

    message = "Wrong Secret"

    return render_template("navigation.html", message=message)


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
    Manreqs = specialReq1 + ';' + specialReq2 + ';' + specialReq3 + ';' + specialReq4 + ';' + specialReq5
    sqlUtil.batch_insert_push({
        'PFName': str(request.form['name1']),
        'PFPhone': str(request.form['phone1']),
        'PFEmail': str(request.form['email1']),
        'PFDept': str(request.form['program1']),
        'HasFocus': str(request.form['HasFocus']),
        'SFName': str(request.form['name2']),
        'SFPhone': str(request.form['phone2']),
        'SFEmail': str(request.form['email2']),
        'GradName': str(request.form['name3']),
        'GradPhone': str(request.form['phone3']),
        'GradEmail': str(request.form['email3']),
        'ProjName': str(request.form['projectTitle']),
        'LongDesc': str(request.form['projectDesc']),
        'WebLink': str(request.form['projectLink']),
        'ManReqs': str(Manreqs),
        'StuMajors': ';'.join(request.form.getlist('majorReq')),
        'AmtOfSup': request.form['AmtOfSup'],
        'SupBy': request.form['SupBy'],
        'NatureOfWork': request.form['NatureOfWork'],
        'AmtOfPreWork': request.form['AmtOfPreWork'],
        'RevStus': str(request.form['preselectStudent']),
        'SpeedType': str(request.form['SpeedType']),
        'AcctContace': str(request.form['AcctContace']),
        'DidSup': request.form['DidSup']
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

    # return json.dumps({'message': 'Faculty info saved successfully !'})
    return url_for('success')


@app.route('/matrix')
def matrix():
    applications = sqlUtil.select_all("SELECT `A_Id`,`S_Id` FROM `APPLICATION`")
    students = []
    dicts = {}
    for A_Id, S_Id in applications:
        row = sqlUtil.select_all("SELECT `Name`, `Gender`, `Origin`, `Race`, `Phone`, \
                                 `Email`, `Address`, `PrimaryMajor`, `StudentNumber`, `GPA`, `Level`\
                                  , `ResearchExperience` \
                                  FROM `STUDENT` WHERE `S_Id`=" + str(S_Id))
        projectInd = sqlUtil.select_all("SELECT `Pr1_P_Id`, `Pr2_P_Id`, `Pr3_P_Id`, `Pr4_P_Id`, `Pr5_P_Id` \
                                  FROM `APPLICATION` WHERE `A_Id`="+str(A_Id))
        projects = getDetail(projectInd)
        students.append(row[0]+(S_Id,))
        dicts[S_Id] = json.dumps(projects)
    return render_template("matrix.html", students=json.dumps(students), projects=json.dumps(dicts))

def getDetail(projectId):
    list = ()
    for i in projectId[0]:
        if i is not None:
            project = sqlUtil.select_one("ProjName", "PROJECT_INFO", "P_Id", i)
            list+=(project,)
    return list
