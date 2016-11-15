create table STUDENT(
    -- ID
    S_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Name varchar(255) NOT NULL default '',
    Gender tinyint(3) UNSIGNED NOT NULL default 0,
    Origin tinyint(3) NOT NULL default 0,
    Race varchar(20) NOT NULL default '',
    Phone varchar(20) default NULL default '',
    Email varchar(100) NOT NULL default '',
    Address varchar(100) NOT NULL default '',
    SumPhone varchar(20) default NULL,
    SumEmail varchar(100) default NULL,
    SumAddress varchar(100) default NULL,
    PrimaryMajor tinyint(3) UNSIGNED NOT NULL default 0,
    SecondaryMajor tinyint(3) UNSIGNED default 0,
    StudentNumber int(11) NOT NULL default 0,
    GPA varchar(5) NOT NULL default '',
    Level tinyint(3) NOT NULL default 0,
    GraduationDate date NOT NULL default '2016-12-00',
    ResearchExperience boolean default NULL,
    AppliedBefore tinyint(3) UNSIGNED default NULL,
    EmploymentPlanned varchar(1000) default NULL,
    BackgroundCheck tinyint(3) default NULL,
    Discrimination tinyint(3) default NULL,
    SSN smallint(5) default NULL,
    Skills varchar(1000) default NULL,


    PRIMARY KEY (S_Id),

    INDEX (PrimaryMajor, SecondaryMajor), 

    FOREIGN KEY (PrimaryMajor) REFERENCES MAJOR(M_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (SecondaryMajor) REFERENCES MAJOR(M_Id) ON UPDATE CASCADE ON DELETE RESTRICT

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET SESSION SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
ALTER TABLE STUDENT AUTO_INCREMENT = 0;

INSERT INTO STUDENT 
    (S_Id)
VALUES 
    (0) ;