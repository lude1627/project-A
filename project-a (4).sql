-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-08-2025 a las 18:55:23
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `project-a`
--
CREATE DATABASE IF NOT EXISTS `project-a` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `project-a`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

DROP TABLE IF EXISTS `carrito`;
CREATE TABLE IF NOT EXISTS `carrito` (
  `Car_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `Car_Cantidad` int(11) NOT NULL DEFAULT 1,
  `Car_subTotal` float NOT NULL,
  PRIMARY KEY (`Car_id`),
  KEY `fk_carrito_usuario` (`User_id`),
  KEY `fk_carrito_producto` (`Product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`Car_id`, `User_id`, `Product_id`, `Car_Cantidad`, `Car_subTotal`) VALUES
(2, 123, 14, 3, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

DROP TABLE IF EXISTS `categorias`;
CREATE TABLE IF NOT EXISTS `categorias` (
  `Cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `Cat_name` varchar(100) NOT NULL,
  PRIMARY KEY (`Cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1238 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`Cat_id`, `Cat_name`) VALUES
(1, 'Comida'),
(2, 'Aseo'),
(3, 'Utensilios de cocina'),
(1237, 'df');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `Product_id` int(11) NOT NULL AUTO_INCREMENT,
  `Product_name` varchar(100) NOT NULL,
  `Product_description` varchar(255) NOT NULL,
  `Cat_id` int(11) NOT NULL,
  `Product_cant` int(11) NOT NULL DEFAULT 0,
  `Product_price` float NOT NULL,
  PRIMARY KEY (`Product_id`),
  KEY `fk_productos_categoria` (`Cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`Product_id`, `Product_name`, `Product_description`, `Cat_id`, `Product_cant`, `Product_price`) VALUES
(14, 'sachipapa', 'dgsdsgsdgsdg', 1, 15, 10000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(100) NOT NULL,
  `User_phone` varchar(15) NOT NULL,
  `User_mail` varchar(100) NOT NULL,
  `User_password` varchar(255) NOT NULL COMMENT 'Contraseña en hash (bcrypt/argon2)',
  PRIMARY KEY (`User_id`),
  UNIQUE KEY `User_mail` (`User_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=1034299688 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Tabla de usuarios';

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`User_id`, `User_name`, `User_phone`, `User_mail`, `User_password`) VALUES
(123, 'lude', '213214241', 'lfdelahozfontalvo@gmail.com', '123456');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `fk_carrito_producto` FOREIGN KEY (`Product_id`) REFERENCES `productos` (`Product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_carrito_usuario` FOREIGN KEY (`User_id`) REFERENCES `usuario` (`User_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_productos_categoria` FOREIGN KEY (`Cat_id`) REFERENCES `categorias` (`Cat_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
