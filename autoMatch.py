from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil
import datetime
from collections import defaultdict



sql = MysqlUtil(app)
sql.use_account('developer')
sql.use_database('NewSE')


Assigned = sql.select_all('select `S_Id`,`P_Id` from ASSIGNED')
Assigned_S_Ids, Assigned_P_Ids = zip(*Assigned)
Assigned_S_Ids = set(Assigned_S_Ids)
Assigned_P_Ids = set(Assigned_P_Ids)
# print Assigned_S_Ids
# print Assigned_P_Ids

"""Firstly select all the students whose GPA is above 3.0"""
Students = sql.select_all('select `S_Id`, `StudentNumber` from STUDENT where GPA > 3.0')
StudentDict = defaultdict(lambda: {"S_Id": None}) #This dic is for reserved student mapping (studentNum: S_Id)
for S_Id, StudentNumber in Students: 
    StudentDict[str(StudentNumber)]["S_Id"] = S_Id


"""Assign reserved students"""
ProjectsWithReservation = sql.select_all('select `P_Id`, `RevStus` from PROJECT_INFO where RevStus is not NULL')
for P_Id, RevStuds in ProjectsWithReservation:
    RevStudsLst = RevStuds.split(',')
    for student in RevStudsLst: 
        if StudentDict.has_key(student) and StudentDict[student]["S_Id"] not in Assigned_S_Ids:
            sql.insert_many_push({"S_Id": StudentDict[student]["S_Id"], "P_Id": P_Id})
            Assigned_S_Ids.add(StudentDict[student]["S_Id"])
            Assigned_P_Ids.add(P_Id)
if len(sql.data_list) > 0: 
    sql.insert_many_execute("ASSIGNED")
    sql.clear()

print Assigned_S_Ids
print Assigned_P_Ids

"""Get students who graduate one year later"""
now = datetime.datetime.now()
date2Compare = now + datetime.timedelta(days=365)
date2CompareStr = str(date2Compare.year) + "-" + str(date2Compare.month) + "-" + "01" + " 00:00:00"
Students = sql.select_all('select `S_Id`,`Name`,`Gender`,`Origin`,`Race`,`PrimaryMajor`,`SecondaryMajor`,`GPA`,`level`,`AppliedBefore` from STUDENT where GraduationDate > "{}" and GPA > 3.0'.format(date2CompareStr))
StudentDict = defaultdict(lambda: {"Projects": []})
print Students
# for student in Studens: 



"""Eliminate Projects no one applied"""
Applications = sql.select_all("select `S_Id`, `Pr1_P_Id`, `Pr2_P_Id`,`Pr3_P_Id`,`Pr4_P_Id`,`Pr5_P_Id`, `OptReqsCheck` from APPLICATION")
AppliedProjects = set()
for  S_Id, Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id, OptReqsCheck in Applications:
    StudentDict[S_Id]["Projects"] += Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id
    AppliedProjects = AppliedProjects.union([Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id])
    StudentDict[S_Id]["OptReqsCheck"] = OptReqsCheck
AppliedProjects = [str(x) for x in AppliedProjects - set([None])]
Projects = sql.select_all("select `P_Id` from PROJECT_INFO where P_Id in (%s)"%(", ".join(AppliedProjects)))


# now = datetime.datetime.now()
# date2Compare = now + datetime.timedelta(days=365)
# date2CompareStr = str(date2Compare.year) + "-" + str(date2Compare.month) + "-" + "01" + " 00:00:00"


# print date2CompareStr
# date2CompareStr = "2016-12-01" + " 00:00:00"

# P_Ids = ['1','2','3']

# Students = sql.select_all('select `S_Id`, `GPA`, `level` from STUDENT where GraduationDate > "{}" and GPA > 3.0'.format(date2CompareStr))
# for student in Students:


# PROJECTS = sql.select_all("select `P_Id` from PROJECT_INFO where P_Id in (%s)"%(", ".join(P_Ids)))
# print DEPT_Dict
# print PROJECTS

# APPLICATIONAS = sql.select_all('select `S_ID`, `Pr1_P_Id`, `Pr2_P_Id`, `Pr3_P_Id`, `Pr4_P_Id`, `Pr5_P_Id`, `OptReqsCheck` from APPLICATION')
# print APPLICATIONAS


# StudentDict = defaultdict(lambda: {"GPA": None, "GraduationDate": None, "ProjectList": [], "Name": None, "Gender": None, "Race": None, "PrimaryMajor": None,
# "SecondaryMajor": None, "studentNumber": None, "AppliedBefore":None, })
# StudentDict







"""
Mandatory:
Remove all the student GPA < 3.0
Assign reserved students 
Elimate project no one applied 
Student's graduation month must be one year later


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

{"S_Id":
"Assigned":
    "Project":{
        P_Id: grade
    }
}



`A_Id`
`S_ID`
`Pr1_P_Id`
`Pr2_P_Id`
`Pr3_P_Id`
`Pr4_P_Id`
`Pr5_P_Id`
`OptReqsCheck`

`S_Id`
`Name`
`Gender`
`Origin`
`Race`
`PrimaryMajor`
`SecondaryMajor`
`studentNumber`
`GPA`
`level`
`GraduationDate`
`AppliedBefore`
"""
