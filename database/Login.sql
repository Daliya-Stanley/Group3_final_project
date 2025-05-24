create database Login;
drop database Login;
use Login;
select * from User;
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
('Not Available'),
('Promotion');

create table Product
(
ProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ProductName VARCHAR(100) NOT NULL,
ProductPrice INT NOT NULL,
ProductStatusID INT NOT NULL,
foreign key (ProductStatusID) references ProductStatus(ProductStatusID),
ProductImage VARCHAR (50) NOT NULL
);
ALTER TABLE Product
ADD ProductDescription TEXT;

SET SQL_SAFE_UPDATES =0;
UPDATE Product
SET ProductDescription = 'A bottomless suitcase that fits everything you need for an epic adventure.'
WHERE ProductName = 'All You Can Pack Suitcase';

UPDATE Product
SET ProductDescription = 'A flying carpet that whisks you away to your destination in style.'
WHERE ProductName = 'Magical Carpet';

UPDATE Product
SET ProductDescription = 'A mysterious elixir with enchanting effects and which heals your heart and body.'
WHERE ProductName = 'Magic Potion';

UPDATE Product
SET ProductDescription = 'A sleek wand that channels your inner wizard with a flick and a spark and get your house squeaky clean.'
WHERE ProductName = 'Magic Wand';

UPDATE Product
SET ProductDescription = 'A magical outfit that transforms into any style with zero effort.'
WHERE ProductName = 'Spectacular One Dress - No mess';


INSERT INTO Product (ProductName, ProductPrice, ProductStatusID, ProductImage)
VALUES
('All You Can Pack Suitcase', 200, 1, 'product_suitcase.jpeg'),
('Magical Carpet', 500, 1, 'product_carpet.jpeg'),
('Magic Potion', 100, 1, 'product-magic bottle.jpeg'),
('Magic Wand', 50, 1,'magical_wand.jpeg'),
('Spectacular One Dress - No Mess', 100, 1, 'product_clothes.jpeg'),
('All You Can Pack Suitcase - Free', 0, 3, 'product_suitcase.jpeg'),
('Magical Carpet - Free', 0, 3, 'product_carpet.jpeg'),
('Magic Potion - Free', 0, 3, 'product-magic bottle.jpeg'),
('Magic Wand - Free', 0, 3,'magical_wand.jpeg'),
('One Dress - No Mess - Free', 0, 3, 'product_clothes.jpeg');

CREATE TABLE Orders (
  OrderID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  UserID INT NOT NULL,
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);

CREATE TABLE OrderStatus (
    OrderStatusID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    StatusName VARCHAR(20) NOT NULL
);

INSERT INTO OrderStatus (StatusName)
VALUES ('Pending'), ('Shipped'), ('Delivered');

select * from Orders;
select * from BookingDestination;
select * from ProductOrders;
DELETE from ProductOrders where ProductOrdersID = 10;
select * from BookingExperience;
DELETE from Orders where OrderID = 17;
DELETE from BookingExperience where BookingID = 16;
DELETE from BookingDestination where BookingDestinationID = 4;
SELECT * from CancelDestinationRequests;
DELETE from CancelDestinationRequests where CancelRequestID = 3;

