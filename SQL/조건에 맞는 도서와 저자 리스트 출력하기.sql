select b.book_id, a.author_name, DATE_FORMAT(b.published_date, '%Y-%m-%d') as published_date
from book b
left outer join author a
on a.author_id = b.author_id
where b.category = '경제'
order by DATE_FORMAT(b.published_date, '%Y-%m-%d') asc
