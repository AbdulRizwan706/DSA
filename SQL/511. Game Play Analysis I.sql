-- Write your PostgreSQL query statement below
select 
    activity.player_id,
    min(event_date) as first_login
from Activity
group by activity.player_id