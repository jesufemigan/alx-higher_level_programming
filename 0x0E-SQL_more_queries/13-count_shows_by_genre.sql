--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT DISTINCT g.name as genre, COUNT(*) as number_of_shows
	FROM tv_genres g 
	RIGHT JOIN tv_show_genres t
	ON g.id = t.genre_id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
