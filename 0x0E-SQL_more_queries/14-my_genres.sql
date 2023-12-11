-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY tg.name ASC;
