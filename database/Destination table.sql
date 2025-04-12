use Login;

create table Destination
(
DestinationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
DestinationName VARCHAR (25) NOT NULL,
DestinationPricePerNight INT NOT NULL
);

INSERT INTO Destination (DestinationName, DestinationPricePerNight)
VALUES 
('Wonderland','£100'),
('Cinderella','£125'),
('Destination 3','£100'),
('Frozen','£100'),
('Destination 5','£150');