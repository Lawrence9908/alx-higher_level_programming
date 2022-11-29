-- Lists all records of second table where name is not null.
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
