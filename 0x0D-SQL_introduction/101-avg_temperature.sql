-- Displays the average temprature by city ordered by descending
-- displays the average temp in desc order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
