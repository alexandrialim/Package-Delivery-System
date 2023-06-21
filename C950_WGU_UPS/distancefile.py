from readCSVfile import readCSV
import Hashtable


class delivery:
    #time complexity: O(1)
    #space complexity: O(n)
    #initialize hash tables and variables
    def __init__(self, address1):
        self.address1 = address1
        self.hashmap = Hashtable.HashTable()
        self.distance = Hashtable.HashTable()

    #time complexity: O(n)
    #space complexity: O(1)
    #create address hash table
    def createAddHash(self, data):
        for row in data:
            self.address = row[0]
            self.distances = row[2:]
            self.hashmap.insert("Address", self.address)
            self.hashmap.insert("miles", self.distances)
        return self.hashmap.table

    # time complexity: O(n)
    # space complexity: O(N)
    #create distance hash table
    def createDistHash(self, data):
        for row in data:
            self.distances = row[2:]
            self.distance.insert("miles", self.distances)
        return self.distance.table

    # time complexity: O(1)
    # space complexity: O(n^2)
    #get the distance between two addresses
    def getdistance(self, vertex1, vertex2): #address1, address2
        rowind = self.hashmap.getIndex(vertex1)
        colind = self.hashmap.getIndex(vertex2)
        row = distances[colind][1]
        col = row[rowind]
        if len(col) == 0:
            row = distances[rowind][1]
            col = row[colind]
        return col

    # time complexity: O(n)
    # space complexity: O(n)
    #return the next closest address in list
    def nextclosest(self, var1): #input address string
        tempaarr = []
        for s in df.hashmap.getValue("Address"):
            result = float(df.getdistance(var1, s))
            tempaarr.append(result)
            minval = min(number for number in tempaarr if number > 0.0)
            val1 = tempaarr.index(minval)
            output = df.hashmap.getValue("Address")[val1]
            output = output.split("\n")[1]
            output = output.split(" ", 1)[1]
        return output

#read distance table csv
deliver = readCSV("WGUPS Distance Table.csv")

#map delivery data
df = delivery(deliver.data[0][0])

#create hash table for address and mileage
addtable = df.createAddHash(deliver.data)
output = df.hashmap.table

#create distance table with just mileage
distances = df.createDistHash(deliver.data)
