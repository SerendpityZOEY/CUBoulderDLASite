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

    
) ENGINE=InnoDB DEFAULT CHARSET=utf8;