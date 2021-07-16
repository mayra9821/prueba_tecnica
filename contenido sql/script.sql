-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Registros_especies
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Registros_especies` ;

-- -----------------------------------------------------
-- Schema Registros_especies
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Registros_especies` DEFAULT CHARACTER SET utf8 ;
USE `Registros_especies` ;

-- -----------------------------------------------------
-- Table `Registros_especies`.`Proyectos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Registros_especies`.`Proyectos` ;

CREATE TABLE IF NOT EXISTS `Registros_especies`.`Proyectos` (
  `idProyecto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idProyecto`),
  UNIQUE INDEX `idProyecto_UNIQUE` (`idProyecto` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Registros_especies`.`Ecorregion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Registros_especies`.`Ecorregion` ;

CREATE TABLE IF NOT EXISTS `Registros_especies`.`Ecorregion` (
  `idEcorregion` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idEcorregion`),
  UNIQUE INDEX `idEcorregion_UNIQUE` (`idEcorregion` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Registros_especies`.`registro_bio_especies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Registros_especies`.`registro_bio_especies` ;

CREATE TABLE IF NOT EXISTS `Registros_especies`.`registro_bio_especies` (
  `identificador` INT NOT NULL AUTO_INCREMENT,
  `especie` VARCHAR(45) NULL,
  `familia` VARCHAR(45) NULL,
  `nombre_comun` VARCHAR(45) NULL,
  `proyecto` INT NULL,
  `base_registro` VARCHAR(45) NULL,
  `anio_identificacion` YEAR(4) NULL,
  `departamento` VARCHAR(45) NULL,
  `municipio` VARCHAR(45) NULL,
  `localidad` VARCHAR(45) NULL,
  `latitud` FLOAT NULL,
  `longitud` FLOAT NULL,
  `autor` VARCHAR(45) NULL,
  `fecha_captura` DATE NULL,
  `ecorregion` INT NULL,
  PRIMARY KEY (`identificador`),
  UNIQUE INDEX `idregistro_bio_especies_UNIQUE` (`identificador` ASC),
  INDEX `idProyecto_idx` (`proyecto` ASC) ,
  INDEX `idEcorregion_idx` (`ecorregion` ASC),
  CONSTRAINT `proyecto`
    FOREIGN KEY (`proyecto`)
    REFERENCES `Registros_especies`.`Proyectos` (`idProyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ecorregion`
    FOREIGN KEY (`ecorregion`)
    REFERENCES `Registros_especies`.`Ecorregion` (`idEcorregion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
