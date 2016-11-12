from csv import DictReader
from app import app
from flask import render_template, request, json
from flaskext.mysql import MySQL
from MysqlUtil import MysqlUtil

csv_content = list(DictReader(open("Students.csv", 'r')))


sql = MysqlUtil(app)
sql.use_account('developer')
sql.use_database('NewSE')
MAJOR = sql.select_all("select * from MAJOR;")
MAJOR_Dict = {}
for item in MAJOR:
    MAJOR_Dict[item[1]] = item[0]

for row in csv_content:
    # sql.batch_insert_push({
    #
    # })
    # sql.insert_execute('STUDENT')
    # sql.clear()

    pass

