create table student(
   -- ID
   S_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

   -- Primary Faculty Info
   Name varchar(255) NOT NULL default 'Firstname Lastname',
   Gender tinyint(3) UNSIGNED NOT NULL default 0,
   Origin tinyint(3) NOT NULL default 0,
   Race varchar(10) NOT NULL default '',
   PhoneNumber varchar(20) default NULL default '(111)-222-3333',
   Email varchar(100) NOT NULL default '@colorado.edu',
   Address varchar(100) NOT NULL default '0',
   SumPhoneNumber varchar(20) default NULL,
   SumEmail varchar(100) default NULL,
   SumAddress varchar(100) default NULL,
   PrimaryMajor tinyint(3) UNSIGNED NOT NULL default 0,
   SecondaryMajor tinyint(3) default 0,
   StudentNumber int(11) NOT NULL default 0,
   GPA varchar(5) NOT NULL default '',
   Level tinyint(3) NOT NULL default 0,
   GraduationDate date NOT NULL default CURRENT_DATE
   ResearchExperience tinyint(1) default NULL,
   AppliedBefore tinyint(1) default NULL
   EmploymentPlanned varchar(255) default NULL,
   BackgroundCheck tinyint(3) default NULL,
   Discrimination tinyint(3) default NULL,
   SSN int(4) default NULL,
   Skills varchar(255) default NULL

   PRIMARY KEY (S_Id)
);