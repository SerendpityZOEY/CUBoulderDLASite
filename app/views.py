from app import app
from flask import render_template, request, json, redirect, url_for, Response
from flaskext.mysql import MySQL
import MysqlUtil
import random
import string
import uuid
import hashlib
from hashlib import sha512
import datetime
from collections import defaultdict, Counter
import os

sqlUtil = MysqlUtil.MysqlUtil(app)
sqlUtil.use_account('developer')
sqlUtil.use_database('SEDB')


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
    data = sqlUtil.select_all("SELECT `StuMajors`,`ProjName`, `ManReqs`, `OptReqs` FROM `PROJECT_INFO`")
    # print data
    majors = sqlUtil.select_all("SELECT `M_Id`, `Acronym`, `FullName` FROM `MAJOR`")
    return render_template("student.html", data=json.dumps(data), majors=majors)


@app.route('/project', methods=['GET'])
def project():
    data = []
    dic = dict(sqlUtil.select_all("SELECT `D_Id`, `FullName` FROM `DEPT`"))
    major = sqlUtil.select_all("SELECT `M_Id`, `FullName` FROM `MAJOR`")
    dic_M = dict(major)
    # cursor.execute("SELECT * FROM `project`")
    # projects = cursor.fetchall()
    projects = sqlUtil.select_all(
        "SELECT `PFName`,`PFPhone`,`PFEmail`,`PFDept`,`SFName`,`SFPhone`,`SFEmail`,`GradName`,`GradPhone`,`GradEmail`,`ProjName`,`LongDesc`,`WebLink`,`ManReqs`,`OptReqs`,`StuMajors` FROM PROJECT_INFO")
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
        for i, r in enumerate(ManReqs.strip().split('$;^')):
            Req = Req + str(i + 1) + '.' + r + '\n'
        if OptReqs:
            Req += 'Nice to have:\n'
            for i, r in enumerate(OptReqs.strip().split('$;^')):
                Req = Req + str(i + 1) + '.' + r + '\n'
                # app.logger.info(StuMajors)
                Maj = ''
                if StuMajors!='':
                    for m in StuMajors.split(','):
                        Maj=Maj+dic_M[int(m)]+','
        data.append(
            [ProjName, contact, dic[PFDept], WebLink if WebLink is not None else u"", LongDesc, Req, Maj])
        # app.logger.info(data)
    return render_template("project.html", data=json.dumps(data), major=json.dumps(major))


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
    Manreqs = specialReq1 + '$;^' + specialReq2 + '$;^' + specialReq3 + '$;^' + specialReq4 + '$;^' + specialReq5
    sqlUtil.batch_insert_push({
        'PFName': request.form.get('name1'),
        'PFPhone': request.form.get('phone1'),
        'PFEmail': request.form.get('email1'),
        'PFDept': request.form.get('program1'),
        'HasFocus': request.form.get('HasFocus'),
        'SFName': request.form.get('name2'),
        'SFPhone': request.form.get('phone2'),
        'SFEmail': request.form.get('email2'),
        'GradName': request.form.get('name3'),
        'GradPhone': request.form.get('phone3'),
        'GradEmail': request.form.get('email3'),
        'ProjName': request.form.get('projectTitle'),
        'LongDesc': request.form.get('projectDesc'),
        'WebLink': request.form.get('projectLink'),
        'ManReqs': Manreqs,
        'OptReqs': Manreqs,
        'StuMajors': ','.join(request.form.getlist('majorReq')),
        'AmtOfSup': request.form.get('AmtOfSup'),
        'SupBy': request.form.get('SupBy'),
        'NatureOfWork': request.form.get('NatureOfWork'),
        'AmtOfPreWork': request.form.get('AmtOfPreWork'),
        'RevStus': request.form.get('preselectStudent'),
        'SpeedType': request.form.get('SpeedType'),
        'AcctContace': request.form.get('AcctContace'),
        'DidSup': request.form.get('DidSup')
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
    gender_dic = {0:'male', 1:'female'}
    origin_dic = {0:'yes', 1:'no', 2:'N/A'}
    race_dic = {1:'American Indian or Alaskan',2:'Black or African-American',3:'Native Hawaiian or other Pacific Islander',\
    4:'Asian',5:'White',6:'Other',7:'N/A'}
    major = sqlUtil.select_all("SELECT `M_Id`, `Acronym` FROM `MAJOR`")
    major_dic = dict(major)
    level_dic = {1:'freshman', 2:'sophomore', 3:'junior', 4:'senior', 5:'fifth'}
    re_dic = {0:'No',1:'Yes',None:''}

    applications = sqlUtil.select_all("SELECT `S_Id`, `Pr1_P_Id`, `Pr2_P_Id`, `Pr3_P_Id`, `Pr4_P_Id`, `Pr5_P_Id` FROM `APPLICATION`")
    student_info = sqlUtil.select_all("SELECT `S_Id`, `Name`, `Gender`, `Origin`, `Race`,\
                                 `Email`, `PrimaryMajor`, `StudentNumber`, `GPA`, `Level`\
                                  , `ResearchExperience` FROM `STUDENT`")
    student_info = dict((e[0],e[1:]) for e in student_info)
    project = sqlUtil.select_all("SELECT `P_Id`,`ProjName` FROM `PROJECT_INFO`")
    project_name = dict(project)
    students = []
    for application in applications:
        row = list(student_info[application[0]])
        projects = getDetail(application[1:], project_name)
        row[1],row[2], row[5], row[8], row[9] = gender_dic[row[1]], origin_dic[row[2]], major_dic[row[5]], level_dic[row[8]], re_dic[row[9]]
        row[3] = ', '.join([race_dic[int(r)] for r in row[3].split(',')])
        students.append(row+projects)
    return render_template("matrix.html", students=json.dumps(students), s_id_name=json.dumps([(e[0],e[1][0]) for e in student_info.items()]), p_id_name=json.dumps(project), major=json.dumps(major))


def getDetail(projectId, dic):
    list = []
    for i in projectId:
        if i is not None:
            list.append(dic[i])
        else:
            list.append('')
    return list

@app.route('/assign', methods=['POST'])
def assign():
    sid = request.form['student']
    pid = request.form['project']
    app.logger.info(type(sid))
    app.logger.info(pid)
    if sid and pid:
        sqlUtil.insert_push('S_Id',int(sid))
        sqlUtil.insert_push('P_Id',int(pid))
        sqlUtil.insert_execute('ASSIGNED')
        sqlUtil.clear()
    return redirect(request.referrer)

@app.route('/results')
def results():
    data = sqlUtil.select_all("SELECT `S_Id`,`P_Id` FROM `ASSIGNED`")
    students = sqlUtil.select_all("SELECT `S_Id`, `Name` FROM STUDENT")
    projects = sqlUtil.select_all("SELECT `P_Id`, `ProjName` FROM `PROJECT_INFO`")
    stuDict = dict()
    projDict = dict()
    res = []
    for person in students:
        stuDict[person[0]] = person[1]

    for proj in projects:
        projDict[proj[0]] = proj[1]

    for i in data:
        # print(i[0], stuDict[i[0]], projDict[i[1]])
        res.append([i[0], stuDict[i[0]], projDict[i[1]]])
    return render_template("result.html", data=json.dumps(res), projects=projects)

@app.route('/update', methods=['POST'])
def update():
    res = request.json
    print('update',res['S_Id'],'P_Id',res['P_Id'])
    sqlUtil.update_one("UPDATE `ASSIGNED` SET `P_Id`="+ str(res['P_Id']) +" WHERE `S_Id`="+str(res['S_Id']))
    return render_template("result.html")

@app.route('/autoMatch', methods=['POST'])
def autoMatch():
    Assigned = sqlUtil.select_all('select `S_Id`,`P_Id` from ASSIGNED')
    if len(Assigned) > 0:
        Assigned_S_Ids, Assigned_P_Ids = zip(*Assigned)
    else:
        Assigned_S_Ids, Assigned_P_Ids = [], []
    Assigned_S_Ids = set(Assigned_S_Ids)
    Assigned_P_Ids = Counter(Assigned_P_Ids)
    # print Assigned_S_Ids
    print Assigned_P_Ids

    """Select all the students whose GPA is above 3.0"""
    Students = sqlUtil.select_all(
        'select `S_Id`, `StudentNumber` from STUDENT where GPA > 3.0')
    # This dic is for reserved student mapping (studentNum: S_Id)
    StudentDict = defaultdict(lambda: {"S_Id": None})
    for S_Id, StudentNumber in Students:
        StudentDict[str(StudentNumber)]["S_Id"] = S_Id


    """Assign reserved students"""
    ProjectsWithReservation = sqlUtil.select_all(
        'select `P_Id`, `RevStus` from PROJECT_INFO where RevStus is not NULL')
    for P_Id, RevStuds in ProjectsWithReservation:
        RevStudsLst = RevStuds.split(',')
        for student in RevStudsLst:
            if StudentDict.has_key(student.strip()) and StudentDict[student]["S_Id"] not in Assigned_S_Ids:
                sqlUtil.insert_many_push(
                    {"S_Id": StudentDict[student]["S_Id"], "P_Id": P_Id})
                Assigned_S_Ids.add(StudentDict[student]["S_Id"])
                Assigned_P_Ids[P_Id] += 1
    if len(sqlUtil.data_list) > 0:
        sqlUtil.insert_many_execute("ASSIGNED")
        sqlUtil.clear()

    # print Assigned_S_Ids
    # print Assigned_P_Ids


    """Get students who graduate one year later and GPA above 3.0"""
    now = datetime.datetime.now()
    date2Compare = now + datetime.timedelta(days=365)
    date2CompareStr = str(date2Compare.year) + "-" + \
        str(date2Compare.month) + "-" + "01" + " 00:00:00"
    Students = sqlUtil.select_all(
        'select `S_Id`,`Gender`,`Origin`,`PrimaryMajor`,`SecondaryMajor`,`GPA`,`level`,`AppliedBefore` from STUDENT where GraduationDate > "{}" and GPA > 3.0'.format(date2CompareStr))
    StudentDict = defaultdict(lambda: {"Projects": [], "Priority": 0})
    S_Id_set = set([0])
    print StudentDict
    for S_Id, Gender, Origin, PrimaryMajor, SecondaryMajor, GPA, level, AppliedBefore in Students:
        if S_Id not in Assigned_S_Ids:
            StudentDict[S_Id]["Gender"] = Gender
            StudentDict[S_Id]["Origin"] = Origin
            StudentDict[S_Id]["PrimaryMajor"] = PrimaryMajor
            StudentDict[S_Id]["SecondaryMajor"] = SecondaryMajor
            StudentDict[S_Id]["GPA"] = GPA
            StudentDict[S_Id]["level"] = level
            StudentDict[S_Id]["AppliedBefore"] = AppliedBefore
            S_Id_set.add(S_Id)

    print StudentDict


    """Eliminate Projects no one applied"""
    AppliedProjects = []
    Applications = sqlUtil.select_all(
        'select `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id` from APPLICATION')
    for Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id in Applications:
        AppliedProjects += Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id, 
    AppliedProjectsCounter = Counter(AppliedProjects)
    print 'select `S_Id`, `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id`, `OptReqsCheck` from APPLICATION where S_Id in (%s)' % (", ".join([str(x) for x in S_Id_set]))
    Applications = sqlUtil.select_all(
        'select `S_Id`, `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id`, `OptReqsCheck` from APPLICATION where S_Id in (%s)' % (", ".join([str(x) for x in S_Id_set])))
    for S_Id, Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id, OptReqsCheck in Applications:
        StudentDict[S_Id][
            "Projects"] += Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id
        StudentDict[S_Id]["OptReqsCheck"] = OptReqsCheck
        # Projects = sqlUtil.select_all(
        # "select `P_Id` from PROJECT_INFO where P_Id in (%s)" % (", ".join([str(x) for x in AppliedProjects - set([None])])))
    print '\n\n'
    print StudentDict
    print AppliedProjects
    print AppliedProjectsCounter


    """Build priority"""
    for key in StudentDict.iterkeys():
        print '\n\n'

        print StudentDict[key]
        if StudentDict[key]["AppliedBefore"] == 0:
            StudentDict[key]["Priority"] += 1
        if StudentDict[key]["Gender"] == 1:
            StudentDict[key]["Priority"] += 1
        if StudentDict[key]["Origin"] == 0:
            StudentDict[key]["Priority"] += 1
        if StudentDict[key]["level"] == 4 or StudentDict[key]["level"] == 5:
            StudentDict[key]["Priority"] += 1
        StudentDict[key]["Priority"] += StudentDict[key]["GPA"] * 1.1 ** StudentDict[key]["level"]

    StudentsSorted = sorted(StudentDict.items(), key = lambda student: student[1]["Priority"], reverse=True)
    for student in StudentsSorted:
        Projects = [x for x in student[1]["Projects"] if x is not None]
        P_Id_choose = 0
        min_Applied = 10000000
        min_Applied_P_Id = 0
        min_Assigned = 10000000
        min_Assigned_P_Id = 0
        for idx, P_Id in enumerate(Projects):
            if P_Id not in Assigned_P_Ids.keys():
                P_Id_choose = P_Id
                # print Assigned_P_Ids
                Assigned_P_Ids[P_Id] += 1
                break
            if idx < 3 and AppliedProjectsCounter[P_Id] < min_Applied:
                min_Applied = AppliedProjectsCounter[P_Id]
                min_Applied_P_Id = P_Id
            if Assigned_P_Ids[P_Id] < min_Assigned:
                min_Assigned = Assigned_P_Ids[P_Id]
                min_Assigned_P_Id = P_Id
        if P_Id_choose == 0:
            if min_Applied_P_Id != 0:
                P_Id_choose = min_Applied_P_Id
            else:
                P_Id_choose = min_Assigned_P_Id
        sqlUtil.insert_many_push({"S_Id": student[0], "P_Id": P_Id_choose})
    if len(sqlUtil.data_list) > 0:
        sqlUtil.insert_many_execute("ASSIGNED")
        
    return url_for('results')

    """
    Mandatory:
    Remove all the student GPA < 3.0
    Assign reserved students 
    Elimate project no one applied 
    Student's graduation date must be one year later


    Priority:
    Applied DLA before
    Special requirements
    Num of applicants, fewest first only if student make it in the first 3 choice


    Carefully Consideration:
    Last year student 
    Gender balance(female first)
    minority first
    First and Second choice first 


    Higher GPA 

    Program accept minor major(fewest program prefer) first assigned
    """


@app.route('/getCSV', methods=['GET','POST'])
def download():
    # print('start downloading')
    os.system('python exportCsv.py'),
    file = open('result.csv', 'r')
    csv = file.readlines()
    # print csv
    return Response("".join(csv), mimetype="text/csv", headers={"Content-disposition":"attachment;filename=result.csv"})
    # return send_file("".join(csv),
    #                  mimetype='text/csv',
    #                  attachment_filename='Adjacency.csv',
    #                  as_attachment=True)
