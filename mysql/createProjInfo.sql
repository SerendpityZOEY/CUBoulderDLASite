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