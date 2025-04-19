use Login;

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