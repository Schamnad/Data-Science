import MapReduce
import sys

"""
Relational join - Sanjeed Schamnad
     SELECT *
     FROM Orders, LineItem
     WHERE Order.order_id = LineItem.order_id
Sample input:
["order", "1", "36901", "O", "173665.47", "1996-01-02", "5-LOW", "Clerk#000000951", "0", "nstructions sleep furiously among "]
["line_item", "1", "63700", "3701", "3", "8", "13309.60", "0.10", "0.02", "N", "
O", "1996-01-29", "1996-03-05", "1996-01-31", "TAKE BACK RETURN", "REG AIR", "ri
ously. regular, express dep"]
The first field indicates what type of record, second field is the order_id.
Combination should have 27
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    length = len(list_of_values)

    for i in range(1,length):
        attr_list = []
        attr_list += list_of_values[0] + list_of_values[i]
        mr.emit(attr_list)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
