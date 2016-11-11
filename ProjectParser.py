from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil

csv_content = list(DictReader(open("Projects.csv", 'r')))

major = {
    'AES': 1,
    'APPM': 2,
    'CHBE': 3,
    'CEAE': 4,
    'CS': 5,
    'ECEE': 6,
    # 'PHYS': 7, We don't know the acronyms for physics
    'EVEN': 8,
    'ME': 9,
    'CSGC': 10,
    'EnEd': 11,
    'ATLAS': 12,
}

sql = MysqlUtil(app)
sql.use_account('developer')
sql.use_database('NewSE')
for row in csv_content:
    sql.batch_insert_push({
        "PFName":            row['PrimaryPrFirst'] + ' ' + row['PrimaryPrLast'],
        "PFPhone":           row['PrimaryPrPhone'],
        "PFEmail":           row['PrimaryPrMail'],
        "PFDept":            major[row['']],
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

