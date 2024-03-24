WITH tt AS(
SELECT user_id, COUNT(user_id) as tb FROM tweets
where tweet_date >= '2022-01-01 00:00:00' And tweet_date < '2023-01-01 00:00:00'
GROUP BY user_id)
select tb as tweet_bucket,
count(user_id) as users_num
from tt GROUP BY tb
;