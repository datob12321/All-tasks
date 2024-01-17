CREATE SCHEMA football; 

CREATE table national_teams (
	teamID int primary key auto_increment not null,
    team_name varchar(50) not null,
    world_cups int not null,
    continent_cups int not null
);

CREATE table clubs (
	clubID int primary key auto_increment not null,
    club_name varchar(50) not null,
    ucl_cups int,
    inner_championship int
);

CREATE table footballers (
	footballerID int primary key auto_increment not null,
	firstname varchar(50) not null,
    lastname varchar(50) not null,
    birth_date date not null,
    clubID int,
    teamID int,
    foreign key (clubID) references clubs (clubID),
    foreign key (teamID) references national_teams (teamID)
);


INSERT INTO clubs (club_name, ucl_cups, inner_championship) VALUES 
('Barcelona', 5, 27),
('Real Madrid', 14, 35),
('Manchester City', 1, 7),
('Napoli', 0, 3),
('Bayern Munich', 6, 33),
('Inter Maimi', 0, 0 ),
('Al Nassr', 0, 9);

INSERT INTO national_teams (team_name, world_cups, continent_cups) VALUES 
('Argentina', 3, 15),
('Brazil', 5, 9),
('Spain', 1, 3),
('Italy', 4, 2),
('France', 2, 2),
('Germany', 4, 3),
('Uruguay',  2, 15),
('Portugal', 0, 1),
('Georgia', 0 , 0),
('Norway', 0, 0),
('Croatia', 0, 0);


INSERT INTO footballers (firstname, lastname, birth_date, clubID, teamID) VALUES 
('Khvicha', 'Kvaratskhelia', '2001-02-12', 4, 18),
('Pedro', 'Gavi', '2004-08-05', 1, 12),
('Luka', 'Modric', '1985-09-09', 2, 20),
('Julian', 'Alvarez', '2000-01-31', 3, 10),
('Lionel', 'Messi', '1987-06-24', 6, 10),
('Cristiano', 'Ronaldo', '1985-02-05', 7, 17),
('Erling', 'Haaland', '2000-07-21', 3, 19),
('Federico', 'Valverde', '1998-06-22', 2, 16);

CREATE view playerInfo AS 
SELECT f.firstname, f.lastname, f.birth_date, c.club_name, n.team_name 
FROM footballers f 
JOIN clubs c ON f.clubID=c.clubID
JOIN national_teams n ON f.teamID=n.teamID;

SELECT firstname, lastname, club_name, team_name FROM playerinfo;


