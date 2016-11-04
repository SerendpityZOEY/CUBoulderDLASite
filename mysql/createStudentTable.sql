create table student(
   -- ID
   S_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

   -- Primary Faculty Info
   name varchar(255) NOT NULL default 'Firstname Lastname',
   gender tinyint(3) UNSIGNED NOT NULL default 0,
   origin varchar(30) NOT NULL default 'Yes',
   race varchar(10) NOT NULL default 'Asian',
   phoneNumber varchar(20) default NULL default '(111)-222-3333',
   email varchar(255) NOT NULL default '@colorado.edu',
   Address varchar(100) NOT NULL default '0',
   Major tinyint(3) UNSIGNED NOT NULL default 0,
   studentNumber int(10) NOT NULL default 0,
   GPA varchar(5) NOT NULL default '0.0',
   level varchar(10) NOT NULL default ' ',
   graduationDate date NOT NULL default CURRENT_DATE
   researchExperience tinyint(1),
   appliedBefore tinyint(1)

   PRIMARY KEY (S_Id)
);