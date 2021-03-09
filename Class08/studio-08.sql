/* Studio #1 */
SELECT DISTINCT country FROM `directors`

/* Studio #2 */
SELECT first, last FROM directors WHERE country = 'France'

/* Studio #3 */
SELECT MIN(date_viewed) FROM viewings

/* Studio #4 */
SELECT movies.title, directors.country FROM movies 
LEFT JOIN directors ON movies.director_id = directors.director_id
WHERE directors.country = 'USA';

/* Studio #5 */
SELECT movies.title, directors.first, directors.last FROM movies 
LEFT JOIN directors ON movies.director_id = directors.director_id
WHERE directors.first = 'Akira' AND directors.last = 'Kurosawa';

/* Studio #6 */
SELECT COUNT(date_viewed) FROM viewings
LEFT JOIN movies ON movies.director_id = viewings.movie_id
WHERE movies.title = "Talk to Me";

/* Studio #7 */
SELECT MAX(date_viewed) FROM viewings;

/* Studio #8 */
SELECT movies.movie_id FROM movies
LEFT JOIN viewings on movies.movie_id = viewings.movie_id
WHERE viewings.date_viewed = (SELECT MAX(date_viewed) FROM viewings)

/* ___OR___ */

SELECT viewings.movie_id FROM viewings
WHERE viewings.date_viewed = (SELECT MAX(date_viewed) FROM viewings)

/* Studio #9 */
SELECT movies.title FROM movies
LEFT JOIN viewings on movies.movie_id = viewings.movie_id
WHERE viewings.date_viewed = (SELECT MIN(date_viewed) FROM viewings)

/* Studio #10 */
SELECT viewers.first, viewers.last FROM viewers
LEFT JOIN viewings ON viewers.viewer_id = viewings.viewer_id
WHERE viewings.date_viewed = (SELECT MAX(date_viewed) FROM viewings)

/* Studio #11 */
SELECT movie_id, COUNT(viewings.viewing_id) FROM viewings
WHERE movie_id IN (SELECT DISTINCT viewings.movie_id FROM viewings)
GROUP BY movie_id

/* Studio #12 */
SELECT email FROM viewers
WHERE viewer_id IN
(
SELECT viewings.viewer_id FROM viewings
WHERE viewings.movie_id = (SELECT movies.movie_id FROM movies WHERE movies.title = "Talk to Me")
)
ORDER BY email;

/* Studio #13 */

SELECT email, CONCAT(first, ' ', last) FROM viewers
WHERE viewers.viewer_id IN
(
SELECT viewings.viewer_id FROM viewings
WHERE viewings.movie_id IN
(
SELECT DISTINCT movies.movie_id FROM movies
WHERE director_id = (SELECT director_id FROM directors WHERE directors.first = 'Akira' AND directors.last = 'Kurosawa')
)
);