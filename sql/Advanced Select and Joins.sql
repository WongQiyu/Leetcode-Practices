/*1731*/
select e1.employee_id, e1.name, count(*) as reports_count,
round(avg(e2.age)) as average_age
from employees e1
right join employees e2 on e1.employee_id = e2.reports_to
where e1.employee_id is not null
 group by e1.employee_id order by employee_id;

/* 1789 */
select employee_id, department_id from employee
where primary_flag = 'Y' union
select employee_id, department_id from employee group by employee_id having
count(employee_id) = 1;

/* 610 */
select *, if (x + y > z and y + z > x and x + z > y, "Yes", "No") as triangle from Triangle;

/* 180 */
with cte as (select num,
lead(num,1) over() num1,
lead(num,2) over() num2 from logs)

select distinct num as ConsecutiveNums from cte where ( num= num1) and (num= num2);

/*1164*/

select distinct p1.product_id , COALESCE(p2.new_price,10) as price
from products p1 left join
(select product_id, new_price, change_date from products
 where (product_id, change_date) in
(select product_id, max(change_date) as change_date from products
where change_date < '2019-08-17' group by product_id)) as p2
on p1.product_id = p2.product_id;

/*1204*/
select person_name from
(select person_name, turn, weight, sum(weight)
over(order by turn) as total from queue ) as tmp where total <= 1000
order by total desc limit 1
/*
SELECT Date, Sales,
SUM(Sales)
OVER (ORDER BY Date) as CumulativeSales
FROM daily_sales;`*/

/*1907*/
# Write your MySQL query statement below
(
select "Low Salary" as category,
(select count(*) from accounts where income <20000 )as accounts_count)
union
(select "Average Salary" as category,
(select count(*) from accounts where income >=20000 and income <= 50000)
as accounts_count)
union
(select "High Salary" as category,
(select count(*) from accounts where income >50000) as accounts_count);