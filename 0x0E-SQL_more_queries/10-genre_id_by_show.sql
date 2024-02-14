-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT t.title, g.genre_id FROM
	tv_shows t LEFT JOIN
	tv_show_genres g
	ON t.id = g.show_id
	WHERE g.genre_id IS NOT NULL
	ORDER BY t.title, g.genre_id;
