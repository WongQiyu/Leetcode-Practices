/* select */

select product_id from Products where low_fats = 'Y' and recyclable = 'Y';


select name from Customer where referee_id <> 2 OR referee_id is NULL

select name, population, area from world where area >= 3000000
union
select name, population, area from world where population >= 25000000


select distinct author_id as id from Views where author_id = viewer_id order by author_id

select tweet_id from Tweets where Length(content) > 15