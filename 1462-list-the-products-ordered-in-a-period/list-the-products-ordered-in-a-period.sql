# Write your MySQL query statement below
select p.product_name ,sum(unit) as unit
from  Products p
join Orders k
on k.product_id=p.product_id
where k.order_date between '2020-02-1' and '2020-02-29' 
group by k.product_id 
having sum(unit)>=100


