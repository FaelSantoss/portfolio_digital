-- Active: 1716055461921@@127.0.0.1@3306@fael
CREATE DATABASE IF NOT EXISTS `bla`;
CREATE TABLE IF NOT EXISTS personal_project (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    technologies VARCHAR(255),
    link VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS academic_project (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    technologies VARCHAR(255),
    link VARCHAR(255)
);

INSERT INTO personal_project (title, content, technologies, link)
VALUES ('Projeto Todo List',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odit distinctio vero dolorum ipsa quod maxime, minus, earum doloribus laborum nobis unde aliquam sequi incidunt natus beatae dolor debitis iure eius!',
         'HTML, CSS, JavaScript',
         'https://github.com/FaelSantoss/projeto-todo'
         );

INSERT INTO personal_project (title, content, technologies, link)
VALUES ('ZipCode Finder',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odit distinctio vero dolorum ipsa quod maxime, minus, earum doloribus laborum nobis unde aliquam sequi incidunt natus beatae dolor debitis iure eius!',
         'HTML, CSS, JavaScript, React',
         'https://github.com/FaelSantoss/zip-code-finder'
         );

SELECT * FROM personal_project;