select c.first_name, c.last_name, c.email, a.address from customer c
join address a
on c.address_id = a.address_id
where a.city_id = 312;

select f.title, f.description, f.release_year, f.rating, f.special_features, c.name as genre from category c
join film_category fc
on c.category_id = fc.category_id
join film f
on fc.film_id = f.film_id
where c.name = "Comedy";

select a.actor_id, a.first_name, a.last_name, f.title, f.description,  f.release_year from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on a.actor_id = fa.actor_id
where fa.actor_id = 5;

select c.first_name, c.last_name, c.email, a.address from customer c
join store s
on s.store_id = c.store_id
join address a
on c.address_id = a.address_id
where a.address_id in (1, 42, 312, 459)
and s.store_id = 1;

select f.title, f.description, f.release_year, f.rating, f.special_features from film f
join film_actor fa
on f.film_id = fa.film_id
where fa.actor_id = 15
and f.rating = "G"
and f.special_features like "%Behind the Scenes%";

select f.film_id, f.title, a.actor_id, a.first_name, a.last_name from actor a
join film_actor fa
on a.actor_id = fa.actor_id
join film f
on f.film_id = fa.film_id
where f.film_id = 369;

select f.title, f.description, f.release_year, f.rating, f.special_features, c.name as genre from film_category fc
join category c
on fc.category_id = c.category_id
join film f
on f.film_id = fc.film_id
where c.name = "Drama"
and f.rental_rate = 2.99;

select f.title, f.description, f.release_year, f.rating, f.special_features, c.name as genre, a.first_name, a.last_name from film_category fc
join category c
on fc.category_id = c.category_id
join film f
on fc.film_id = f.film_id
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id
where c.name = "Action"
and a.first_name = "SANDRA"
and a.last_name = "KILMER";