-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT ts.title
FROM tv_shows AS ts
WHERE ts.title NOT IN 
(
    SELECT ts.title
    FROM tv_shows AS ts
    INNER JOIN tv_show_genres AS tsg
    ON ts.id = tsg.show_id
    INNER JOIN tv_genres AS tg
    ON tg.id = tsg.genre_id
    WHERE tg.name = "Comedy"
)
GROUP BY ts.title
ORDER BY ts.title ASC;
