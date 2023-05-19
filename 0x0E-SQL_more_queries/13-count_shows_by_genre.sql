-- list and count the number of shows in each genre
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres tvg
ON tvg.genre_id = g.id
JOIN tv_shows AS s
ON s.id = tvg.show_id
GROUP BY genre
ORDER BY 2 DESC;
