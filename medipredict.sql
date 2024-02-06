-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: medipredict
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `breastcancer`
--

DROP TABLE IF EXISTS `breastcancer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breastcancer` (
  `name` varchar(255) DEFAULT NULL,
  `radius_mean` float DEFAULT NULL,
  `texture_mean` float DEFAULT NULL,
  `perimeter_mean` float DEFAULT NULL,
  `area_mean` float DEFAULT NULL,
  `perimeter_se` float DEFAULT NULL,
  `area_se` float DEFAULT NULL,
  `radius_worst` float DEFAULT NULL,
  `texture_worst` float DEFAULT NULL,
  `perimeter_worst` float DEFAULT NULL,
  `area_worst` float DEFAULT NULL,
  `breast_val` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breastcancer`
--

LOCK TABLES `breastcancer` WRITE;
/*!40000 ALTER TABLE `breastcancer` DISABLE KEYS */;
INSERT INTO `breastcancer` VALUES ('preeti',16.76,24.54,47.92,281,12.548,119.15,9.456,30.37,59.16,68.6,0);
/*!40000 ALTER TABLE `breastcancer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diabetes`
--

DROP TABLE IF EXISTS `diabetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diabetes` (
  `name` varchar(50) DEFAULT NULL,
  `preg` int DEFAULT NULL,
  `gluc` int DEFAULT NULL,
  `bp` int DEFAULT NULL,
  `ins` int DEFAULT NULL,
  `bmi` float DEFAULT NULL,
  `dpf` float DEFAULT NULL,
  `age` float DEFAULT NULL,
  `diabet_val` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diabetes`
--

LOCK TABLES `diabetes` WRITE;
/*!40000 ALTER TABLE `diabetes` DISABLE KEYS */;
INSERT INTO `diabetes` VALUES ('Linga Reddy',0,180,72,12,39,0.35,21,1),('Linga Reddy',0,180,72,12,39,0.35,21,1);
/*!40000 ALTER TABLE `diabetes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heart`
--

DROP TABLE IF EXISTS `heart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heart` (
  `name` varchar(200) DEFAULT NULL,
  `age` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `bp_hi` float DEFAULT NULL,
  `bp_lo` float DEFAULT NULL,
  `chol` float DEFAULT NULL,
  `gluc` float DEFAULT NULL,
  `alco` float DEFAULT NULL,
  `active` float DEFAULT NULL,
  `result` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heart`
--

LOCK TABLES `heart` WRITE;
/*!40000 ALTER TABLE `heart` DISABLE KEYS */;
INSERT INTO `heart` VALUES ('Linga Reddy',21,71,130,72,1,1,0,1,0);
/*!40000 ALTER TABLE `heart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'medipredict'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-30 18:25:13
