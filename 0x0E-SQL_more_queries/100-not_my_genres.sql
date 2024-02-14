-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name FROM tv_genres g
where g.name NOT IN
(SELECT g.name FROM tv_genres g
	LEFT JOIN tv_show_genres t
		ON g.id = t.genre_id
	LEFT JOIN tv_shows s
		ON s.id = t.show_id
	WHERE title = "Dexter")
ORDER BY g.name;

