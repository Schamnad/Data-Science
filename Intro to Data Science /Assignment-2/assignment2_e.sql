-- Write a SQL statement to find all documents that have more than 300
-- total terms, including duplicate terms.
--

Select Count(docid)
from (Select docid, sum(count)
from frequency
Group by docid
having sum(count) > 300);
