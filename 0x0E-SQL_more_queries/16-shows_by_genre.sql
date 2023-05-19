-- list all shows and all genre linked to the show
   -- * if no genre display NULL
SELECT s.title, g.name
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS tvg
ON tvg.genre_id = g.id
RIGHT JOIN tv_shows AS s
ON s.id = tvg.show_id
ORDER BY 1, 2;
