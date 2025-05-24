-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: login
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookingdestination`
--

DROP TABLE IF EXISTS `bookingdestination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookingdestination` (
  `BookingDestinationID` int NOT NULL AUTO_INCREMENT,
  `DestinationID` int NOT NULL,
  `BookingStartDate` date NOT NULL,
  `BookingEndDate` date NOT NULL,
  `UserID` int NOT NULL,
  `Guests` int NOT NULL DEFAULT '1',
  `OrderID` int DEFAULT NULL,
  `ReviewText` text,
  `Rating` int DEFAULT NULL,
  PRIMARY KEY (`BookingDestinationID`),
  KEY `DestinationID` (`DestinationID`),
  KEY `UserID` (`UserID`),
  KEY `OrderID` (`OrderID`),
  CONSTRAINT `bookingdestination_ibfk_1` FOREIGN KEY (`DestinationID`) REFERENCES `destination` (`DestinationID`),
  CONSTRAINT `bookingdestination_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `bookingdestination_ibfk_3` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookingdestination`
--

LOCK TABLES `bookingdestination` WRITE;
/*!40000 ALTER TABLE `bookingdestination` DISABLE KEYS */;
INSERT INTO `bookingdestination` VALUES (1,2,'2025-04-29','2025-04-30',16,2,12,NULL,NULL),(2,1,'2025-05-01','2025-05-08',17,2,13,NULL,NULL),(3,2,'2025-04-23','2025-04-25',8,2,15,NULL,NULL),(6,4,'2025-05-18','2025-05-25',20,2,18,NULL,NULL);
/*!40000 ALTER TABLE `bookingdestination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookingexperience`
--

DROP TABLE IF EXISTS `bookingexperience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookingexperience` (
  `BookingID` int NOT NULL AUTO_INCREMENT,
  `ExperienceID` int NOT NULL,
  `BookingDate` date NOT NULL,
  `BookingTime` time NOT NULL,
  `UserID` int NOT NULL,
  `Guests` int NOT NULL DEFAULT '1',
  `OrderID` int DEFAULT NULL,
  `ReviewText` text,
  `Rating` int DEFAULT NULL,
  `IsCancelled` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`BookingID`),
  KEY `ExperienceID` (`ExperienceID`),
  KEY `UserID` (`UserID`),
  KEY `OrderID` (`OrderID`),
  CONSTRAINT `bookingexperience_ibfk_1` FOREIGN KEY (`ExperienceID`) REFERENCES `experiences` (`ExperienceID`),
  CONSTRAINT `bookingexperience_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `bookingexperience_ibfk_3` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookingexperience`
--

LOCK TABLES `bookingexperience` WRITE;
/*!40000 ALTER TABLE `bookingexperience` DISABLE KEYS */;
INSERT INTO `bookingexperience` VALUES (2,1,'2025-04-23','11:00:00',2,1,2,'As a mum of two energetic toddlers, I’m always on the lookout for activities that are fun, safe, and truly magical — and Make a Snowman with Anna and her Frozen friends ticked every box! The staff were incredibly warm and welcoming, and made sure even the youngest little ones felt included. Highly recommend this for families with young kids.',5,0),(3,1,'2025-04-23','11:00:00',1,1,3,'Had an amazing time making a Snowman! My kids absolutely loved every minute — from meeting Anna to building our very own snowman. Great atmosphere, super friendly team, and perfect for young children. Worth every moment.',5,0),(4,2,'2025-04-23','09:00:00',4,1,4,'Went to the Troll Party... danced like nobody was watching , sang like a rockstar (off-key), and left with glitter in places glitter should not be. 10/10 would party with Trolls again!',5,0),(5,3,'2025-04-23','11:00:00',5,1,5,'Had an amazing time at the Troll Party! The music, dancing, and energy were next level — pure joy from start to finish. Definitely one of the most fun experiences I’ve had in a while!',5,0),(6,4,'2025-04-23','10:00:00',6,1,6,'Scuba diving with Ariel was absolutely breathtaking, but the real MVP was Anna from the staff — she made me feel so safe and confident in the water! Thank you for turning nerves into magic.',5,0),(7,5,'2025-04-23','09:00:00',7,1,7,'The spa experience was incredible, and Daphne made it even more special! She was attentive, friendly, and really made me feel like royalty. The whole day was bliss — thank you, Daphne, for making it unforgettable!',5,0),(8,2,'2025-04-23','09:00:00',4,1,8,'The Flying Lesson was absolutely incredible! My partner and I felt like we were truly soaring above Agrabah. The views were breathtaking, and the whole experience was pure magic. Totally worth it for a once-in-a-lifetime adventure!',5,0),(9,1,'2025-04-23','09:00:00',11,1,9,NULL,NULL,0),(10,1,'2025-04-23','09:00:00',12,2,10,NULL,NULL,1),(11,1,'2025-04-30','09:00:00',16,1,12,'It was an amazing experience!',5,0),(12,2,'2025-05-03','12:00:00',17,2,13,'It\'s awesome!!',5,0),(13,1,'2025-04-30','09:00:00',8,1,14,NULL,NULL,0),(14,1,'2025-04-23','09:00:00',8,1,15,NULL,NULL,0),(15,1,'2025-04-29','09:00:00',8,1,16,NULL,NULL,0),(17,1,'2025-05-19','09:00:00',20,1,18,'Loved building a snowman along with Olaf!',5,0);
/*!40000 ALTER TABLE `bookingexperience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `canceldestinationrequests`
--

