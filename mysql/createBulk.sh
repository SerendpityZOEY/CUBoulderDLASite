echo "DROP TABLE APPLICATION;" > ./bulkCreate.sql 
echo "DROP TABLE STUDENT;" >> ./bulkCreate.sql
echo "DROP TABLE PROJECT_INFO;" >> ./bulkCreate.sql
echo "DROP MAJOR;" >> ./bulkCreate.sql
echo "DROP DEPT;" >> ./bulkCreate.sql
cat ./createDepartment.sql >> ./bulkCreate.sql 
cat ./createMajor.sql >> ./bulkCreate.sql 
cat ./createProjInfo.sql >> ./bulkCreate.sql 
cat ./createStudentTable.sql >> ./bulkCreate.sql 
cat ./createApplication.sql >> ./bulkCreate.sql

