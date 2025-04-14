use Login;

create table Experiences
(
ExperienceID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceName VARCHAR (50) NOT NULL,
ExperiencePrice INT NOT NULL,
ExperienceImage VARCHAR (50) NOT NULL,
DateReserved date NULL
);

INSERT INTO Experiences (ExperienceName, ExperiencePrice,ExperienceImage,DateReserved)
VALUES
('Make a Snowman', 50, 'Experience-snowman.jpeg', null ),
('Flying Lesson', 250, 'Experience-carpet.jpeg', null),
('Troll Party', 50, 'Experience-Troll.jpeg', null),
('Scuba Diving', 250, 'Experience-Scuba.jpeg', null),
('Spa Experience',100,'Experience-Spa.jpeg', null);