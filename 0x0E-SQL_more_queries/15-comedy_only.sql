-- list shows in the Comedy genre
SELECT s.title
FROM tv_shows AS s
JOIN tv_show_genres AS tvg
ON tvg.show_id = s.id
JOIN tv_genres AS g
ON g.id = tvg.genre_id
WHERE g.name = 'Comedy'
ORDER BY 1;
