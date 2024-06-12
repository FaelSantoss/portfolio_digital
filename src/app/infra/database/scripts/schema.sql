-- Active: 1718017191824@@127.0.0.1@3306@fael
CREATE DATABASE IF NOT EXISTS `portifolio`;

USE `portifolio`;

CREATE TABLE IF NOT EXISTS projects (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    technologies VARCHAR(255),
    link VARCHAR(255),
    img VARCHAR(255)
);
INSERT INTO projects (title, content, technologies, link, img)
VALUES ('Smart-Farming',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odit distinctio vero dolorum ipsa quod maxime, minus, earum doloribus laborum nobis unde aliquam sequi incidunt natus beatae dolor debitis iure eius!',
        'javascript,python,flask,html5,css3,tailwindcss,docker,mysql',
        'https://github.com/CtrI-Alt-Del/smart-farming',
        'smartfarming.png'
         );

INSERT INTO projects (title, content, technologies, link, img)
VALUES ('Meu Timão',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odit distinctio vero dolorum ipsa quod maxime, minus, earum doloribus laborum nobis unde aliquam sequi incidunt natus beatae dolor debitis iure eius!',
        'python,flask,html5,css3,bootstrap,docker,mysql',
        'https://github.com/FaelSantoss/challenge2_classPW',
        'meutimao.png'
         );

INSERT INTO projects (title, content, technologies, link, img)
VALUES ('Todo List',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odit distinctio vero dolorum ipsa quod maxime, minus, earum doloribus laborum nobis unde aliquam sequi incidunt natus beatae dolor debitis iure eius!',
         'javascript,html5,css3',
         'https://github.com/FaelSantoss/projeto-todo',
         'todolist.png'
         );

INSERT INTO projects (title, content, technologies, link, img)
VALUES ('Buscador CEP',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Odit distinctio vero dolorum ipsa quod maxime, minus, earum doloribus laborum nobis unde aliquam sequi incidunt natus beatae dolor debitis iure eius!',
        'javascript,react,html5,css3',
        'https://github.com/FaelSantoss/zip-code-finder',
        'zipcodefinder.png'
         );

SELECT * FROM projects;