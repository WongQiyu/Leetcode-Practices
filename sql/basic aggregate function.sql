select id, movie, description, rating
from cinema where MOD(ID, 2) = 1 and  description <> 'boring' order by rating desc

select p.product_id, ifnull(round(sum(u.units * p.price)/sum(u.units),2),0) as average_price
from prices p left join unitssold u  on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id


# Write your MySQL query statement below
select p.project_id, round(avg(e.experience_years),2) as average_years
from project p join employee e on p.employee_id = e.employee_id
group by p.project_id

# Write your MySQL query statement below

select contest_id, round(count(contest_id) * 100/(select count(user_id) from users) ,2)
as percentage from register group by contest_id order by percentage desc, contest_id asc;

select query_name, round(avg(rating/position),2) as quality,
round(sum(case when rating <3 then 1 else 0 end)* 100/ count(*), 2)
as poor_query_percentage
from queries
where query_name is not null
group by query_name


/*SUBST(trans_date,1,7) to extract moth and year only
  or date_format(trans_date, "%Y-%m")*/
select SUBSTR(trans_date,1,7) as month,
country, count(id) as trans_count,
sum(case when state = 'approved' then 1 else 0 end)
as approved_count,
sum(amount) as trans_total_amount,
sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
GROUP BY month,country;

select
round(100 * sum(if(order_date = customer_pref_delivery_date,1,0)) /
count(customer_id)
,2) as immediate_percentage from delivery
where (customer_id, order_date) in
(select customer_id, min(order_date) from delivery group by customer_id)

/*550*/
select round(count(distinct player_id)/ (select count(distinct player_id) from activity), 2)
as fraction from activity
where (player_id, event_date) in
(select player_id, ADDDATE(min(event_date), INTERVAL 1 DAY)
 from activity group by player_id )

