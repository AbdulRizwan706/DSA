-- Write your PostgreSQL query statement below
delete from Person email
where id not in (
    select min(id) from Person
    group by email
)