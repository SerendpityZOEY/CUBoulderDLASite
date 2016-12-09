from csv import DictReader,DictWriter
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil
import datetime
from collections import defaultdict, Counter


sqlUtil = MysqlUtil(app)
sqlUtil.use_account('developer')
sqlUtil.use_database('SEDB')
data = sqlUtil.select_all("SELECT `S_Id`,`P_Id` FROM `ASSIGNED`")
students = sqlUtil.select_all("SELECT `S_Id`, `StudentNumber`, `Name` FROM STUDENT")
projects = sqlUtil.select_all("SELECT `P_Id`, `ProjName` FROM `PROJECT_INFO`")
stuDict = dict()
projDict = dict()
res = []
for person in students:
    stuDict[person[0]] = [person[2], person[1]]

for proj in projects:
    projDict[proj[0]] = proj[1]

for i in data:
    # print(i[0], stuDict[i[0]], projDict[i[1]])
    res.append([i[0], stuDict[i[0]], projDict[i[1]]])
with open('./app/result.csv', 'wb') as csvfile:
    fieldnames = ["Student Name", 'Student Number', "Assigned Project Name"]
    writer = DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # print projDict
    # print 
    for i in data:
        print (i)
        print (fieldnames[0])
        print (stuDict[i[0]][0])
        print (fieldnames[1])
        print (stuDict[i[0]][1])
        print (fieldnames[2])
        print (projDict[i[1]][0])
        writer.writerow({fieldnames[0]: stuDict[i[0]][0], fieldnames[1]: stuDict[i[0]][1], fieldnames[2]: projDict[i[1]].encode('utf8')})
    # res.append([i[0], stuDict[i[0]], projDict[i[1]]]) 