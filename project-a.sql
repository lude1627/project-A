<<<<<<< HEAD:project-a .sql
-- Base de datos: project-a
-- Limpieza inicial (seguridad: elimina tablas si ya existen)
DROP TABLE IF EXISTS `carrito`;
DROP TABLE IF EXISTS `productos`;
DROP TABLE IF EXISTS `categorias`;
DROP TABLE IF EXISTS `usuario`;

-- --------------------------------------------------------
-- Tabla: categorias
-- --------------------------------------------------------
CREATE TABLE `categorias` (
  `Cat_id` INT(11) NOT NULL AUTO_INCREMENT,
  `Cat_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Cat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
=======
-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-08-2025 a las 15:17:59
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `Cat_id` int(11) NOT NULL,
  `Cat_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `categorias`
--
>>>>>>> d2a49498c6f85a53a24e1bc92c86479066f371a7:project-a.sql

INSERT INTO `categorias` (`Cat_id`, `Cat_name`) VALUES
(1, 'Comida'),
(2, 'Aseo'),
(3, 'Utensilios de cocina');

-- --------------------------------------------------------
-- Tabla: productos
-- --------------------------------------------------------
CREATE TABLE `productos` (
<<<<<<< HEAD:project-a .sql
  `Product_id` INT(11) NOT NULL AUTO_INCREMENT,
  `Product_name` VARCHAR(100) NOT NULL,
  `Product_description` VARCHAR(255) NOT NULL,
  `Cat_id` INT(11) NOT NULL,
  `Product_cant` INT(11) NOT NULL DEFAULT 0,
  `Product_price` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`Product_id`),
  KEY `fk_productos_categoria` (`Cat_id`),
  CONSTRAINT `fk_productos_categoria` FOREIGN KEY (`Cat_id`) REFERENCES `categorias` (`Cat_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `productos` (`Product_id`, `Product_name`, `Product_description`, `Cat_id`, `Product_cant`, `Product_price`) VALUES
(13, 'Sachipapa', 'Comida rápida', 1, 27, 10000.00);
=======
  `Product_id` int(11) NOT NULL,
  `Product_name` varchar(60) NOT NULL,
  `Product_description` varchar(100) NOT NULL,
  `Cat_id` int(11) NOT NULL,
  `Product_cant` int(11) NOT NULL,
  `Product_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`Product_id`, `Product_name`, `Product_description`, `Cat_id`, `Product_cant`, `Product_price`) VALUES
(13, 'Sachipapa', 'comida rapida', 1, 27, 10000);
>>>>>>> d2a49498c6f85a53a24e1bc92c86479066f371a7:project-a.sql

-- --------------------------------------------------------
-- Tabla: usuario
-- --------------------------------------------------------
CREATE TABLE `usuario` (
<<<<<<< HEAD:project-a .sql
  `User_id` INT(11) NOT NULL AUTO_INCREMENT,
  `User_name` VARCHAR(100) NOT NULL,
  `User_phone` VARCHAR(15) NOT NULL,
  `User_mail` VARCHAR(100) NOT NULL UNIQUE,
  `User_password` VARCHAR(255) NOT NULL COMMENT 'Contraseña en hash (bcrypt/argon2)',
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Tabla de usuarios';
=======
  `User_id` int(15) NOT NULL,
  `User_name` varchar(100) NOT NULL,
  `User_phone` int(15) NOT NULL,
  `User_mail` varchar(60) NOT NULL,
  `User_password` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci COMMENT='tabla registro de usuario';
>>>>>>> d2a49498c6f85a53a24e1bc92c86479066f371a7:project-a.sql

INSERT INTO `usuario` (`User_name`, `User_phone`, `User_mail`, `User_password`) VALUES
('luis felipe', '302401912', 'lfdelahozfontalvo@gmail.com', 'hashed_password_aqui');

<<<<<<< HEAD:project-a .sql
-- --------------------------------------------------------
-- Tabla: carrito
-- --------------------------------------------------------
CREATE TABLE `carrito` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `User_id` INT(11) NOT NULL,
  `Product_id` INT(11) NOT NULL,
  `cantidad` INT(11) NOT NULL DEFAULT 1,
  `precio_unitario` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_carrito_usuario` (`User_id`),
  KEY `fk_carrito_producto` (`Product_id`),
  CONSTRAINT `fk_carrito_usuario` FOREIGN KEY (`User_id`) REFERENCES `usuario` (`User_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_carrito_producto` FOREIGN KEY (`Product_id`) REFERENCES `productos` (`Product_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
=======
INSERT INTO `usuario` (`User_id`, `User_name`, `User_phone`, `User_mail`, `User_password`) VALUES
(103429967, 'luis felipe', 302401912, 'lfdelahozfontalvo@gmail.com', 1627);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`Cat_id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`Product_id`),
  ADD KEY `fk_productos_categoria` (`Cat_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`User_id`),
  ADD UNIQUE KEY `User_id_UNIQUE` (`User_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `Cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `Product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_productos_categoria` FOREIGN KEY (`Cat_id`) REFERENCES `categorias` (`Cat_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
>>>>>>> d2a49498c6f85a53a24e1bc92c86479066f371a7:project-a.sql
