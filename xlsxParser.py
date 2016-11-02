from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil

csv_content = list(DictReader(open("Students.csv", 'r')))

# fieldnames = ['Name',
#               'Primary Major',
#               'Secondary Major',
#               'Major on System if different',
#               'Level In School',
#               'Grad Date',
#               'Self-Reported GPA',
#               'GPA after spring semester',
#               'Gender',
#               'Ethnicity',
#               'Prev-Exper-ience',
#               'Other employ%s',
#               'Applied Before%s',
#               'ProjectName/ Choice given',
#               'Skill1',
#               'Skill2',
#               'Skill3',
#               'Project1',
#               'Project2',
#               'Project3',
#               'Project4',
#               'Project5',
#               'Student ID',
#               'BldrEmail',
#               'SummerEmail',
#               'Other Employment']

# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'user'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'l74z3oC1=1V>5J7'
# app.config['MYSQL_DATABASE_DB'] = 'SEDB'
# app.config['MYSQL_DATABASE_HOST'] = '54.186.181.45'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# mysql.init_app(app)
#
# conn = mysql.connect()
# cursor = conn.cursor()
# cursor.callproc('sp_createUser', (_name, _gender, _origin, _race))
# data = cursor.fetchall()

sql = MysqlUtil(app)

for row in csv_content[50:53]:
    sql.insert_push('name', row['Name'])
    sql.insert_push('gender', row['Gender'])
    sql.insert_push('race', row['Ethnicity'])
    sql.insert_push('email', row['BldrEmail'])
    sql.insert_push('studentNumber', row['Student ID'])
    sql.insert_push('Major', row['Primary Major'])
    sql.insert_push('GPA', row['Self-Reported GPA'])
    sql.insert_push('level', row['Level In School'])
    sql.insert_execute('student')
    # The clear can be ignored, since in next iteration, all the values will be assigned a new value
    sql.clear()

    # query = "INSERT INTO `student` (`name`, `gender`, `race`, `email`,`Major`,`studentNumber`,`GPA`,`level`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    # cursor.execute(query, (name, gender, race, email, Major, studentNumber, GPA, level))
    # conn.commit()
# cursor.close()
# conn.close()
