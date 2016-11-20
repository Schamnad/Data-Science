--
-- Write a query to compute the similarity matrix D x DT.
--

Select count
from (Select A.docid as docidA, B.docid as docidB, Sum(A.count*B.count) as count
from frequency A, frequency B
where A.term = B.term and A.docid < B.docid
Group by A.docid, B.docid)
where docidA like '10080_txt_crude' and docidB like '17035_txt_earn';
