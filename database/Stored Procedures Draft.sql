Stored Procedures:

DELIMITER //

CREATE PROCEDURE pRetrieve_All_Users()
BEGIN
SELECT * FROM User;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE pRetrieve_All_Bookings()
BEGIN
SELECT * FROM Booking;
END //

DELIMITER ;

DELIMITER // 

CREATE PROCEDURE pGet_Available_Products(
IN pStatus varchar(25)
)
BEGIN
SELECT * FROM ProductStatus 
WHERE Status = Available;
END //

DELIMITER ;

DELIMITER // 

CREATE PROCEDURE pGet_Available_Products(
IN pStatus varchar(25)
)
BEGIN
SELECT * FROM ProductStatus 
WHERE Status = Available;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE pGet_Booked_Experiences(
IN pDateReserved DATE
)
BEGIN
SELECT * FROM Experiences 
WHERE DateReserved = pDateReserved;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE pRetrieve_Products_Purchased()
BEGIN
SELECT * FROM Shopping;
END //

DELIMITER ;

