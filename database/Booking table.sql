use Login;

create table BookingExperience
(
BookingID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceID INT NOT NULL,
foreign key (ExperienceID) references Experiences(ExperienceID),
BookingDate date NOT NULL,
BookingTime time NOT NULL
);



