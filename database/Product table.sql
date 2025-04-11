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

INSERT INTO Product (ProductName, ProductPrice, ProductImage)
VALUES 
('All You Can Pack Suitcase','£200', 'product_suitcase.jpeg'),
('Magical Carpet','£500', 'product_carpet.jpeg'),
('Magic Potion','£100', 'product-magic bottle.jpeg'),
('Magic Wand','£50', 'magical_wand.jpeg'),
('Spectacular One Dress - No Mess','£100', 'product_clothes.jpeg');