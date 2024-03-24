
select eu.unique_id, e.name from Employees e left join EmployeeUNI eu on e.id = eu.id


select p.product_name , s.year, s.price
from sales s join product p on s.product_id = p.product_id

/*Group by*/
select customer_id, count(visit_id) as count_no_trans from visits
where visit_id not in
(select visit_id from transactions) group by customer_id


select w2.id from
weather w1, weather w2
where datediff(w2.recordDate, w1.recordDate) = 1
and w2.temperature > w1.temperature

select machine_id,
Round(sum(case when activity_type='start' then timestamp*-1 else timestamp end)
/ (select count(distinct process_id) ), 3) as processing_time
from activity group by machine_id

select name, bonus from employee left join bonus using(empId) where coalesce(bonus,0) <1000

select s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) as
attended_exams from students s
JOIN subjects sub
LEFT JOIN examinations e on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by s.student_id, sub.subject_name
order by s.student_id, sub.subject_name

select e1.name from employee e1
where e1.id in (
    select e2.managerId from employee e2
    group by e2.managerID
    having count(e2.managerID) >= 5
)
/*
 select e2.name from employee e1 inner join employee e2
on e1.managerID = e2.id group by e1.managerID
having count(e1.managerID) >= 5
 */

select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;

