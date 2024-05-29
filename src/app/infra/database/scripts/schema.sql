CREATE DATABASE IF NOT EXISTS `bla`;

CREATE TABLE IF NOT EXISTS personal_project (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    desc VARCHAR(255),
    technologies VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS academic_project (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    desc VARCHAR(255),
    technologies VARCHAR(255)
);