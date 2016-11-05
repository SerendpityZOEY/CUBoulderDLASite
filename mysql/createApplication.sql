create table APPLICATION(
   -- ID
   A_Id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

   -- Application Info
   S_Id int(11) UNSIGNED NOT NULL default 0,
   Pr1_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr2_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr3_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr4_P_Id int(11) UNSIGNED NOT NULL default 0,
   Pr5_P_Id int(11) UNSIGNED NOT NULL default 0,

   PRIMARY KEY (A_Id)
);