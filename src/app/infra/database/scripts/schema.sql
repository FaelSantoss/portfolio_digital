-- Active: 1716055461921@@127.0.0.1@3306@bla
CREATE DATABASE IF NOT EXISTS `bla`;
CREATE TABLE IF NOT EXISTS personal_project (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    technologies VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS academic_project (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    technologies VARCHAR(255)
);

INSERT INTO personal_project (title, content, technologies)
VALUES ('Projeto Exemplo 1', 'Este é o conteúdo do projeto exemplo 1.', 'HTML, CSS, JavaScript');

INSERT INTO personal_project (title, content, technologies)
VALUES ('Projeto Exemplo 2', 'Este é o conteúdo do projeto exemplo 2.', 'Python, Django');
