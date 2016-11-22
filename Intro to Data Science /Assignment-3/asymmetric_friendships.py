import MapReduce
import sys

"""
Asymmetric relationship detector
Input is a two-element list [personA, personB], representing a simple social network.  Note that friendship may not be bidirectional.  Show the ones that are not symmetric.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(friend_record):
    mr.emit_intermediate(friend_record[0], friend_record[1])

def reducer(key, list_of_friends):
    for false_friend in list_of_friends:
        if false_friend not in mr.intermediate or key not in mr.intermediate[false_friend]:
            mr.emit((false_friend,key))
            mr.emit((key,false_friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
