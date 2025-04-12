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
('Make a Snowman', 50, null),
('Flying Lesson', 250, null),
('Troll Party', 50, null),
('Scuba Diving', 250, null),
('Spa Experience',100, null);