create table ProductOrders
(
	ProductOrdersID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ProductID INT NOT NULL,
    foreign key (ProductID) references Product(ProductID),
	UserID INT NOT NULL,
	foreign key (UserID) references User(UserID),
    Quantity INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    OrderID INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
ALTER TABLE ProductOrders ADD COLUMN Status VARCHAR(20) DEFAULT 'Processing';
ALTER TABLE ProductOrders
DROP COLUMN Status;

ALTER TABLE ProductOrders
ADD COLUMN OrderStatusID INT DEFAULT 1,
ADD FOREIGN KEY (OrderStatusID) REFERENCES OrderStatus(OrderStatusID);


create table Destination
(
DestinationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
DestinationName VARCHAR (25) NOT NULL,
DestinationPricePerNight INT NOT NULL,
DestinationImage VARCHAR(100)
);

INSERT INTO Destination (DestinationName, DestinationPricePerNight, DestinationImage)
VALUES 
('Wonderland','100','WT.JPG'),
('Cinderella','125','cinderella.jpg'),
('Aquariel','100','ariel_topsection.jpg'),
('Frozen','100','frozen_main.jpeg'),
("Mulan's World",'150','mulan.png');

create table BookingDestination
(
BookingDestinationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
DestinationID INT NOT NULL,
foreign key (DestinationID) references Destination(DestinationID),
BookingStartDate date NOT NULL,
BookingEndDate date NOT NULL,
UserID INT NOT NULL,
foreign key (UserID) references User(UserID),
Guests INT NOT NULL DEFAULT 1,
OrderID INT NULL,
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
ReviewText TEXT NULL,
Rating INT NULL
);

create table ExperienceLevel
(
ExperienceLevelID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceLevelKey VARCHAR (20) NOT NULL
);

INSERT INTO ExperienceLevel (ExperienceLevelKey)
VALUES
('Light'),
('Moderate'),
('High');

create table Experiences
(
ExperienceID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceName VARCHAR (50) NOT NULL,
ExperiencePrice INT NOT NULL,
ExperienceImage VARCHAR (50) NOT NULL,
ExperienceDescription TEXT NOT NULL,
ExperienceDuration INT NOT NULL,
ExperienceLevelID INT NOT NULL,
foreign key (ExperienceLevelID) references ExperienceLevel(ExperienceLevelID),
ExperienceMinAge INT NOT NULL,
ExperienceGroupSize INT NOT NULL
);

INSERT INTO Experiences (
  ExperienceName, ExperiencePrice, ExperienceImage,
  ExperienceDescription, ExperienceDuration,
  ExperienceLevelID, ExperienceMinAge,
  ExperienceGroupSize
)
VALUES
(
  'Make a Snowman', 50, 'Experience-snowman.jpeg',
  'Join Anna and her Frozen friends for a magical snowman-making adventure where laughter, snowflakes, and enchantment come to life!',
  2, 2, 5, 10
),
(
  'Flying Lesson', 250, 'Experience-carpet.jpeg',
  'Soar above the clouds with Aladdin on a magical flying carpet ride—an unforgettable adventure straight out of Agrabah!',
  1, 3, 8, 4
),
(
  'Troll Party', 50, 'Experience-Troll.jpeg',
  'Get ready to dance, sing, and sparkle in the ultimate feel-good party with the Trolls—where every moment is a burst of magic and music!',
  3, 1, 4, 15
),
(
  'Scuba Diving', 250, 'Experience-Scuba.jpeg',
  'Dive into an underwater wonderland with Ariel and explore vibrant reefs, shimmering treasures, and ocean magic like never before!',
  6, 3, 10, 6
  ),
(
  'Spa Experience', 100, 'Experience-Spa.jpeg',
  'Indulge in a royal spa day at Princess Aurora’s castle, where enchantment meets elegance for the ultimate fairy-tale pampering!',
  4, 1, 12, 5
);

create table BookingExperience
(
BookingID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ExperienceID INT NOT NULL,
foreign key (ExperienceID) references Experiences(ExperienceID),
BookingDate date NOT NULL,
BookingTime time NOT NULL,
UserID INT NOT NULL,
foreign key (UserID) references User(UserID),
Guests INT NOT NULL DEFAULT 1,
OrderID INT NULL,
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
ReviewText TEXT NULL,
Rating INT NULL
);
ALTER TABLE BookingExperience
ADD COLUMN IsCancelled BOOLEAN DEFAULT FALSE;

CREATE TABLE CancelStatus (
    CancelStatusID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    StatusName VARCHAR(20) NOT NULL
);

INSERT INTO CancelStatus (StatusName)
VALUES ('Pending'), ('Approved'), ('Rejected');


CREATE TABLE CancelExperienceRequests (
  CancelRequestID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  BookingID INT NOT NULL,
  UserID INT NOT NULL,
  RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  Status VARCHAR(20) DEFAULT 'Pending',
  FOREIGN KEY (BookingID) REFERENCES BookingExperience(BookingID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE CancelDestinationRequests (
  CancelRequestID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  BookingDestinationID INT NOT NULL,
  UserID INT NOT NULL,
  RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CancelStatus VARCHAR(20) DEFAULT 'Pending',
  FOREIGN KEY (BookingDestinationID) REFERENCES BookingDestination(BookingDestinationID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);

SHOW COLUMNS FROM CancelExperienceRequests;


ALTER TABLE CancelExperienceRequests
DROP COLUMN Status;

ALTER TABLE CancelExperienceRequests
ADD COLUMN CancelStatusID INT DEFAULT 1,
ADD FOREIGN KEY (CancelStatusID) REFERENCES CancelStatus(CancelStatusID);


CREATE TABLE CancelDestinationRequests (
  CancelRequestID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  BookingDestinationID INT NOT NULL,
  UserID INT NOT NULL,
  RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CancelStatus VARCHAR(20) DEFAULT 'Pending',
  FOREIGN KEY (BookingDestinationID) REFERENCES BookingDestination(BookingDestinationID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);


CREATE TABLE PromotionalWinners (
    WinnerID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserID INT NOT NULL,
    ProductID INT NOT NULL,
    WonAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
-- DELIMITER $$

-- CREATE PROCEDURE GetExperienceDetails(IN exp_id INT)
-- BEGIN
--     SELECT 
--         ExperienceName AS name, 
--         ExperiencePrice AS price, 
--         ExperienceImage AS image, 
--         DateOfBooking AS date
--     FROM Experiences
--     WHERE ExperienceID = exp_id;
-- END $$

-- DELIMITER ;
ALTER TABLE CancelDestinationRequests
DROP COLUMN CancelStatus,
ADD COLUMN CancelStatusID INT DEFAULT 1,
ADD CONSTRAINT fk_cancelstatus FOREIGN KEY (CancelStatusID) REFERENCES CancelStatus(CancelStatusID);

-- CALL GetExperienceDetails(2);
SHOW COLUMNS FROM BookingExperience;
select * from ProductOrders;
select * from BookingExperience;
select * from Orders;
SELECT p.ProductName, po.Quantity, p.ProductPrice, p.ProductImage
        FROM ProductOrders po
        JOIN Product p ON p.ProductID = po.ProductID
        WHERE po.OrderID = 10;
SELECT OrderDate FROM Orders WHERE OrderID = 15;


 SELECT e.ExperienceName, b.BookingDate, b.BookingTime, b.Guests, e.ExperiencePrice, e.ExperienceImage
        FROM BookingExperience b
        JOIN Experiences e ON e.ExperienceID = b.ExperienceID
        WHERE b.OrderID = 15;

SELECT P.ProductName, P.ProductImage, P.ProductPrice, OP.Quantity, O.OrderDate
        FROM ProductOrders OP
        JOIN Product P ON OP.ProductID = P.ProductID
        JOIN Orders O ON OP.OrderID = O.OrderID
        WHERE O.UserID =1
        ORDER BY O.OrderDate DESC;

SELECT
            E.ExperienceName, E.ExperienceImage, E.ExperiencePrice,
            B.Guests, B.BookingDate, B.BookingTime, B.BookingID,
            (SELECT Status FROM CancelExperienceRequests
             WHERE BookingID = B.BookingID AND UserID = 1 LIMIT 1) AS CancelStatus
        FROM BookingExperience B
        JOIN Experiences E ON B.ExperienceID = E.ExperienceID
        JOIN Orders O ON B.OrderID = O.OrderID
        WHERE O.UserID = 1
        ORDER BY B.BookingDate DESC;

SELECT c.CancelRequestID, c.RequestDate, cs.StatusName AS Status, u.FirstName, u.LastName, u.Email,
               e.ExperienceName, b.BookingDate
        FROM CancelExperienceRequests c
        JOIN BookingExperience b ON c.BookingID = b.BookingID
        JOIN User u ON c.UserID = u.UserID
        JOIN Experiences e ON b.ExperienceID = e.ExperienceID
        JOIN CancelStatus cs ON c.CancelStatusID = cs.CancelStatusID
        ORDER BY c.RequestDate DESC;


select * from Product;

use login;
select * from bookingexperience;
select * from bookingdestination;
select * from Destinations;

        SELECT *
        FROM (
            SELECT 
                b.ExperienceID,
                b.ReviewText,
                b.Rating,
                b.BookingDate,
                u.FirstName,
                u.LastName,
                ROW_NUMBER() OVER (PARTITION BY b.ExperienceID ORDER BY b.BookingDate DESC) AS row_num
            FROM BookingExperience b
            JOIN User u ON b.UserID = u.UserID
            WHERE b.ReviewText IS NOT NULL AND b.ExperienceID = 1
        ) AS ranked
        WHERE row_num <= 5