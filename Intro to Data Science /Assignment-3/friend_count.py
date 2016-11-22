import MapReduce
import sys

"""
Friend Count
Input is a two-element list [personA, personB], representing a simple social network.  Note that friendship may not be bidirectional.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(friend_record):
    mr.emit_intermediate(friend_record[0], 1)

def reducer(key, list_of_friends):
    num_of_friends = len(list_of_friends)
    mr.emit((key,num_of_friends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
