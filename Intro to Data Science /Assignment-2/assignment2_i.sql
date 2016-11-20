-- Find the best matching document to the keyword query
-- "washington taxes treasury".
-- ;

--add the search query "washington taxes treasury" to the corpus
create table if not exists q ( kw varchar(20) );
insert into q values('washington');
insert into q values('taxes');
insert into q values('treasury');

Select docid, max(similarity)
from (Select A.docid, B.docid, Sum(A.count) as similarity
From frequency A join frequency B on A.term = B.term
where A.docid < B.docid
and A.term in (Select kw from q)
and B.term in (Select kw from q)
Group by A.docid, B.docid);
