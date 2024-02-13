-- displays the top three cities tempearatures during July and August order by temperature
-- mysql -u root -p hbtn_0c_0 < temperatures.sql
SELECT city, AVG(value) as avg_temp FROM temperatures 
	WHERE (month = 8 OR month = 7)
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
