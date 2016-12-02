from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil

csv_content = list(DictReader(open("Projects.csv", 'r')))


sql = MysqlUtil(app)
sql.use_account('developer')
sql.use_database('SEDB')

DEPT = sql.select_all("select * from DEPT;")
DEPT_Dict = {}
for item in DEPT:
    DEPT_Dict[item[1]] = item[0]

for row in csv_content:
    sql.batch_insert_push({
        "PFName":            row['PrimaryPrFirst'] + ' ' + row['PrimaryPrLast'],
        "PFPhone":           row['PrimaryPrPhone'],
        "PFEmail":           row['PrimaryPrMail'],
        "PFDept":            DEPT_Dict[row['']],
        # "HasFocus":          row[''],
        "SFName":            row['SecondPrFirst'] + ' ' + row['SecondPrLast'],
        "SFPhone":           row['SecondPrPhone'],
        "SFEmail":           row['PrimaryPrMail'],
        "GradName":          row['GradFirst'] + ' ' + row['GradLast'],
        "GradPhone":         row['GradPhone'],
        "GradEmail":         row['GradMail'],
        "ProjName":          row['ProjectName'],
        "LongDesc":          row['Description'],
        "WebLink":           row['Weblink'],
        "ManReqs":           row['Special Requirements Mandatory1'] + '$;^' + row['Special Requirements Mandatory2'],
        "OptReqs":           row['Special Requirements Optional1'] + '$;^' + row['Special Requirements Optional2'] + '$;^' + row['Special Requirements Optional3'],
        # "StuMajors":         row[''],
        # "AmtOfSup":          row[''],
        # "SupBy":             row[''],
        # "NatureOfWork":      row[''],
        # "AmtOfPreWork":      row[''],
        # "RevStus":           row[''],
        # "SpeedType":         row[''],
        # "AcctContace":       row[''],
        # "DidSup":            row['']
    })
    sql.insert_execute('PROJECT_INFO')
    sql.clear()

