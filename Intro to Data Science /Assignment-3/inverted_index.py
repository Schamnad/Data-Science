import MapReduce
import sys

"""
Inverted Index
The input is a two-element list: [document_id, text].  The document text may have words in upper or lower case and may contain punctuation.  Each token is treated as if it was a valid word.
"""

mr = MapReduce.MapReduce()

#
# Make the word list unique & preserve order.
# Source: http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-whilst-preserving-order
# Complexity: O(1) insertion, deletion and member-check per operation.
#
def make_unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def mapper(record_list):
    key = record_list[0]
    value = record_list[1]
    for word in value.split():
        mr.emit_intermediate(word, key)

def reducer(key, list_of_values):
    index_list = []
    for doc in list_of_values:
        index_list += doc
    mr.emit((key, index_list))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
