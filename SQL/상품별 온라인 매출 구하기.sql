select p.product_code, sum(s.sales_amount) * p.price as sales
from product p
right outer join offline_sale s
on p.product_id = s.product_id
where s.sales_amount > 0 and p.product_id 
group by p.product_code
order by sales desc, product_code asc
