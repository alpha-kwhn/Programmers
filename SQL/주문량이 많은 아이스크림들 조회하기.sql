select A.FLAVOR
from (select * from FIRST_HALF union select * from JULY) A
group by A.FLAVOR
order by SUM(A.TOTAL_ORDER) DESC
limit 3;
