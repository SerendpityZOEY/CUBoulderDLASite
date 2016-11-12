echo "DROP TABLE IF EXISTS APPLICATION;" > ./bulkCreate.sql 
echo "DROP TABLE IF EXISTS STUDENT;" >> ./bulkCreate.sql
echo "DROP TABLE IF EXISTS PROJECT_INFO;" >> ./bulkCreate.sql
echo "DROP TABLE IF EXISTS MAJOR;" >> ./bulkCreate.sql
echo "DROP TABLE IF EXISTS DEPT;" >> ./bulkCreate.sql
echo "" >> ./bulkCreate.sql
cat ./createDepartment.sql >> ./bulkCreate.sql 
echo "" >> ./bulkCreate.sql
cat ./createMajor.sql >> ./bulkCreate.sql 
echo "" >> ./bulkCreate.sql
cat ./createProjInfo.sql >> ./bulkCreate.sql 
echo "" >> ./bulkCreate.sql
cat ./createStudentTable.sql >> ./bulkCreate.sql 
echo "" >> ./bulkCreate.sql
cat ./createApplication.sql >> ./bulkCreate.sql

