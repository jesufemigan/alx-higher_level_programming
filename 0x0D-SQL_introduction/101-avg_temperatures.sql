-- displays the average temperature by city ordered by tmperature
-- mysql -u root -p hbtn_0c_0 < temperature.sql
SELECT city, SUM(value) / COUNT(*) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC
