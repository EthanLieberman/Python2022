SELECT * FROM countries;

SELECT name, languages.language, Percentage FROM countries
JOIN languages ON languages.Country_Code = countries.Code
WHERE languages.language = 'Slovene' ORDER BY Percentage DESC;


SELECT countries.name, COUNT(cities.name) AS citycount
FROM countries JOIN cities ON countries.code = cities.country_code
GROUP BY countries.name ORDER BY citycount DESC;


SELECT cities.name, cities.population, countries.id
FROM cities JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'mexico' AND cities.population > 500000 ORDER BY cities.population DESC;


SELECT countries.name, languages.language, languages.percentage
FROM countries JOIN languages ON countries.code = languages.country_code
WHERE languages.percentage > 89 ORDER BY languages.percentage DESC;


SELECT countries.name, countries.surface_area, cities.population, countries.population
FROM countries JOIN cities ON countries.id = cities.country_id
WHERE countries.surface_area < 501 AND countries.population > 100000;


SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE capital > 200 AND life_expectancy > 75 AND government_form = 'Constitutional Monarchy';


SELECT countries.name, cities.name, cities.district, cities.population
FROM countries JOIN cities ON countries.code = cities.country_code
WHERE cities.district = 'Buenos Aires' AND cities.population > 500000;

SELECT region, COUNT(name) AS countries
FROM countries
GROUP BY region ORDER BY countries DESC;