-- Write a SQL statement that is equivalent to the following relational algebra expression.
--
-- πterm(σdocid=10398_txt_earn and count=1(frequency))

Select Count(term)
from frequency
where docid like '10398_txt_earn' and count = 1;
