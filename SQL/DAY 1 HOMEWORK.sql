-- 1. How many actors are there with the last name 'wahlberg'? 2
select count(LAST_NAME) from ACTOR where LAST_NAME like 'Wahlberg';

-- 2. How many payments were made between $3.99 and $5.99? 0
select count(AMOUNT) from PAYMENT where AMOUNT > 3.99 and AMOUNT < 5.99;

-- 3. What fiLm does the store have the most of? 8 COPIES OF MOVIES: 434,835,69,356,174,200,86,738,266,418,341,683,873,767,621,1000,559,109,531,331,973,893,846,572,745,586,206,702,489,301,697,295,378,358,382,412,444,468,730,220,500,91,73,193,231,1,103,525,361,239,789,880,911,403,127,773,595,638,945,753,350,870,609,460,199,369,748,764,897,31,849,856
select COUNT(FILM_ID),FILM_ID from INVENTORY group by FILM_ID order by COUNT(FILM_ID) desc;

-- 4. HOW MANY CUSTOMERS HAVE THE LAST NAME 'WILLIAM'? 0
select COUNT(LAST_NAME) from CUSTOMERS where LAST_NAME like 'William';

-- 5. WHAT STORE EMPLOYEE SOLD THE MOST  RENTALS? 1 AT 8040
select COUNT(STAFF_ID),STAFF_ID from rental group by STAFF_ID order by COUNT(STAFF_ID) DESC;

-- 6. HOW MANY DIFFERENT DISTRICT NAMES ARE THERE? Directory doesnt exist, cant test
select COUNT(distinct(DISTRICT)) from city;

-- 7. WHAT FILM HAS THE MOST ACTORS IN IT? 508 AT 15
select COUNT(FILM_ID),FILM_ID  from film_actor group by FILM_ID order by COUNT(FILM_ID) desc;

-- 9. HOW MANY PAYMENT AMOUNTS 4.99,5.99,ETC HAD A NUMBER OF RENTALS ABOVE 250 CUSTOMERS WITH IDS BETWEEN 380 AND 430? Directory doesnt exist, cantt test
select count(distinct(PAYMENT_AMOUNTS)),count(distinct(rental_id) rental_count from RENTALS where rental_count > 250 and customer_id > 380 and customer_id < 430;

-- 10. WITHIN THE FILM TABLE, HOW MANY RATING CATEGORIES ARE THERE? AND WHAT RATING HAS THE MOST MOVIES TOTAL? 5 TOTAL RATINGS AND PG-13 HAS THE MOST RATINGS
select COUNT(RATING),rating from FILM group by rating order by COUNT(rating) DESC;