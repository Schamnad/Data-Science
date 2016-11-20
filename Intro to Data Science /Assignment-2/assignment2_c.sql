-- Write a SQL statement that is equivalent to the following relational
-- algebra expression.
-- πterm( σdocid=10398_txt_earn and count=1(frequency)) U πterm( σdocid=925_txt_trade and count=1(frequency))

Select Count(term)
from frequency
where docid in ('10398_txt_earn', '925_txt_trade') and count = 1;
