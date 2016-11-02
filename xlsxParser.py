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
              'Other employ%s',
              'Applied Before%s',
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
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'l74z3oC1=1V>5J7'
app.config['MYSQL_DATABASE_DB'] = 'SEDB'
app.config['MYSQL_DATABASE_HOST'] = '54.186.181.45'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
# cursor.callproc('sp_createUser', (_name, _gender, _origin, _race))
# data = cursor.fetchall()

for row in csv_content[:20]:
    name = row['Name']
    gender = row['Gender']
    race = row['Ethnicity']
    email = row['BldrEmail']
    Major = row['Primary Major']
    studentNumber = row['Student ID']
    GPA = row['Self-Reported GPA']
    level = row['Level In School']
    query = "INSERT INTO `student` (`name`, `gender`, `race`, `email`,`Major`,`studentNumber`,`GPA`,`level`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(query, (name, gender, race, email, Major, studentNumber, GPA, level))
    conn.commit()
cursor.close()
conn.close()
