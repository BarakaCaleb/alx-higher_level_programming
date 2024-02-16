-- list all shows contained in the DATABASE
SELECT t.title, ts.genre_id
FROM tv_shows t 
LEFT JOIN tv_show_genres ts ON t.id = ts.show_id
ORDER BY t.title ASC, ts.genre_id ASC;
