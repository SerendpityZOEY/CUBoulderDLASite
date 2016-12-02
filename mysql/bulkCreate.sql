DROP TABLE IF EXISTS APPLICATION;
DROP TABLE IF EXISTS STUDENT;
DROP TABLE IF EXISTS PROJECT_INFO;
DROP TABLE IF EXISTS MAJOR;
DROP TABLE IF EXISTS DEPT;

create table DEPT(
    -- ID
    D_Id tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Acronym varchar(10) NOT NULL DEFAULT "",
    FullName varchar(100) NOT NULL DEFAULT "",

    PRIMARY KEY (D_Id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- SET SESSION SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
ALTER TABLE DEPT AUTO_INCREMENT = 1;

INSERT INTO DEPT 
    (D_Id, Acronym, FullName)
VALUES 
-- (0,  "ZERO", "Not Selected Or Error"),
(1,  "AES" , "Aerospace Engineering Sciences"),
(2,  "APPM", "Applied Math"),
(3,  "CHBE", "Chemical and Biological Engineering"),
(4,  "CEAE", "Civil, Environmental and Architectural Engineering"),
(5,  "CS"  , "Computer Science"),
(6,  "ECEE", "Electrical, Computer and Energy Engineering"),
(7,  "PHYS", "Physics"),
(8,  "EVEN", "Environmental Engineering"),
(9,  "ME"  , "Mechanical Engineering"),
(10, "CSGC", "Colorado Space Grant"),
(11, "EnEd", "Engineering Education"),
(12, "ATLS", "ATLAS");
create table MAJOR(
    -- ID
    M_Id tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Acronym varchar(10) NOT NULL DEFAULT "",
    FullName varchar(100) NOT NULL DEFAULT "",


    PRIMARY KEY (M_Id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- SET SESSION SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
ALTER TABLE MAJOR AUTO_INCREMENT = 1;


INSERT INTO MAJOR 
    (M_Id, Acronym, FullName)
VALUES 
-- (0,  "ZERO", "Not Selected Or Error"),
(1,  "ASEN", "Aerospace Engineering"),
(2,  "AMEN", "Applied Mathematics"),
(3,  "AREN", "Architectural Engineering"),
(4,  "CHEN", "Chemical Engineering"),
(5,  "CBEN", "Chemical and Biological Engineering"),
(6,  "CVEN", "Civil Engineering"),
(7,  "CSEN", "Computer Science"),
(8,  "EEEN", "Electrical Engineering"),
(9,  "ECEN", "Electrical and Computer Engineering"),
(10, "EPEN", "Engineering Physics"),
(11, "EVEN", "Environmental Engineering"),
(12, "GEEN", "Engineering Plus"),
(13, "MCEN", "Mechanical Engineering"),
(14, "TMEN", "Technology, Arts, and Media");
create table PROJECT_INFO(
    -- ID
    P_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Primary Faculty Info
    PFName varchar(255) NOT NULL DEFAULT '',
    PFPhone varchar(20) DEFAULT NULL,
    PFEmail varchar(255) NOT NULL DEFAULT '',
    PFDept tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
    HasFocus boolean NOT NULL DEFAULT 0,

    -- Second Faculty Info
    SFName varchar(255) DEFAULT NULL,
    SFPhone varchar(20) DEFAULT NULL,
    SFEmail varchar(255) DEFAULT NULL,

    -- Graduate/Postdoc Info
    GradName varchar(255) DEFAULT NULL,
    GradPhone varchar(20) DEFAULT NULL,
    GradEmail varchar(255) DEFAULT NULL,

    -- Apprenticeship Info
    ProjName varchar(80) NOT NULL DEFAULT '',
    LongDesc varchar(2000) NOT NULL DEFAULT '',
    WebLink varchar(255) DEFAULT NULL,
    -- Mandatory Special Requirement
    ManReqs varchar(1000) DEFAULT NULL,
    -- Optional Special Requirement
    OptReqs varchar(1000) DEFAULT NULL,
    StuMajors varchar(100) NOT NULL DEFAULT '',
    AmtOfSup tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
    SupBy tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
    NatureOfWork varchar(50) NOT NULL DEFAULT '0',
    AmtOfPreWork varchar(50) NOT NULL DEFAULT '0',
    RevStus varchar(500) DEFAULT NULL,

    -- Finances
    SpeedType varchar(255) NOT NULL DEFAULT '',
    AcctContace varchar(255) NOT NULL DEFAULT '',
    DidSup boolean NOT NULL DEFAULT 0,


    PRIMARY KEY (P_Id),

    INDEX (PFDept),

    FOREIGN KEY (PFDept) REFERENCES DEPT(D_Id) ON UPDATE CASCADE ON DELETE RESTRICT

    
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- SET SESSION SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
ALTER TABLE PROJECT_INFO AUTO_INCREMENT = 1;

-- INSERT INTO PROJECT_INFO 
--     (P_Id)
-- VALUES 
--     (0);
create table STUDENT(
    -- ID
    S_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Name varchar(255) NOT NULL DEFAULT '',
    Gender tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
    Origin tinyint(3) NOT NULL DEFAULT 0,
    Race varchar(20) NOT NULL DEFAULT '',
    Phone varchar(20) DEFAULT NULL DEFAULT '',
    Email varchar(100) NOT NULL DEFAULT '',
    Address varchar(100) NOT NULL DEFAULT '',
    SumPhone varchar(20) DEFAULT NULL,
    SumEmail varchar(100) DEFAULT NULL,
    SumAddress varchar(100) DEFAULT NULL,
    PrimaryMajor tinyint(3) UNSIGNED NOT NULL,
    SecondaryMajor tinyint(3) UNSIGNED DEFAULT NULL,
    StudentNumber int(11) NOT NULL DEFAULT 0,
    GPA varchar(5) NOT NULL DEFAULT '',
    Level tinyint(3) NOT NULL DEFAULT 0,
    GraduationDate date NOT NULL DEFAULT '2016-12-01',
    ResearchExperience boolean DEFAULT NULL,
    AppliedBefore tinyint(3) UNSIGNED DEFAULT NULL,
    EmploymentPlanned varchar(1000) DEFAULT NULL,
    BackgroundCheck tinyint(3) DEFAULT NULL,
    Discrimination tinyint(3) DEFAULT NULL,
    SSN smallint(5) DEFAULT NULL,
    Skills varchar(1000) DEFAULT NULL,


    PRIMARY KEY (S_Id),

    INDEX (PrimaryMajor, SecondaryMajor), 

    FOREIGN KEY (PrimaryMajor) REFERENCES MAJOR(M_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (SecondaryMajor) REFERENCES MAJOR(M_Id) ON UPDATE CASCADE ON DELETE RESTRICT

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- SET SESSION SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
ALTER TABLE STUDENT AUTO_INCREMENT = 1;

-- INSERT INTO STUDENT 
    -- (S_Id)
-- VALUES 
    -- (0) ;

create table APPLICATION(
    -- ID
    A_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Application Info
    S_Id int(11) UNSIGNED NOT NULL,
    Pr1_P_Id int(11) UNSIGNED NOT NULL,
    Pr2_P_Id int(11) UNSIGNED DEFAULT NULL,
    Pr3_P_Id int(11) UNSIGNED DEFAULT NULL,
    Pr4_P_Id int(11) UNSIGNED DEFAULT NULL,
    Pr5_P_Id int(11) UNSIGNED DEFAULT NULL,

    -- Optional Special Requirement Check
    OptReqsCheck varchar(20) NOT NULL DEFAULT '',

    Secret varchar(32) NOT NULL DEFAULT '',
    CreatedTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    LastUpdatedTime TIMESTAMP NOT NULL DEFAULT '1970-01-02 15:04:05',
    -- LastUpdatedTime TIMESTAMP NOT NULL CURRENT_TIMESTAMP,

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
