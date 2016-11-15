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
    GraduationDate date NOT NULL DEFAULT '2016-12-00',
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