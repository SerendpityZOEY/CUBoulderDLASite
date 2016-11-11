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
