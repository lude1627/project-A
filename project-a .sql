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

INSERT INTO `categorias` (`Cat_id`, `Cat_name`) VALUES
(1, 'Comida'),
(2, 'Aseo'),
(3, 'Utensilios de cocina');

-- --------------------------------------------------------
-- Tabla: productos
-- --------------------------------------------------------
CREATE TABLE `productos` (
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

-- --------------------------------------------------------
-- Tabla: usuario
-- --------------------------------------------------------
CREATE TABLE `usuario` (
  `User_id` INT(11) NOT NULL AUTO_INCREMENT,
  `User_name` VARCHAR(100) NOT NULL,
  `User_phone` VARCHAR(15) NOT NULL,
  `User_mail` VARCHAR(100) NOT NULL UNIQUE,
  `User_password` VARCHAR(255) NOT NULL COMMENT 'Contraseña en hash (bcrypt/argon2)',
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Tabla de usuarios';

INSERT INTO `usuario` (`User_name`, `User_phone`, `User_mail`, `User_password`) VALUES
('luis felipe', '302401912', 'lfdelahozfontalvo@gmail.com', 'hashed_password_aqui');

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
