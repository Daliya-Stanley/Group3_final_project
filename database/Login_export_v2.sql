CREATE DATABASE  IF NOT EXISTS `login` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `login`;
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
  `ReviewText` text,
  `Rating` int DEFAULT NULL,
  PRIMARY KEY (`BookingID`),
  KEY `ExperienceID` (`ExperienceID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `bookingexperience_ibfk_1` FOREIGN KEY (`ExperienceID`) REFERENCES `experiences` (`ExperienceID`),
  CONSTRAINT `bookingexperience_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookingexperience`
--

LOCK TABLES `bookingexperience` WRITE;
/*!40000 ALTER TABLE `bookingexperience` DISABLE KEYS */;
INSERT INTO `bookingexperience` VALUES (1,1,'2025-04-19','09:00:00',1,1,NULL,NULL),(2,1,'2025-04-19','09:00:00',1,1,NULL,NULL),(3,1,'2025-04-19','09:00:00',1,3,NULL,NULL),(4,1,'2025-04-19','09:00:00',1,1,NULL,NULL),(5,1,'2025-04-19','09:00:00',1,3,NULL,NULL);
/*!40000 ALTER TABLE `bookingexperience` ENABLE KEYS */;
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
  PRIMARY KEY (`DestinationID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destination`
--

LOCK TABLES `destination` WRITE;
/*!40000 ALTER TABLE `destination` DISABLE KEYS */;
INSERT INTO `destination` VALUES (1,'Wonderland',100),(2,'Cinderella',125),(3,'Aquariel',100),(4,'Frozen',100),(5,'Mulan\'s World',150);
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
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `InventoryID` int NOT NULL AUTO_INCREMENT,
  `ProductID` int NOT NULL,
  `ProductStatusID` int NOT NULL,
  PRIMARY KEY (`InventoryID`),
  KEY `ProductID` (`ProductID`),
  KEY `ProductStatusID` (`ProductStatusID`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`),
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`ProductStatusID`) REFERENCES `productstatus` (`ProductStatusID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
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
  PRIMARY KEY (`ProductID`),
  KEY `ProductStatusID` (`ProductStatusID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`ProductStatusID`) REFERENCES `productstatus` (`ProductStatusID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'All You Can Pack Suitcase',200,1,'product_suitcase.jpeg'),(2,'Magical Carpet',500,1,'product_carpet.jpeg'),(3,'Magic Potion',100,1,'product-magic bottle.jpeg'),(4,'Magic Wand',50,1,'magical_wand.jpeg'),(5,'Spectacular One Dress - No Mess',100,1,'product_clothes.jpeg');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productstatus`
--

LOCK TABLES `productstatus` WRITE;
/*!40000 ALTER TABLE `productstatus` DISABLE KEYS */;
INSERT INTO `productstatus` VALUES (1,'Available'),(2,'Not Available');
/*!40000 ALTER TABLE `productstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping`
--

DROP TABLE IF EXISTS `shopping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping` (
  `ShoppingID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `InventoryID` int NOT NULL,
  `ExperienceID` int NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`ShoppingID`),
  KEY `UserID` (`UserID`),
  KEY `InventoryID` (`InventoryID`),
  KEY `ExperienceID` (`ExperienceID`),
  CONSTRAINT `shopping_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `shopping_ibfk_2` FOREIGN KEY (`InventoryID`) REFERENCES `inventory` (`InventoryID`),
  CONSTRAINT `shopping_ibfk_3` FOREIGN KEY (`ExperienceID`) REFERENCES `experiences` (`ExperienceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping`
--

LOCK TABLES `shopping` WRITE;
/*!40000 ALTER TABLE `shopping` DISABLE KEYS */;
/*!40000 ALTER TABLE `shopping` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Anna','Kout','anna.koutsaki@outlook.com','$2b$12$WfZw5IJW9dug8HPIJjoZnuTm2bZw30Wz7wJNLJ5A6QDAXTy7awfGS');
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

-- Dump completed on 2025-04-18 23:29:43
