create table MAJOR(
    -- ID
    M_Id tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Acronym varchar(10) NOT NULL default "",
    FullName varchar(100) NOT NULL default "",


    PRIMARY KEY (M_Id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


SET SESSION SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
ALTER TABLE MAJOR AUTO_INCREMENT = 0;


INSERT INTO MAJOR 
    (M_Id, Acronym, FullName)
VALUES 
(0,  "ZERO", "Not Selected Or Error"),
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