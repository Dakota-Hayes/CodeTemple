-- 1. List all customers who live in Texas (use JOINs) (couldnt test because state is not a column anywhere)
select address.state,customer.customer_id from address inner join customer on address.address_id = customer.address_id where address.state is 'Texas';

-- 2. Get all payments above $6.99 with the Customer's Full Name
select customer.customer_id,payment.payment_id,payment.amount from payment inner join customer on payment.customer_id = customer.customer_id where payment.amount > 6.99;

-- 3. Show all customers names who have made payments over $175(use subqueries)
select customer.first_name,customer.last_name from customer where customer_id in (select customer.customer_id from payment inner join customer on payment.customer_id = customer.customer_id where payment.amount > 175.00);

-- 4. List all customers that live in Nepal (use the city table) there is no nepal in the city table
select address.city_id,customer.customer_id from address inner join customer on address.address_id = customer.address_id where address.city_id = (select city.city_id from city where city.city = 'Nepal');

-- 5. Which staff member had the most transactions?
select max(cnt) from (select count(payment.staff_id) cnt from payment group by payment.staff_id order by payment.staff_id desc) as thing;

-- 6. How many movies of each rating are there?
select count(film.film_id),film.rating from film group by film.rating order by film.rating;

-- 7.Show all customers who have made a single payment above $6.99 (Use Subqueries)
select * from customer where customer.customer_id in (select customer.customer_id from customer inner join payment on payment.customer_id = customer.customer_id where payment.amount > 6.99);

-- 8. How many free rentals did our stores give away?
select count(payment.amount) from payment where payment.amount = 0.00;