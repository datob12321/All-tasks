CREATE DATABASE music;

CREATE TABLE music.artists (
	artistID int primary key auto_increment not null,
	firstname varchar(50) not null,
    lastname varchar(50),
    birth_date date,
    country varchar(50),
    monthly_listeners int
);


CREATE TABLE music.songs (
	songID int primary key auto_increment not null,
	name varchar(50) not null,
    language varchar(50) not null,
    release_date int,
    genre varchar(50),
    youtube_likes int,
    artistID int,
    foreign key (artistID) references music.artists (artistID)
);



INSERT INTO music.artists (firstname, lastname, birth_date, country, monthly_listeners) VALUES
('Paulo', 'Londra', '1998-04-12', 'Argentina', 14000000),
('Daddy Yankee', NULL, '1972-03-10', 'Puerto Rico', 49000000),
('Carlos', 'Vives', '1961-08-07', 'Colombia', 14000000),
('Jose', 'Balvin', '1985-05-07', 'Colombia', 50000000),
('Maluma', NULL, '1994-01-28', 'Colombia', 43000000),
('Enrique', 'Iglesias', '1975-03-08', 'Spain', 25800000),
('Marc', 'Anthony', '1968-09-16', 'USA', 11500000);

INSERT INTO music.songs (name, language, release_date, genre, youtube_likes, artistID) VALUES
('Adan y Eva', 'Spanish', 2019, 'Latino Urbano', 7200000, 8),
('Que tengo que hacer', 'Spanish', 2008, 'Reggaeton', 650000, 9),
('Ella es mi fiesta', 'Spanish', 2014, 'Salsa', 180000, 10),
('Ay vamos', 'Spanish', 2014, 'Reggaeton', 5500000, 11),
('Perecta', 'Spanish', 2021, 'Latino Urbano', 530000, 12),
('El perdon', 'Spanish', 2017, 'Latino Pop', 4100000, 13),
('Tu vida en la mia', 'Spanish', 2019, 'Salsa', 540000, 14);

UPDATE music.songs SET youtube_likes=youtube_likes+1000;

UPDATE music.artists SET monthly_listeners=monthly_listeners+2000;

INSERT INTO music.songs (name, language, release_date, genre, youtube_likes, artistID) VALUES
('Nena maldicion', 'Spanish', 2019, 'Latino Urbano', 6700000, 8),
('Hawai', 'Spanish', 2020, 'Latino Pop', 5900000, 12),
('Tu principe', 'Spanish', 2004, 'Reggaeton', 412000, 9),
('La Gota Fria', 'Spanish', 1993, 'Tropipop', 286000, 10);

SELECT * FROM music.songs;

DELETE FROM music.songs WHERE name LIKE 'H%' OR genre='Tropipop';

CREATE VIEW music.reggaetons AS 
SELECT s.songID, s.name, s.language, s.genre, a.artistID, a.firstname, a.lastname, a.country 
FROM music.songs s JOIN music.artists a ON s.artistID=a.artistID 
WHERE genre='Reggaeton';

SELECT name, language, country, firstname, lastname FROM music.reggaetons;

