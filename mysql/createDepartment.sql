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
