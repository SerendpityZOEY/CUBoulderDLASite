create table APPLICATION(
   -- ID
   A_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

   -- Student Info
   S_Id int(11) UNSIGNED NOT NULL default 0,
   Pr1_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr2_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr3_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr4_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr5_P_Id int(11) UNSIGNED NOT NULL default 0,


   PRIMARY KEY (A_Id),



   INDEX (S_Id),
   INDEX (Pr1_P_Id, Pr2_P_Id, Pr3_P_Id, Pr4_P_Id, Pr5_P_Id),

   FOREIGN KEY (S_Id) REFERENCES STUDENT(S_Id) ON UPDATE CASCADE ON DELETE RESTRICT,

   FOREIGN KEY (Pr1_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
   FOREIGN KEY (Pr2_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
   FOREIGN KEY (Pr3_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
   FOREIGN KEY (Pr4_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,
   FOREIGN KEY (Pr5_P_Id) REFERENCES PROJECT_INFO(P_Id) ON UPDATE CASCADE ON DELETE RESTRICT,


);