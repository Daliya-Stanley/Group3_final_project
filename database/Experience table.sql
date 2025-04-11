use Login;

create table Experiences
(
ExperienceID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceName VARCHAR (50) NOT NULL,
ExperiencePrice INT NOT NULL,
DateReserved date NULL
);

INSERT INTO Experiences (ExperienceName, ExperiencePrice, DateReserved)
VALUES 
('Make a Snowman','£50'),
('Flying Lesson','£250'),
('Troll Party','£50'),
('Scuba Diving','£250'),
('Spa Experience','£100');