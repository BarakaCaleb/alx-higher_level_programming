-- lists all genres and the number of shows linked to each
SELECT tg.name AS genre, COUNT(ts.genre_id) AS number_of_shows
FROM tv_genres tg
INNER JOIN tv_show_genres ts ON tg.id = ts.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
