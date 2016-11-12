create table DEPT(
    -- ID
    D_Id tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,

    -- Student Info
    Acronym varchar(10) NOT NULL default "",
    FullName varchar(100) NOT NULL default "",

    PRIMARY KEY (D_Id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO DEPT 
    (D_Id, Acronym, FullName)
VALUES 
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