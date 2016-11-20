--
-- Express A X B as a SQL query.  REturn just the value of cell (2,3)
--
--

Select mult
from (Select A.row_num, B.col_num, Sum(A.value*B.value) as mult
from A, B
where A.col_num = B.row_num
group by A.row_num, B.col_num)
where row_num = 2 and col_num = 3;