DROP TABLE IF EXISTS `canceldestinationrequests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canceldestinationrequests` (
  `CancelRequestID` int NOT NULL AUTO_INCREMENT,
  `BookingDestinationID` int NOT NULL,
  `UserID` int NOT NULL,
  `RequestDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `CancelStatusID` int DEFAULT '1',
  PRIMARY KEY (`CancelRequestID`),
  KEY `BookingDestinationID` (`BookingDestinationID`),
  KEY `UserID` (`UserID`),
  KEY `fk_cancelstatus` (`CancelStatusID`),
  CONSTRAINT `canceldestinationrequests_ibfk_1` FOREIGN KEY (`BookingDestinationID`) REFERENCES `bookingdestination` (`BookingDestinationID`),
  CONSTRAINT `canceldestinationrequests_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `fk_cancelstatus` FOREIGN KEY (`CancelStatusID`) REFERENCES `cancelstatus` (`CancelStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canceldestinationrequests`
--

LOCK TABLES `canceldestinationrequests` WRITE;
/*!40000 ALTER TABLE `canceldestinationrequests` DISABLE KEYS */;
INSERT INTO `canceldestinationrequests` VALUES (1,1,16,'2025-04-22 17:56:43',1),(2,2,17,'2025-04-22 19:27:56',3),(4,6,20,'2025-04-24 18:28:57',3);
/*!40000 ALTER TABLE `canceldestinationrequests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancelexperiencerequests`
--

DROP TABLE IF EXISTS `cancelexperiencerequests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancelexperiencerequests` (
  `CancelRequestID` int NOT NULL AUTO_INCREMENT,
  `BookingID` int NOT NULL,
  `UserID` int NOT NULL,
  `RequestDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `CancelStatusID` int DEFAULT '1',
  PRIMARY KEY (`CancelRequestID`),
  KEY `BookingID` (`BookingID`),
  KEY `UserID` (`UserID`),
  KEY `CancelStatusID` (`CancelStatusID`),
  CONSTRAINT `cancelexperiencerequests_ibfk_1` FOREIGN KEY (`BookingID`) REFERENCES `bookingexperience` (`BookingID`),
  CONSTRAINT `cancelexperiencerequests_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `cancelexperiencerequests_ibfk_3` FOREIGN KEY (`CancelStatusID`) REFERENCES `cancelstatus` (`CancelStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancelexperiencerequests`
--

LOCK TABLES `cancelexperiencerequests` WRITE;
/*!40000 ALTER TABLE `cancelexperiencerequests` DISABLE KEYS */;
INSERT INTO `cancelexperiencerequests` VALUES (2,4,4,'2025-04-22 15:01:14',2),(3,10,12,'2025-04-22 16:56:17',2),(4,12,17,'2025-04-22 19:27:49',2);
/*!40000 ALTER TABLE `cancelexperiencerequests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancelstatus`
--

DROP TABLE IF EXISTS `cancelstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancelstatus` (
  `CancelStatusID` int NOT NULL AUTO_INCREMENT,
  `StatusName` varchar(20) NOT NULL,
  PRIMARY KEY (`CancelStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancelstatus`
--

LOCK TABLES `cancelstatus` WRITE;
/*!40000 ALTER TABLE `cancelstatus` DISABLE KEYS */;
INSERT INTO `cancelstatus` VALUES (1,'Pending'),(2,'Approved'),(3,'Rejected');
/*!40000 ALTER TABLE `cancelstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destination`
--

DROP TABLE IF EXISTS `destination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destination` (
  `DestinationID` int NOT NULL AUTO_INCREMENT,
  `DestinationName` varchar(25) NOT NULL,
  `DestinationPricePerNight` int NOT NULL,
  `DestinationImage` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`DestinationID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destination`
--

LOCK TABLES `destination` WRITE;
/*!40000 ALTER TABLE `destination` DISABLE KEYS */;
INSERT INTO `destination` VALUES (1,'Wonderland',100,'WT.JPG'),(2,'Cinderella',125,'cinderella.jpg'),(3,'Aquariel',100,'ariel_topsection.jpg'),(4,'Frozen',100,'frozen_main.jpeg'),(5,'Mulan\'s World',150,'mulan.png');
/*!40000 ALTER TABLE `destination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencelevel`
--

DROP TABLE IF EXISTS `experiencelevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencelevel` (
  `ExperienceLevelID` int NOT NULL AUTO_INCREMENT,
  `ExperienceLevelKey` varchar(20) NOT NULL,
  PRIMARY KEY (`ExperienceLevelID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencelevel`
--

LOCK TABLES `experiencelevel` WRITE;
/*!40000 ALTER TABLE `experiencelevel` DISABLE KEYS */;
INSERT INTO `experiencelevel` VALUES (1,'Light'),(2,'Moderate'),(3,'High');
/*!40000 ALTER TABLE `experiencelevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiences`
--

DROP TABLE IF EXISTS `experiences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiences` (
  `ExperienceID` int NOT NULL AUTO_INCREMENT,
  `ExperienceName` varchar(50) NOT NULL,
  `ExperiencePrice` int NOT NULL,
  `ExperienceImage` varchar(50) NOT NULL,
  `ExperienceDescription` text NOT NULL,
  `ExperienceDuration` int NOT NULL,
  `ExperienceLevelID` int NOT NULL,
  `ExperienceMinAge` int NOT NULL,
  `ExperienceGroupSize` int NOT NULL,
  PRIMARY KEY (`ExperienceID`),
  KEY `ExperienceLevelID` (`ExperienceLevelID`),
  CONSTRAINT `experiences_ibfk_1` FOREIGN KEY (`ExperienceLevelID`) REFERENCES `experiencelevel` (`ExperienceLevelID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiences`
--

LOCK TABLES `experiences` WRITE;
/*!40000 ALTER TABLE `experiences` DISABLE KEYS */;
INSERT INTO `experiences` VALUES (1,'Make a Snowman',50,'Experience-snowman.jpeg','Join Anna and her Frozen friends for a magical snowman-making adventure where laughter, snowflakes, and enchantment come to life!',2,2,5,10),(2,'Flying Lesson',250,'Experience-carpet.jpeg','Soar above the clouds with Aladdin on a magical flying carpet ride—an unforgettable adventure straight out of Agrabah!',1,3,8,4),(3,'Troll Party',50,'Experience-Troll.jpeg','Get ready to dance, sing, and sparkle in the ultimate feel-good party with the Trolls—where every moment is a burst of magic and music!',3,1,4,15),(4,'Scuba Diving',250,'Experience-Scuba.jpeg','Dive into an underwater wonderland with Ariel and explore vibrant reefs, shimmering treasures, and ocean magic like never before!',6,3,10,6),(5,'Spa Experience',100,'Experience-Spa.jpeg','Indulge in a royal spa day at Princess Aurora’s castle, where enchantment meets elegance for the ultimate fairy-tale pampering!',4,1,12,5);
/*!40000 ALTER TABLE `experiences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `OrderID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `OrderDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`OrderID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'2025-04-22 14:19:47'),(2,2,'2025-04-22 14:24:28'),(3,1,'2025-04-22 14:37:02'),(4,4,'2025-04-22 14:40:35'),(5,5,'2025-04-22 14:42:50'),(6,6,'2025-04-22 14:56:54'),(7,7,'2025-04-22 14:59:44'),(8,4,'2025-04-22 15:02:56'),(9,11,'2025-04-22 16:31:43'),(10,12,'2025-04-22 16:53:47'),(11,14,'2025-04-22 17:29:06'),(12,16,'2025-04-22 17:56:25'),(13,17,'2025-04-22 19:24:38'),(14,8,'2025-04-22 20:30:51'),(15,8,'2025-04-22 22:10:11'),(16,8,'2025-04-24 10:54:43'),(18,20,'2025-04-24 18:25:06');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderstatus`
--

DROP TABLE IF EXISTS `orderstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderstatus` (
  `OrderStatusID` int NOT NULL AUTO_INCREMENT,
  `StatusName` varchar(20) NOT NULL,
  PRIMARY KEY (`OrderStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderstatus`
--

LOCK TABLES `orderstatus` WRITE;
/*!40000 ALTER TABLE `orderstatus` DISABLE KEYS */;
INSERT INTO `orderstatus` VALUES (1,'Pending'),(2,'Shipped'),(3,'Delivered');
/*!40000 ALTER TABLE `orderstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `ProductID` int NOT NULL AUTO_INCREMENT,
  `ProductName` varchar(100) NOT NULL,
  `ProductPrice` int NOT NULL,
  `ProductStatusID` int NOT NULL,
  `ProductImage` varchar(50) NOT NULL,
  `ProductDescription` text,
  PRIMARY KEY (`ProductID`),
  KEY `ProductStatusID` (`ProductStatusID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`ProductStatusID`) REFERENCES `productstatus` (`ProductStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'All You Can Pack Suitcase',200,1,'product_suitcase.jpeg','A bottomless suitcase that fits everything you need for an epic adventure.'),(2,'Magical Carpet',500,1,'product_carpet.jpeg','A flying carpet that whisks you away to your destination in style.'),(3,'Magic Potion',100,1,'product-magic bottle.jpeg','A mysterious elixir with enchanting effects and which heals your heart and body.'),(4,'Magic Wand',50,1,'magical_wand.jpeg','A sleek wand that channels your inner wizard with a flick and a spark and get your house squeaky clean.'),(5,'Spectacular One Dress - No Mess',100,1,'product_clothes.jpeg','A magical outfit that transforms into any style with zero effort.'),(6,'All You Can Pack Suitcase - Free',0,3,'product_suitcase.jpeg',NULL),(7,'Magical Carpet - Free',0,3,'product_carpet.jpeg',NULL),(8,'Magic Potion - Free',0,3,'product-magic bottle.jpeg',NULL),(9,'Magic Wand - Free',0,3,'magical_wand.jpeg',NULL),(10,'One Dress - No Mess - Free',0,3,'product_clothes.jpeg',NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productorders`
--

DROP TABLE IF EXISTS `productorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productorders` (
  `ProductOrdersID` int NOT NULL AUTO_INCREMENT,
  `ProductID` int NOT NULL,
  `UserID` int NOT NULL,
  `Quantity` int NOT NULL,
  `OrderDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `OrderID` int NOT NULL,
  `OrderStatusID` int DEFAULT '1',
  PRIMARY KEY (`ProductOrdersID`),
  KEY `ProductID` (`ProductID`),
  KEY `UserID` (`UserID`),
  KEY `OrderID` (`OrderID`),
  KEY `OrderStatusID` (`OrderStatusID`),
  CONSTRAINT `productorders_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`),
  CONSTRAINT `productorders_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `productorders_ibfk_3` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`),
  CONSTRAINT `productorders_ibfk_4` FOREIGN KEY (`OrderStatusID`) REFERENCES `orderstatus` (`OrderStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productorders`
--

LOCK TABLES `productorders` WRITE;
/*!40000 ALTER TABLE `productorders` DISABLE KEYS */;
INSERT INTO `productorders` VALUES (1,2,11,1,'2025-04-22 16:31:43',9,3),(2,3,12,1,'2025-04-22 16:53:48',10,1),(3,7,12,1,'2025-04-22 16:53:48',10,1),(4,2,14,1,'2025-04-22 17:29:06',11,1),(5,1,16,2,'2025-04-22 17:56:25',12,1),(6,10,17,1,'2025-04-22 19:24:38',13,3),(7,4,17,1,'2025-04-22 19:24:38',13,3),(8,2,8,1,'2025-04-22 22:10:11',15,1),(9,3,8,1,'2025-04-24 10:54:43',16,3),(12,7,20,1,'2025-04-24 18:25:06',18,1),(13,4,20,1,'2025-04-24 18:25:06',18,1),(14,1,20,1,'2025-04-24 18:25:06',18,1);
/*!40000 ALTER TABLE `productorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productstatus`
--

DROP TABLE IF EXISTS `productstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productstatus` (
  `ProductStatusID` int NOT NULL AUTO_INCREMENT,
  `Status` varchar(20) NOT NULL,
  PRIMARY KEY (`ProductStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productstatus`
--

LOCK TABLES `productstatus` WRITE;
/*!40000 ALTER TABLE `productstatus` DISABLE KEYS */;
INSERT INTO `productstatus` VALUES (1,'Available'),(2,'Not Available'),(3,'Promotion');
/*!40000 ALTER TABLE `productstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promotionalwinners`
--

DROP TABLE IF EXISTS `promotionalwinners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promotionalwinners` (
  `WinnerID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `ProductID` int NOT NULL,
  `WonAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`WinnerID`),
  KEY `UserID` (`UserID`),
  KEY `ProductID` (`ProductID`),
  CONSTRAINT `promotionalwinners_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `promotionalwinners_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotionalwinners`
--

LOCK TABLES `promotionalwinners` WRITE;
/*!40000 ALTER TABLE `promotionalwinners` DISABLE KEYS */;
/*!40000 ALTER TABLE `promotionalwinners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Password` (`Password`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Kenny','Dash','kenny@gmail.com','$2b$12$3mQgj23x3Gf8yDZDKoBiUOCSWKPUC7Nd7TFL0G.jY3QlNrE0nPWNS'),(2,'Grace ','Spencer','Grace@gmail.com','$2b$12$XEazpZSw8NsB0e9UtBpyS.yWHc01uITC41bZJacaudF9kAIAvw4BO'),(3,'Titi','Ejembi','admin@egt.magic','$2b$12$bYpazZrNEGCdK9dUCixsnOZ4xQW6ikLOVYDnmkYr7CcruP9fTSBxi'),(4,'Taylor','Swift','tay@gmail.com','$2b$12$D/0ebuJcCBNMMFkrd7za0OL0jiTbvFXm6/EYr47IsYjf.IvUVEXnm'),(5,'Oche ','Ejembi','oche@gmail.com','$2b$12$JpRBCLSlR3eJvnOMnSf/BePbGPFQWvUH0nwVoMBTPe6I3rG55cY6m'),(6,'Arin','Waters','arin@gmail.com','$2b$12$mdafkiKpfU9xkNuLpyDRIOwBOUKqloKaAxPLMRNdh.iCtwft3yFVy'),(7,'lena','hart','lena@gmail.com','$2b$12$lU3wuF1z12RAukcLcf.2ReMO/yMmrJDE8nwN.L6ZKV2m1DNAcK0au'),(8,'Anna','Kout','anna@gmail.com','$2b$12$q4jlSDN6YpPwnw45hapUyu5ewn/B8kDCkxnXhGLbPGtDPRC9pXRJi'),(9,'Anna','Kout','anna@outlook.com','$2b$12$gbNCKJPlS2e3jJR/AJ3dSep4PbLfsf5ahHbiZV.f4rf2gU1/NI50S'),(10,'Elena','Kout','elena@gmail.com','$2b$12$.DvV1IsAi.NH7.5iDYe5Q.mmstPQJDjRJhdB06ZJCzxIvRDzshHCe'),(11,'Emma','Tudor','emma@gmail.com','$2b$12$pFk6WEJa4OMiTKANe2OUCeFLBfnF4/fpckf7svzvTnsFlUD0M7kOG'),(12,'Daphne','Sisi','daphnesisi@gmail.com','$2b$12$D.CHImg3EyFOmklzMdwEyuKeZN7BR32ncxfomOIyOYxM5BXlBKCh.'),(13,'Kate','Koutsaki','kate@gmail.com','$2b$12$F79zFuYAF2lm6O2MgXNrze0Z6FfEDO9tHoyNP776bXVa7lvA9oELG'),(14,'Kate','Kout','kate1@gmail.com','$2b$12$RSEwjG5jVHzJrU5PNAJ2c.NfroM5p3GDKPn5AxDS8FNAOohzOOVC.'),(15,'Ariel','Magic','ariel@gmail.com','$2b$12$izkYbV3lTfuSOmu./2EZ..ISDX4rkZt.UvHXe00puSG5JeLudWL3m'),(16,'Ariel','Magic','ariel2@gmail.com','$2b$12$dJk.dirMXe88ve3paXX9kOxHIs2uUPcU.oEPCEJToL5xJTsF47p9a'),(17,'Victoria','Lloyd','victoria@gmail.com','$2b$12$duZMQ7wAZFPWwx3/nyyy0OFMNAZ7viHb7qkH/kjPeL4H/f8bEzQUy'),(18,'Ariana','Grande','ariana@gmail.com','$2b$12$aBYd7XAUevfJVzOB/zh5uOV4ASn1UKGR0IRPQ1eqN7tw34I1fCjM6'),(19,'Titi','Ejembi','titi@gmail.com','$2b$12$wc1haQEEeNXCU5Qsc2B1B.E/D7KvDke3giCdDH8bPsbrpcHAd.Im2'),(20,'Shona','Traveller','fly@gmail.com','$2b$12$uRz35Or6SqVSKhPZlh26yusUfMDDDLfrNacn9JXM1WA89A8MNdcu6');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'login'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-24 11:50:48
