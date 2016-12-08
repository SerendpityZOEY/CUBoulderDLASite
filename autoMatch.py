from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil
import datetime
from collections import defaultdict, Counter


sql = MysqlUtil(app)
sql.use_account('developer')
sql.use_database('NewSE')


Assigned = sql.select_all('select `S_Id`,`P_Id` from ASSIGNED')
if len(Assigned) > 0:
    Assigned_S_Ids, Assigned_P_Ids = zip(*Assigned)
else:
    Assigned_S_Ids, Assigned_P_Ids = [], []
Assigned_S_Ids = set(Assigned_S_Ids)
Assigned_P_Ids = Counter(Assigned_P_Ids)
# print Assigned_S_Ids
print Assigned_P_Ids

"""Select all the students whose GPA is above 3.0"""
Students = sql.select_all(
    'select `S_Id`, `StudentNumber` from STUDENT where GPA > 3.0')
# This dic is for reserved student mapping (studentNum: S_Id)
StudentDict = defaultdict(lambda: {"S_Id": None})
for S_Id, StudentNumber in Students:
    StudentDict[str(StudentNumber)]["S_Id"] = S_Id


"""Assign reserved students"""
ProjectsWithReservation = sql.select_all(
    'select `P_Id`, `RevStus` from PROJECT_INFO where RevStus is not NULL')
for P_Id, RevStuds in ProjectsWithReservation:
    RevStudsLst = RevStuds.split(',')
    for student in RevStudsLst:
        if StudentDict.has_key(student.strip()) and StudentDict[student]["S_Id"] not in Assigned_S_Ids:
            sql.insert_many_push(
                {"S_Id": StudentDict[student]["S_Id"], "P_Id": P_Id})
            Assigned_S_Ids.add(StudentDict[student]["S_Id"])
            Assigned_P_Ids[P_Id] += 1
if len(sql.data_list) > 0:
    sql.insert_many_execute("ASSIGNED")
    sql.clear()

# print Assigned_S_Ids
# print Assigned_P_Ids


"""Get students who graduate one year later and GPA above 3.0"""
now = datetime.datetime.now()
date2Compare = now + datetime.timedelta(days=365)
date2CompareStr = str(date2Compare.year) + "-" + \
    str(date2Compare.month) + "-" + "01" + " 00:00:00"
Students = sql.select_all(
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
Applications = sql.select_all(
    'select `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id` from APPLICATION')
for Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id in Applications:
    AppliedProjects += Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id, 
AppliedProjectsCounter = Counter(AppliedProjects)
print 'select `S_Id`, `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id`, `OptReqsCheck` from APPLICATION where S_Id in (%s)' % (", ".join([str(x) for x in S_Id_set]))
Applications = sql.select_all(
    'select `S_Id`, `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id`, `OptReqsCheck` from APPLICATION where S_Id in (%s)' % (", ".join([str(x) for x in S_Id_set])))
for S_Id, Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id, OptReqsCheck in Applications:
    StudentDict[S_Id][
        "Projects"] += Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id
    StudentDict[S_Id]["OptReqsCheck"] = OptReqsCheck
    # Projects = sql.select_all(
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
    sql.insert_many_push({"S_Id": student[0], "P_Id": P_Id_choose})
if len(sql.data_list) > 0:
    sql.insert_many_execute("ASSIGNED")
    
    

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
