-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: kosoylebed
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `meals`
--

DROP TABLE IF EXISTS `meals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meals` (
  `id` int NOT NULL,
  `name` text,
  `image` text,
  `description` text,
  `fullDescription` text,
  `totalWeight` int DEFAULT NULL,
  `calories` int DEFAULT NULL,
  `mealTime` text,
  `containsMeat` tinyint(1) DEFAULT NULL,
  `seafood` tinyint(1) DEFAULT NULL,
  `healthy` tinyint(1) DEFAULT NULL,
  `drink` tinyint(1) DEFAULT NULL,
  `difficulty` text,
  `mealRecipe` text,
  `recipeSteps` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meals`
--

LOCK TABLES `meals` WRITE;
/*!40000 ALTER TABLE `meals` DISABLE KEYS */;
INSERT INTO `meals` VALUES (0,'Фруктовый салат','0000000.jpg','Свежий салат с яблоками, бананами, апельсинами и грушами.','Фруктовый салат: свежий и простой способ получить порцию витаминов и освежающей энергии. Сочные яблоки, бананы, апельсины и груши сочетаются в легкое угощение, приносящее пользу вашему здоровью. Идеально подходит в качестве быстрого и питательного перекуса в любое время дня!',450,200,'утро вечер',0,0,1,0,'Легкий','яблоки 200/ бананы 100/ апельсины 100/ груши 50','Яблоки помойте, обсушите и удалите сердцевину. Можно оставить кожуру, если она хорошо вымыта._000000000.jpg/ Бананы очистите от кожуры и нарежьте кружочками или дольками._000000001/ Апельсины очистите от кожуры и белой части, разделите на дольки._000000002/ Груши помойте, обсушите и нарежьте кубиками._000000003/ В большой миске аккуратно смешайте все нарезанные фрукты._000000004/ По желанию можно добавить сок лимона или апельсина для сохранения свежести фруктов._000000005/ Если вы предпочитаете сладкий вкус, можно добавить немного меда или кленового сиропа._000000006/ Фруктовый салат хорошо дополняется орехами или ягодами._000000007/ Можно посыпать сверху небольшим количеством мяты или базилика для аромата._000000008/ Распределите фруктовый салат по порционным тарелкам и подавайте._000000009'),(1,'Салат Цезарь','0000001.jpg','Классический салат Цезарь с курицей, сыром Пармезан и хрустящими крутонами.','Салат Цезарь - классическое блюдо с историей, которое любят многие. Он сочетает в себе сочный листовой салат, ароматную заправку, нежное куриное мясо, сыр Пармезан и хрустящие крутоны. Этот салат насыщен вкусом и текстурой, что делает его прекрасным выбором как для легкого обеда, так и для ужина.',350,350,'обед',1,0,0,0,'Средний','Салатный лист 150/ куриное филе 150/ сыр Пармезан 50/ хлеб 50/ чеснок 1 зубчик/ яйцо 1 шт./ оливковое масло 2 ст.л./ лимонный сок 2 ст.л./ горчица 1 ч.л./ ворчестерский соус 1 ч.л./ соль и перец по вкусу','Приготовьте куриное филе, обжарив его на сковороде с солью и перцем._000000100.jpg/ Обжарьте крутоны: нарежьте хлеб на кубики, обмажьте оливковым маслом, посыпьте измельченным чесноком, посолите и поперчите, затем запеките в духовке до золотистости._000000101/ Приготовьте заправку: в миске смешайте лимонный сок, оливковое масло, ворчестерский соус, измельченный чеснок, горчицу, соль и перец._000000102/ Отварите яйцо вкрутую, остудите и порежьте кружочками._000000103/ На большой тарелке уложите листовой салат, выложите нарезанное куриное филе, крутоны, сыр Пармезан и кружочки яйца._000000104/ Полейте салат заправкой и аккуратно перемешайте._000000105/ Подавайте сразу после приготовления, чтобы сохранить хрустящесть крутонов._000000106 ');
/*!40000 ALTER TABLE `meals` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-31 12:55:36
