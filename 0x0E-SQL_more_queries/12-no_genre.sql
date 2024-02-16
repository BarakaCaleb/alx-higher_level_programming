-- lists all shows without a genre linked
SELECT t.title, ts.genre_id
FROM tv_shows t 
LEFT JOIN tv_show_genres ts ON t.id = ts.show_id
WHERE ts.genre_id IS NULL
ORDER BY t.title ASC, ts.genre_id ASC;
