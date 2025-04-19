use Login;

create table Inventory
(
Inventory INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
ProductID INT NOT NULL,
foreign key (ProductID) references Product(ProductID),
ProductStatusID INT NOT NULL,
foreign key (ProductStatusID) references ProductStatus(ProductStatusID)
);
alter table Inventory 
change column Inventory InventoryID INT;

