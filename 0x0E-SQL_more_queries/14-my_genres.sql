-- list all the genre of the show 'Dexter' sorted by genre name
SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS tvg
ON tvg.genre_id = g.id
JOIN tv_shows AS s
ON s.id = tvg.show_id
WHERE s.title = 'Dexter'
ORDER BY 1;
