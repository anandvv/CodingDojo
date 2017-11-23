select c.name, l.percentage from countries c
join languages l 
on c.id = l.country_id
where l.language = "Slovene"
order by l.percentage DESC;

select co.name, count(ci.name) from cities ci
join countries co
on ci.country_id = co.id
group by co.name
order by count(ci.name) DESC;

select ci.name, ci.population from cities ci
join countries co
on ci.country_id = co.id
where co.name = "Mexico"
and ci.population > 50000
order by ci.population DESC;

select l.language, co.name, l.percentage from languages l
join countries co
on l.country_id = co.id
where l.percentage > 89
order by l.percentage DESC;

select * from countries
where surface_area < 501
and population > 100000;

select * from countries c
where government_form = "Constitutional Monarchy"
and capital > 200
and life_expectancy > 75;

select co.name, ci.name, ci.district, ci.population from cities ci
join countries co
on co.name = "Argentina"
where ci.district = "Buenos Aires"
and ci.population > 500000;

select co.region, count(name) from countries co
group by co.region
order by count(name) desc;








