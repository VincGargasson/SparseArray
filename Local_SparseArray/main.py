from SparseArray import SparsArrayClass
import sys 
import os 

if __name__ == '__main__':
    
    #collecting queries input from user
    queries_input = sys.argv[1]
    #Processing user input
    queries = queries_input.split(sep=',')
    queries_count = len(queries)

    #Defining string input
    strings = os.getenv("STRINGS",['ab','abc','abc','abc','bc','bc'])
    queries_count = len(strings)

    result = SparsArrayClass.matchingStrings(strings, queries)
    print(result)
