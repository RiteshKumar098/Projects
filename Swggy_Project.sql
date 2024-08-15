use food_delivery;
show tables;

/*Describing schema of a table*/
describe swiggy;

/*Setting ID column as a primary key*/
alter table swiggy
add primary key(ID);

/*Find total numbers of rows from the table*/
select count(*) from swiggy;

/*Find total restaurants from where the orders were made*/
select count(distinct(Restaurant))
from swiggy;

/*Find total numbers of orders made from each restaurant*/
select Restaurant, count(ID) as total_orders
from swiggy 
group by Restaurant;

/* Find top three restaurants with maximum numbers of orders*/
select Restaurant, count(ID) as orders, dense_rank() over (order by count(ID) desc) as rankk
from swiggy 
group by Restaurant
limit 3;

/*OR*/
select Restaurant, count(ID) as orders
from swiggy 
group by Restaurant
order by orders desc
limit 3;

/*Find total number of restaurants from each city*/
select City, count(Restaurant)
from swiggy
group by City
order by count(Restaurant) desc;


/*What is average delivery time taken by swiggy*/
select avg(Delivery_time) 
from swiggy;

/*Find all restaurants from Kormangala Bangalore*/
select Restaurant
from swiggy 
where City = 'Bangalore' and Area = 'Koramangala';

select * from swiggy;

/*Find average Price of restaurants from Powai area of Mumbai*/
select City, Area, avg(Price)
from swiggy
group by Area 
having City = "Mumbai" and Area = "Powai";

/*Rank all restaurant based on their average ratings*/
select Restaurant, Avg_ratings, dense_rank() over (order by Avg_ratings desc) as Position
from swiggy 
group by Restaurant;

/*Find restaurants from Delhi who serves Fast food or Chinese or both*/
select *
from swiggy
where (Food_type = 'Fast Food' or Food_type = 'Chinese')
and City = 'Delhi';

/*Find restaurants from Hyderabad who serves Fast food or Chinese or Mughlai or 
North Indian or South indian*/
select *
from swiggy
where Food_type in ('Fast Food','Chinese', 'North Indian','South Indian','Mughlai')
and City = 'Hyderabad';
