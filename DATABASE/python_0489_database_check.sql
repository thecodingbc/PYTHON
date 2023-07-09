-- We can learn 2 points in this sql script:

-- Point 1) check usage --------------------------------------
-- check helps us add more complex constraints in table data
-- there are 2 kinds of check
-- 1) column check, which you put after the column definition
-- 2) table check, which you put parallel with the column definition


-- Point 2) insert multiple rows in 1 single insert sql ------
-- you can add mulitple rows, separated by comma in 1 single insert sql.

drop table if exists schools;

create table schools (
 id integer primary key,
 name text not null,
 grade text check(grade in ('Primary', 'Secondary', 'Junior college', 'Polytechnic', 'University')), -- column check
 location text,
 postalcode text not null check(postalcode like 'S______'), -- column check
 students integer not null,

 check(length(name) >= 5 and students > 300) -- table check
);


insert into schools values
(1, 'School A', 'Primary', 'Tampines', 'S123456', 582),
(2, 'School B', 'Secondary', 'Bishan', 'S284621', 1278);


insert into schools (name, grade, location, postalcode, students) values
('School C', 'Primary', 'Jurong East', 'S373452', 856),
('School D', 'University', 'Clementi', 'S728937', 20843),
('School E', 'Polytechnic', 'Bukit Timah', 'S217382', 8912);


insert into schools (name, grade, postalcode, students) values
('School F', 'Junior college', 'S271373', 2945),
('School G', 'Secondary', 'S728341',  359),
('School H', 'Junior college', 'S348791', 2547);

select * from schools;



update schools set students = students + 100 where grade = 'Secondary';
update schools set students = students - 100 where grade = 'Primary';

select * from schools;



delete from schools where students < 500;

select * from schools;
