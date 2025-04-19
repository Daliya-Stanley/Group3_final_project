use Login;

create table FreeProduct (
  FreeProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  UserID INT NOT NULL,
  ProductID INT NOT NULL,
  DateAwarded DATETIME DEFAULT CURRENT_TIMESTAMP,

  foreign key (UserID) references User(UserID),
  foreign key (ProductID) references Product(ProductID)
);

drop table FreeProduct;


CREATE TABLE FreeProduct (
    FreeProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FreeProductName VARCHAR(100) NOT NULL,
    FreeProductPrice VARCHAR(100) NOT NULL,
    FreeProductStatusID INT NOT NULL,
    ProductImage VARCHAR(50) NOT NULL,
    FOREIGN KEY (FreeProductStatusID) REFERENCES ProductStatus(ProductStatusID)
);


INSERT INTO FreeProduct (FreeProductName, FreeProductPrice, FreeProductStatusID, ProductImage)
VALUES
('All You Can Pack Suitcase', 'free', 1, 'product_suitcase.jpeg'),
('Magical Carpet', 'free', 1, 'product_carpet.jpeg'),
('Magic Potion', 'free', 1, 'product-magic_bottle.jpeg'),
('Magic Wand', 'free', 1, 'magical_wand.jpeg'),
('Spectacular One Dress - No Mess', 'free', 1, 'product_clothes.jpeg');


CREATE TABLE BookFreeProduct (
    BookFreeProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserID INT NOT NULL,
    FreeProductID INT NOT NULL,
    DateAwarded DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (FreeProductID) REFERENCES FreeProduct(FreeProductID)
);

select * from FreeProduct;