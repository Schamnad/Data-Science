-- Write a SQL statement to count the number of unique documents that -- contain both the word 'transactions' and the word 'world'
--
Select Count(distinct docid)
from frequency
where term is 'transactions'
and docid in (Select docid
from frequency
where term is 'world');
