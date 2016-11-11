DROP TABLE APPLICATION
DROP TABLE STUDENT
DROP TABLE PROJECT_INFO
DROP MAJOR
DROP DEPT
create table DEPT(
    -- ID
    D_Id tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Acronym varchar(10) NOT NULL default "",
    FullName varchar(100) NOT NULL default "",

    PRIMARY KEY (M_Id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE DEPT AUTO_INCREMENT = 1;

INSERT INTO DEPT 
    (D_Id, Acronym, FullName)
VALUES 
(0, 'ERROR', 'Not A Valid Major Or Not Selected')
(1, 'AES', 'Aerospace Engineering Sciences'),
(2, 'APPM', 'Applied Mathematics');
create table MAJOR(
    -- ID
    M_Id tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Acronym varchar(10) NOT NULL default "",
    FullName varchar(100) NOT NULL default "",


    PRIMARY KEY (M_Id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE MAJOR AUTO_INCREMENT = 1;

INSERT INTO MAJOR 
    (M_Id, Acronym, FullName)
VALUES 
(1, 'AES', 'Aerospace Engineering Sciences'),
(2, 'APPM', 'Applied Mathematics');
create table PROJECT_INFO(
    -- ID
    P_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Primary Faculty Info
    PFName varchar(255) NOT NULL default '',
    PFPhone varchar(20) default NULL,
    PFEmail varchar(255) NOT NULL default '',
    PFDept tinyint(3) UNSIGNED NOT NULL default 0,
    HasFocus boolean NOT NULL default 0,

    -- Second Faculty Info
    SFName varchar(255) default NULL,
    SFPhone varchar(20) default NULL,
    SFEmail varchar(255) default NULL,

    -- Graduate/Postdoc Info
    GradName varchar(255) default NULL,
    GradPhone varchar(20) default NULL,
    GradEmail varchar(255) default NULL,

    -- Apprenticeship Info
    ProjName varchar(80) NOT NULL default '',
    LongDesc varchar(2000) NOT NULL default '',
    WebLink varchar(255) default NULL,
    -- Mandatory Special Requirement
    ManReqs varchar(1000) default NULL,
    -- Optional Special Requirement
    OptReqs varchar(1000) default NULL,
    StuMajors varchar(100) NOT NULL default '',
    AmtOfSup tinyint(3) UNSIGNED NOT NULL default 0,
    SupBy tinyint(3) UNSIGNED NOT NULL default 0,
    NatureOfWork varchar(50) NOT NULL default '0',
    AmtOfPreWork varchar(50) NOT NULL default '0',
    RevStus varchar(500) default NULL,

    -- Finances
    SpeedType varchar(255) NOT NULL default '',
    AcctContace varchar(255) NOT NULL default '',
    DidSup boolean NOT NULL default 0,

    PRIMARY KEY (P_Id)
    
    INDEX (PFDept),

    FOREIGN KEY (PFDept) REFERENCES DEPT(D_Id) ON UPDATE CASCADE ON DELETE RESTRICT,

    
) ENGINE=InnoDB DEFAULT CHARSET=utf8;create table STUDENT(
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
    SecondaryMajor tinyint(3) default 0,
    StudentNumber int(11) NOT NULL default 0,
    GPA varchar(5) NOT NULL default '',
    Level tinyint(3) NOT NULL default 0,
    GraduationDate date NOT NULL default '2016-01-01',
    ResearchExperience boolean default NULL,
    AppliedBefore tinyint(3) UNSIGNED default NULL,
    EmploymentPlanned varchar(1000) default NULL,
    BackgroundCheck tinyint(3) default NULL,
    Discrimination tinyint(3) default NULL,
    SSN smallint(5) default NULL,
    Skills varchar(1000) default NULL,

    PRIMARY KEY (S_Id)

    INDEX (PrimaryMajor, SecondaryMajor),

    FOREIGN KEY (PrimaryMajor) REFERENCES MAJOR(M_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (SecondaryMajor) REFERENCES MAJOR(M_Id) ON UPDATE CASCADE ON DELETE RESTRICT,

) ENGINE=InnoDB DEFAULT CHARSET=utf8;create table APPLICATION(
    -- ID
    A_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Application Info
    S_Id int(11) UNSIGNED NOT NULL default 0,
    Pr1_P_Id int(11) UNSIGNED NOT NULL default 0,
    Pr2_P_Id int(11) UNSIGNED NOT NULL default 0,
    Pr3_P_Id int(11) UNSIGNED NOT NULL default 0,
    Pr4_P_Id int(11) UNSIGNED NOT NULL default 0,
    Pr5_P_Id int(11) UNSIGNED NOT NULL default 0,

    -- Optional Special Requirement Check
    OptReqsCheck varchar(20) NOT NULL default '',

    PRIMARY KEY (A_Id),

    INDEX (S_Id),
    INDEX (Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id),

    FOREIGN KEY (S_Id) REFERENCES STUDENT(S_Id) ON UPDATE CASCADE ON DELETE RESTRICT,

    FOREIGN KEY (Pr1_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Pr2_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Pr3_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Pr4_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Pr5_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
