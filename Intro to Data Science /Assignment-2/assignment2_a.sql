-- Write a query that is equivalent to the following relational algebra expression.
--
-- σdocid=10398_txt_earn(frequency)

Select Count(*)
from frequency
where docid like '10398_txt_earn';
