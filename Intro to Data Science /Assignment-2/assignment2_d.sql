-- count the number of unique documents containing the word "law" or containing the word "legal" (If a document contains both law and legal, it should only be counted once)

Select Count(distinct docid)
from frequency
where term in ('law', 'legal');
