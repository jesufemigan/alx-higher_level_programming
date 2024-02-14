--  lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) AS rating FROM tv_genres g
LEFT JOIN tv_show_genres t
ON g.id = t.genre_id
LEFT JOIN tv_shows s
ON s.id = t.show_id
LEFT JOIN tv_show_ratings r
ON s.id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
