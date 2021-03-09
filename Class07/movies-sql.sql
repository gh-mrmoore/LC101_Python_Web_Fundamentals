SELECT * FROM launchcode.movies;

#SELECT * FROM launchcode.movies ORDER BY year DESC;

#INSERT INTO launchcode.movies (title, year, director_id)
#VALUES ('Amelie', 2001, 5)

#SELECT title, country FROM movies LEFT JOIN directors ON movies.director_id = directors.director_id WHERE title = 'Amelie';

#SELECT title, first_name, last_name FROM movies LEFT JOIN directors ON movies.director_id = directors.director_id ORDER BY last_name ASC;