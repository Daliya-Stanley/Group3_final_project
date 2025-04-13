use Login;

create table Booking
(
BookingID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
UserID INT NOT NULL,
foreign key (UserID) references User(UserID),
StartDate date NOT NULL,
EndDate date NOT NULL,
DestinationID INT NOT NULL,
foreign key (DestinationID) references Destination(DestinationID)
);