USE mydatabase;
drop table if exists members;
drop table if exists acceslog;
CREATE TABLE members(
id   		SMALLINT     UNSIGNED NOT NULL AUTO_INCREMENT,
username  	VARCHAR(30) BINARY NOT NULL unique,
password    CHAR(41) NOT NULL,
firstname	VARCHAR(30) NOT NULL,
lastname	VARCHAR(30) NOT NULL,
joindate 	DATE NOT NULL,
gender      ENUM('m','f') NOT NULL,
favoriteGenre  ENUM('crime','horror','thriller','romance','scifi','adventure','nonfiction') NOT NULL,
emailaddress	VARCHAR(50) NOT NULL UNIQUE,
otherInterests TEXT NOT NULL,
PRIMARY KEY(id)
);
insert into members values(1,"mar0y",password('ps'),'jhon','sparks','2007-10-13','m','crime','mail.com','fg');
insert into members values(2,'mar9y',password('ps'),'jack','asia','2001-10-3','m','crime','mail1.com','fg');
insert into members values(3,'mar1y',password('ps'),'jac1k','asiaa','2001-10-3','m','crime','mail2.com','fg');
insert into members values(4,'mar2y',password('ps'),'jac2k','assia','2001-10-3','m','crime','mail3.com','fr');
insert into members values(5,'mar4y',password('ps'),'jac2k','assia','2001-10-3','m','crime','mail4.com','rg');
insert into members values(7,'mar5y',password('ps'),'jac2k','assia','2001-10-3','m','crime','mail5.com','wg');
insert into members values(8,'mar6y',password('ps'),'jac2k','assia','2001-10-3','m','crime','mail6.com','fw');
insert into members values(9,'mar7y',password('ps'),'jac2k','assia','2001-10-3','m','crime','mail7.com','fb');
insert into members values(10,'mar8y',password('ps'),'jac2k','assia','2001-10-3','m','crime','mail8.com','rb');
CREATE TABLE acceslog(
MemberId   SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
PageUrl 	VARCHAR(255) NOT NULL,
numVisits   MEDIUMINT NOT NULL,
lastAccess	TIMESTAMP NOT NULL,
PRIMARY KEY(memberid,pageurl)
);
insert into acceslog(memberid,pageurl,numvisits)values(1,'diary.php',2);
insert into acceslog(memberid,pageurl,numvisits)values(3,'books.php',2);
insert into acceslog(memberid,pageurl,numvisits)values(3,'contact.php',2);
insert into acceslog(memberid,pageurl,numvisits)values(6,'books.php',4);