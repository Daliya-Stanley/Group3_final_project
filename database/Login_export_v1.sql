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
  PRIMARY KEY (`BookingID`),
  KEY `ExperienceID` (`ExperienceID`),
  CONSTRAINT `bookingexperience_ibfk_1` FOREIGN KEY (`ExperienceID`) REFERENCES `experiences` (`ExperienceID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookingexperience`
--

LOCK TABLES `bookingexperience` WRITE;
/*!40000 ALTER TABLE `bookingexperience` DISABLE KEYS */;
INSERT INTO `bookingexperience` VALUES (2,3,'2025-04-30','09:00:00'),(3,2,'2025-04-23','09:00:00'),(4,2,'2025-04-30','09:00:00'),(5,2,'2025-04-30','09:00:00'),(6,2,'2025-04-30','09:00:00'),(7,2,'2025-04-29','13:00:00'),(8,2,'2025-04-24','09:00:00'),(9,2,'2025-04-29','09:00:00'),(10,2,'2025-04-30','09:00:00'),(11,2,'2025-04-29','09:00:00'),(12,2,'2025-04-29','09:00:00'),(13,2,'2025-04-29','09:00:00'),(14,2,'2025-04-29','09:00:00'),(15,2,'2025-04-29','09:00:00'),(16,2,'2025-04-22','09:00:00');
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
  `DateReserved` date DEFAULT NULL,
  PRIMARY KEY (`ExperienceID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiences`
--

LOCK TABLES `experiences` WRITE;
/*!40000 ALTER TABLE `experiences` DISABLE KEYS */;
INSERT INTO `experiences` VALUES (1,'Make a Snowman',50,'Experience-snowman.jpeg',NULL),(2,'Flying Lesson',250,'Experience-carpet.jpeg',NULL),(3,'Troll Party',50,'Experience-Troll.jpeg',NULL),(4,'Scuba Diving',250,'Experience-Scuba.jpeg',NULL),(5,'Spa Experience',100,'Experience-Spa.jpeg',NULL);
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
INSERT INTO `user` VALUES (1,'Anna','Koutsaki','anna.koutsaki@outlook.com','$2b$12$FNdeOV3Hm/vNAOcTQEgxxOSTiF5tGSX4owO3xIJn.J/aDLegOl5eW');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'login'
--
/*!50003 DROP PROCEDURE IF EXISTS `GetExperienceDetails` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetExperienceDetails`(IN exp_id INT)
BEGIN
    SELECT 
        ExperienceName AS name, 
        ExperiencePrice AS price, 
        ExperienceImage AS image, 
        DateReserved AS date
    FROM Experiences
    WHERE ExperienceID = exp_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-15 22:25:27
