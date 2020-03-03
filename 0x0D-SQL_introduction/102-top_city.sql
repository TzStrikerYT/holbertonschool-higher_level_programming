-- top 3 cities temp july and aug
SELECT city, AVG(value) AS avge_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
