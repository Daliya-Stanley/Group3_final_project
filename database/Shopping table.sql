use Login;

create table Shopping
(
ShoppingID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
UserID INT NOT NULL,
foreign key (UserID) references User(UserID),
InventoryID INT NOT NULL,
foreign key (InventoryID) references Inventory(InventoryID),
ExperienceID INT NOT NULL,
foreign key (ExperienceID) references Experience(ExperienceID),
Date date NOT NULL
);