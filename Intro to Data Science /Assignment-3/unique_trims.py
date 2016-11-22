import MapReduce
import sys

"""
Unique trims
Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Remove the last 10 characters from each string then remove any duplicates.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(nucleotide_record):
    mr.emit_intermediate(nucleotide_record[1][:-10], 1)

def reducer(key, num_of_nucleotides):
    mr.emit(key) #That's it

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
