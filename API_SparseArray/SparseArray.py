# This class contains one function MatchStinrgs
# This function must return an array of integers representing 
# the frequency of occurrence of each query string in strings.

#Library to count occurences
from collections import Counter 

class SparsArrayClass:
    def __init__(self, string, query):
        self.string = string
        self.query = query
        
    def matchingStrings(strings, queries):            
        counter = Counter(strings)
        keys = list(queries)
        values = [counter[q] for q in queries]
        return dict(zip(keys, values))
