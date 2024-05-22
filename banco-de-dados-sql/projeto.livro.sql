-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: livros
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `armario`
--

DROP TABLE IF EXISTS `armario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `armario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `armario`
--

LOCK TABLES `armario` WRITE;
/*!40000 ALTER TABLE `armario` DISABLE KEYS */;
/*!40000 ALTER TABLE `armario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `divisao`
--

DROP TABLE IF EXISTS `divisao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `divisao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(20) NOT NULL,
  `id_armario` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_id_armario` (`id_armario`),
  CONSTRAINT `fk_id_armario` FOREIGN KEY (`id_armario`) REFERENCES `armario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `divisao`
--

LOCK TABLES `divisao` WRITE;
/*!40000 ALTER TABLE `divisao` DISABLE KEYS */;
/*!40000 ALTER TABLE `divisao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estoque`
--

DROP TABLE IF EXISTS `estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estoque` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) DEFAULT NULL,
  `numero_nota` varchar(30) DEFAULT NULL,
  `material_didatico_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_estoque_material_didatico` (`material_didatico_id`),
  CONSTRAINT `fk_estoque_material_didatico` FOREIGN KEY (`material_didatico_id`) REFERENCES `material_didatico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estoque`
--

LOCK TABLES `estoque` WRITE;
/*!40000 ALTER TABLE `estoque` DISABLE KEYS */;
INSERT INTO `estoque` VALUES (1,'Livros de Matemática','123456',NULL),(2,'Livros de História','789012',NULL),(3,'Livros de Biologia','345678',NULL);
/*!40000 ALTER TABLE `estoque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_didatico`
--

DROP TABLE IF EXISTS `material_didatico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_didatico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(30) DEFAULT NULL,
  `titulo` varchar(30) DEFAULT NULL,
  `data_publicacao` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_didatico`
--

LOCK TABLES `material_didatico` WRITE;
/*!40000 ALTER TABLE `material_didatico` DISABLE KEYS */;
INSERT INTO `material_didatico` VALUES (1,'Matemática','Álgebra Linear','2023-01-15'),(2,'História','História do Brasil','2022-09-20'),(3,'Biologia','Biologia Celular','2023-05-10');
/*!40000 ALTER TABLE `material_didatico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_didatico_repografia`
--

DROP TABLE IF EXISTS `material_didatico_repografia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_didatico_repografia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_material_didatico` int DEFAULT NULL,
  `id_repografia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_material_didatico_repografia_material` (`id_material_didatico`),
  KEY `fk_id_repografia` (`id_repografia`),
  CONSTRAINT `fk_id_repografia` FOREIGN KEY (`id_repografia`) REFERENCES `repografia` (`id`),
  CONSTRAINT `fk_material_didatico_repografia_material` FOREIGN KEY (`id_material_didatico`) REFERENCES `material_didatico` (`id`),
  CONSTRAINT `fk_material_didatico_repografia_turma` FOREIGN KEY (`id_repografia`) REFERENCES `turma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_didatico_repografia`
--

LOCK TABLES `material_didatico_repografia` WRITE;
/*!40000 ALTER TABLE `material_didatico_repografia` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_didatico_repografia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_didatico_turma`
--

DROP TABLE IF EXISTS `material_didatico_turma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_didatico_turma` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_material_didatico` int DEFAULT NULL,
  `id_turma` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_material_didatico` (`id_material_didatico`),
  KEY `fk_turma` (`id_turma`),
  CONSTRAINT `fk_material_didatico` FOREIGN KEY (`id_material_didatico`) REFERENCES `material_didatico` (`id`),
  CONSTRAINT `fk_turma` FOREIGN KEY (`id_turma`) REFERENCES `turma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_didatico_turma`
--

LOCK TABLES `material_didatico_turma` WRITE;
/*!40000 ALTER TABLE `material_didatico_turma` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_didatico_turma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimentacao`
--

DROP TABLE IF EXISTS `movimentacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimentacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int DEFAULT NULL,
  `tipo` varchar(30) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `material_didatico_id` int DEFAULT NULL,
  `estoque_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_movimentacao_material_didatico` (`material_didatico_id`),
  KEY `fk_movimentacao_estoque` (`estoque_id`),
  CONSTRAINT `fk_movimentacao_estoque` FOREIGN KEY (`estoque_id`) REFERENCES `estoque` (`id`),
  CONSTRAINT `fk_movimentacao_material_didatico` FOREIGN KEY (`material_didatico_id`) REFERENCES `material_didatico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimentacao`
--

LOCK TABLES `movimentacao` WRITE;
/*!40000 ALTER TABLE `movimentacao` DISABLE KEYS */;
INSERT INTO `movimentacao` VALUES (1,100,'Entrada','2023-02-05',NULL,NULL),(2,50,'Saída','2023-04-12',NULL,NULL),(3,30,'Entrada','2023-06-20',NULL,NULL);
/*!40000 ALTER TABLE `movimentacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `observacao`
--

DROP TABLE IF EXISTS `observacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `observacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_observacao` date DEFAULT NULL,
  `descricao` varchar(120) DEFAULT NULL,
  `id_professor` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_professor` (`id_professor`),
  CONSTRAINT `id_professor` FOREIGN KEY (`id_professor`) REFERENCES `professor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `observacao`
--

LOCK TABLES `observacao` WRITE;
/*!40000 ALTER TABLE `observacao` DISABLE KEYS */;
INSERT INTO `observacao` VALUES (1,'2023-03-10','Livros em boas condições',NULL),(2,'2023-04-25','Livros com algumas páginas rasgadas',NULL),(3,'2023-06-05','Livros com anotações nas margens',NULL);
/*!40000 ALTER TABLE `observacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `observacao_material`
--

DROP TABLE IF EXISTS `observacao_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `observacao_material` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_observacao` int DEFAULT NULL,
  `id_material_didatico` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_obse` (`id_observacao`),
  KEY `fk_mater` (`id_material_didatico`),
  CONSTRAINT `fk_mater` FOREIGN KEY (`id_material_didatico`) REFERENCES `material_didatico` (`id`),
  CONSTRAINT `fk_obse` FOREIGN KEY (`id_observacao`) REFERENCES `observacao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `observacao_material`
--

LOCK TABLES `observacao_material` WRITE;
/*!40000 ALTER TABLE `observacao_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `observacao_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `observacao_repografia`
--

DROP TABLE IF EXISTS `observacao_repografia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `observacao_repografia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_observacao` int DEFAULT NULL,
  `id_repografia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_obser` (`id_observacao`),
  KEY `fk_repo` (`id_repografia`),
  CONSTRAINT `fk_obser` FOREIGN KEY (`id_observacao`) REFERENCES `observacao` (`id`),
  CONSTRAINT `fk_repo` FOREIGN KEY (`id_repografia`) REFERENCES `repografia` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `observacao_repografia`
--

LOCK TABLES `observacao_repografia` WRITE;
/*!40000 ALTER TABLE `observacao_repografia` DISABLE KEYS */;
/*!40000 ALTER TABLE `observacao_repografia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES (2,'Maria Oliveira'),(3,'Carlos Souza');
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remessa_conserto`
--

DROP TABLE IF EXISTS `remessa_conserto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remessa_conserto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  `nota_fiscal` int DEFAULT NULL,
  `material_didatico_id` int DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `professor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_remessa_conserto_material` (`material_didatico_id`),
  KEY `fk_remessa_professor_new` (`professor_id`),
  CONSTRAINT `fk_remessa_conserto_material` FOREIGN KEY (`material_didatico_id`) REFERENCES `material_didatico` (`id`),
  CONSTRAINT `fk_remessa_professor_new` FOREIGN KEY (`professor_id`) REFERENCES `professor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remessa_conserto`
--

LOCK TABLES `remessa_conserto` WRITE;
/*!40000 ALTER TABLE `remessa_conserto` DISABLE KEYS */;
INSERT INTO `remessa_conserto` VALUES (1,'2023-03-20',12345,1,10,NULL),(2,'2023-06-10',67890,2,15,NULL),(3,'2023-09-05',54321,3,8,NULL);
/*!40000 ALTER TABLE `remessa_conserto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repografia`
--

DROP TABLE IF EXISTS `repografia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repografia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `professor_id` int DEFAULT NULL,
  `material_didatico_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_repografia_material_didatico` (`material_didatico_id`),
  KEY `fk_repografia_professor` (`professor_id`),
  CONSTRAINT `fk_repografia_material_didatico` FOREIGN KEY (`material_didatico_id`) REFERENCES `material_didatico` (`id`),
  CONSTRAINT `fk_repografia_professor` FOREIGN KEY (`professor_id`) REFERENCES `professor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repografia`
--

LOCK TABLES `repografia` WRITE;
/*!40000 ALTER TABLE `repografia` DISABLE KEYS */;
INSERT INTO `repografia` VALUES (2,'2023-05-15',30,2,2),(3,'2023-07-10',20,3,3);
/*!40000 ALTER TABLE `repografia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solicitacao`
--

DROP TABLE IF EXISTS `solicitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `id_professor` int DEFAULT NULL,
  `id_material_didatico` int DEFAULT NULL,
  `id_turma` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_solicitacao_material` (`id_material_didatico`),
  KEY `fk_id_turma` (`id_turma`),
  KEY `fk_solicitacao_professor_new` (`id_professor`),
  CONSTRAINT `fk_id_turma` FOREIGN KEY (`id_turma`) REFERENCES `turma` (`id`),
  CONSTRAINT `fk_solicitacao_material` FOREIGN KEY (`id_material_didatico`) REFERENCES `material_didatico` (`id`),
  CONSTRAINT `fk_solicitacao_professor_new` FOREIGN KEY (`id_professor`) REFERENCES `professor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitacao`
--

LOCK TABLES `solicitacao` WRITE;
/*!40000 ALTER TABLE `solicitacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turma`
--

DROP TABLE IF EXISTS `turma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turma` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(30) DEFAULT NULL,
  `nome` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turma`
--

LOCK TABLES `turma` WRITE;
/*!40000 ALTER TABLE `turma` DISABLE KEYS */;
INSERT INTO `turma` VALUES (1,'Ensino Médio','Turma A'),(2,'Graduação','Turma de Biologia'),(3,'Ensino Fundamental','Turma de Matemática');
/*!40000 ALTER TABLE `turma` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-22 14:40:54
