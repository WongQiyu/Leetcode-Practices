/*1667*/
SELECT Users.user_id , CONCAT(UPPER(SUBSTR(Users.name,1,1)),LOWER(SUBSTR(Users.name,2))) AS name
FROM Users
ORDER BY
Users.user_id ASC;

/*1527*/
select * from patients where conditions REGEXP '\\bDIAB1'
/*1527 alternative*/
select * from patients where conditions like '% DIAB1%' or
conditions like 'DIAB1%';

/*196*/
Delete p1 from person p1, person p2
where p1.Email = p2.Email and
p1.id >p2.id

/*176*/
select max(salary) as SecondHighestSalary from Employee a
where salary < (select max(salary) from Employee b );

/*1484*/
select sell_date, count(distinct product) as num_sold,
GROUP_CONCAT(Distinct product order by product ASC separator ',') as products
from activities group by sell_date order by sell_date asc

/*1327*/
select p.product_name, sum(o.unit) as unit from products p join
 orders o on p.product_id = o.product_id
where DATE_FORMAT(o.order_date, '%Y-%m') = '2020-02'
group by p.product_id
 having sum(o.unit) >= 100;

/*1517
  . is a specila char, hence \\.com$
  $ is an anchor that asserts the position at the end of the string
  */
select * from users where regexp_like(mail,
'^[A-Za-z]+[A-Za-z0-9\_\.\-]*@leetcode\\.com$');
