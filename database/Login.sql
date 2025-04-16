create database Login;
-- drop database Login;
use Login;

create table User
(
UserID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
FirstName VARCHAR(50) NOT NULL,
LastName VARCHAR(100) NOT NULL,
Email VARCHAR(100) NOT NULL UNIQUE,
Password VARCHAR (255) NOT NULL UNIQUE
);

create table ProductStatus
(
ProductStatusID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Status VARCHAR (20) NOT NULL
);

INSERT INTO ProductStatus (Status)
VALUES 
('Available'),
('Not Available');

create table Product
(
ProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ProductName VARCHAR(100) NOT NULL,
ProductPrice INT NOT NULL,
ProductStatusID INT NOT NULL,
foreign key (ProductStatusID) references ProductStatus(ProductStatusID),
ProductImage VARCHAR (50) NOT NULL
);

INSERT INTO Product (ProductName, ProductPrice, ProductStatusID, ProductImage)
VALUES
('All You Can Pack Suitcase', 200, 1, 'product_suitcase.jpeg'),
('Magical Carpet', 500, 1, 'product_carpet.jpeg'),
('Magic Potion', 100, 1, 'product-magic bottle.jpeg'),
('Magic Wand', 50, 1,'magical_wand.jpeg'),
('Spectacular One Dress - No Mess', 100, 1, 'product_clothes.jpeg');

create table Inventory
(
InventoryID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ProductID INT NOT NULL,
foreign key (ProductID) references Product(ProductID),
ProductStatusID INT NOT NULL,
foreign key (ProductStatusID) references ProductStatus(ProductStatusID)
);


create table Destination
(
DestinationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
DestinationName VARCHAR (25) NOT NULL,
DestinationPricePerNight INT NOT NULL
);

INSERT INTO Destination (DestinationName, DestinationPricePerNight)
VALUES 
('Wonderland','100'),
('Cinderella','125'),
('Aquariel','100'),
('Frozen','100'),
("Mulan's World",'150');

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

create table BookingExperience
(
BookingID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceID INT NOT NULL,
foreign key (ExperienceID) references Experiences(ExperienceID),
BookingDate date NOT NULL,
BookingTime time NOT NULL
);

create table Shopping
(
ShoppingID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
UserID INT NOT NULL,
foreign key (UserID) references User(UserID),
InventoryID INT NOT NULL,
foreign key (InventoryID) references Inventory(InventoryID),
ExperienceID INT NOT NULL,
foreign key (ExperienceID) references Experiences(ExperienceID),
Date date NOT NULL
);

DELIMITER $$

CREATE PROCEDURE GetExperienceDetails(IN exp_id INT)
BEGIN
    SELECT 
        ExperienceName AS name, 
        ExperiencePrice AS price, 
        ExperienceImage AS image, 
        DateReserved AS date
    FROM Experiences
    WHERE ExperienceID = exp_id;
END $$

DELIMITER ;

CALL GetExperienceDetails(2);
