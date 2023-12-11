-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tg.name
FROM tv_genres AS tg
WHERE tg.name NOT IN 
(
    SELECT tg.name
    FROM tv_genres AS tg
    LEFT JOIN tv_show_genres AS tsg
    ON tg.id = tsg.genre_id
    LEFT JOIN tv_shows AS ts
    ON ts.id = tsg.show_id
    WHERE ts.title = "Dexter"
)
ORDER BY tg.name ASC;