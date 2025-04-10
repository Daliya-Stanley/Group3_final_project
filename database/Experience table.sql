use Login;

create table Experiences
(
ExperienceID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceName VARCHAR (50) NOT NULL,
ExperiencePrice INT NOT NULL,
DateReserved date NULL
);