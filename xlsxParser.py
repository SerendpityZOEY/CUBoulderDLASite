from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL

csv_content = list(DictReader(open("Students.csv", 'r')))

fieldnames = ['Name',
 'Primary Major',
 'Secondary Major',
 'Major on System if different',
 'Level In School',
 'Grad Date',
 'Self-Reported GPA',
 'GPA after spring semester',
 'Gender',
 'Ethnicity',
 'Prev-Exper-ience',
 'Other employ?',
 'Applied Before?',
 'ProjectName/ Choice given',
 'Skill1',
 'Skill2',
 'Skill3',
 'Project1',
 'Project2',
 'Project3',
 'Project4',
 'Project5',
 'Student ID',
 'BldrEmail',
 'SummerEmail',
 'Other Employment']


mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abs234grj2345'
app.config['MYSQL_DATABASE_DB'] = 'SEDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
cursor.execute(query, (name, gender, origin, race))
conn.commit()
# cursor.callproc('sp_createUser', (_name, _gender, _origin, _race))
data = cursor.fetchall()
cursor.close()
conn.close()


for row in csv_content:
 query = "INSERT INTO `Demographic` (`name`, `gender`, `origin`, `race`) VALUES (%s,%s,%s,%s);"
