# hashtable

# Create Hashtable class:
class HashTable:
    # assign empty list
    # time complexity: O(1)
    # space complexity: O(N)
    def __init__(self):
        # initialize hash table with empty bucket entries
        self.table = []

    # insert function
    # inserts a value to the end of the table
    # time complexity: O(1)
    # space complexity: O(N)
    def insert(self, key, value):
        self.table.append((key, value))

    # search function
    # searches for package record by looking at key and value pair
    # returns value if key-value pair is found
    # returns 'none' if the key-value pair is NOT found
    # hashes key
    # time complexity: O(n)
    # space complexity: O(N)
    def getValue(self, key):
        values = []
        for k in range(len(self.table)):
            if str(hash(self.table[k][0])) in str(hash(key)):
                if k < 0:
                    return None
                else:
                    values.append(self.table[k][1])
        return values

    #look up info based on address
    #how many packages are sent to the home
    #existing package info from package file
    # time complexity: O(n)
    # space complexity: O(N)
    def getrelatedvalues(self, value):
        list = []
        for v in range(len(self.table)):
            if value in str(self.table[v][1]):
                if v < 0:
                    return None
                else:
                    list.append(self.table[v][1])
        return list

    #get index of any value that you are looking for
    # time complexity: O(n^2)
    # space complexity: O(N)
    def getIndex(self, value):
        for v in range(len(self.table)):
            if value in str(self.table[v][1]):
                if v < 0:
                    return None
                else:
                    for index, x in enumerate(self.table):
                        indexnum = (int(v/2))
                        break
        return indexnum

