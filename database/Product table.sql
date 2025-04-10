use Login;

create table Product
(
ProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ProductName VARCHAR(100) NOT NULL,
ProductPrice INT NOT NULL,
ProductStatusID INT NOT NULL,
foreign key (ProductStatusID) references ProductStatus(ProductStatusID)
);

alter table Product
add column ProductImage VARCHAR (50) NOT NULL;