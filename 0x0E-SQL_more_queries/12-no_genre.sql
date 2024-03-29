-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT t.title, g.genre_id FROM tv_shows t
	LEFT JOIN tv_show_genres g
	ON t.id = g.show_id
	WHERE genre_id IS NULL
	ORDER BY t.title, g.genre_id
