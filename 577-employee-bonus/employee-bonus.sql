# Write your MySQL query statement below
select e.name,b.bonus
from Employee e
left join Bonus b on e.empid=b.empid
where bonus<1000 or bonus is NULL
