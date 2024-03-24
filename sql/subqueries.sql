/*1978
  can ignore manager_id is not null in this case as a clause as null manager_id wont be picked up*/
select employee_id from employees where salary <30000
and manager_id not in (select distinct employee_id from employees) order by employee_id

/*626*/
select ROW_NUMBER() Over() id, student
from seat
ORDER BY IF(MOD(id,2) = 0 , id-1, id+1);

/*1341: union all allows for subqueris*/
(select name as results from
(select u.name, mr.user_id,count(mr.user_id) as counting from MovieRating mr left join users u
on mr.user_id = u.user_id
group by mr.user_id order by counting desc, name asc limit 1) as tmp)
union all
(select m.title as results from MovieRating mr left join movies m on mr.movie_id = m.movie_id
where DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
group by m.title
order by avg(mr.rating) desc, m.title asc limit 1);

/*602*/
select requester_id id ,count(requester_id) num from
(select requester_id from RequestAccepted
union all select accepter_id from RequestAccepted) tmp
group by requester_id order by num desc limit 1;

/*585*/
select round(sum(tiv_2016), 2)  TIV_2016 from (
    select tiv_2016, count(*) over(partition by tiv_2015) as cnt1,
    count(*) over(partition by lat,lon) as cnt2
    from insurance
) as tbl
where cnt1 >= 2 and cnt2 = 1

/*1321 challenging - rolling time*/
SELECT a.visited_on, sum(b.day_sum) as amount,
round(avg(b.day_sum),2) as average_amount
from
(select visited_on, sum(amount) as day_sum from customer group by visited_on) a,
(select visited_on, sum(amount) as day_sum from customer group by visited_on) b
where DATEDIFF(a.visited_on, b.visited_on) Between 0 and 6
group by a.visited_on
having count(b.visited_on) = 7

/*185 hard*/
select d.name as Department, e1.name as Employee, salary  Salary from employee e1
left join department d on e1.departmentId = d.id
where 3 > ( select count(distinct(e2.Salary))
from Employee e2
where e2.Salary > e1.Salary and e1.DepartmentId= e2.DepartmentID);


