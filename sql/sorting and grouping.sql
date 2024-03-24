
select teacher_id, count(distinct(subject_id)) as cnt from teacher group by teacher_id


select activity_date as day, count(distinct(user_id)) as active_users
from activity
where datediff('2019-7-27',activity_date) between 0 and 29
group by activity_date

/*1070 --> group by product id cannot work cos its a foreign key and  year, sales_id is PK*/
select product_id, year as first_year, quantity, price from sales
where (product_id, year) in
(select product_id, min(year) as year from sales group by product_id)

select class from courses  group by class having count(class) >= 5

/*1729 is tricky:
  user_id same as follower_id
  */
select user_id, Count(follower_id) as followers_count from followers group by user_id order by user_id

/*619
cannot just do:
select max(num) as num from MyNumbers group by num having count(num) = 1
above will give all the num with the 'having' condition
 */


select max(num) as num from
(select num from MyNumbers group by num having count(num) = 1) as tmp

/*1045*/
select customer_id from customer group by customer_id
having count(distinct product_key) = (select count(*) from product)

