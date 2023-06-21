import Hashtable
from readCSVfile import readCSV


class Package:
    status = "At Hub"

    # Initialize package values
    # time complexity: O(1)
    # space complexity: O(n)
    def __init__(self, pid, address, city, state, zip, dd, mass, notes):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.dd = dd
        self.mass = mass
        self.notes = notes
        self.deliverystatus = Package.status
        self.hashmap = Hashtable.HashTable()  # Create a hash map

    # time complexity: O(1)
    # space complexity: O(n)
    #create hash table
    #map out key values
    #add values to initialized keys
    def createHash(self, data):
        for row in data:
            self.pid = row[0]
            self.address = row[1]
            self.city = row[2]
            self.state = row[3]
            self.zip = row[4]
            self.dd = row[5]
            self.mass = row[6]
            self.notes = row[7]
            self.hashmap.insert("PID", int(self.pid))
            self.hashmap.insert("Address", self.address)
            self.hashmap.insert("City", self.city)
            self.hashmap.insert("State", self.state)
            self.hashmap.insert("Zip", self.zip)
            self.hashmap.insert("Delivery", self.dd)
            self.hashmap.insert("Weight", self.mass)
            self.hashmap.insert("Notes", self.notes)
        return self.hashmap.table

    # look up package info based on address
    # time complexity: O(n^3)
    # space complexity: O(n)
    def lookup_package(self, data: str, list):
        output = self.hashmap.getrelatedvalues(data)
        for all in list:
            for i in all:
                for each in output:
                    if each in i[1]:
                        return i

    #look up notes for specific package
    # time complexity: O(n^3)
    # space complexity: O(n)
    def lookupinfo_notes(self, data: str, list):
        output = self.hashmap.getrelatedvalues(data)
        for all in list:
            for i in all:
                for each in output:
                    if each in i[7]:
                        return i

    #look up Package ID for all packages at a specific address
    # time complexity: O(n^3)
    # space complexity: O(n)
    def lookupPID(self, data: str, list):
        output = self.hashmap.getrelatedvalues(data)
        for all in list:
            for i in all:
                for each in output:
                    if each in i[0]:
                        return i
                        # break

    # look up package delivery deadline based on address
    # time complexity: O(n^3)
    # space complexity: O(n)
    def lookup_bytime(self, data: str, list):
        output = self.hashmap.getrelatedvalues(data)
        for all in list:
            for i in all:
                for each in output:
                    if each in i[5]:
                        return i
                        # break

    #group packages by address
    # time complexity: O(n)
    # space complexity: O(n)
    def Group(list, pos):
        # looping till length l
        for i in range(0, len(list), pos):
            yield list[i:i + pos]

    #get all related package IDs
    # time complexity: O(n^2)
    # space complexity: O(n)
    def getrelatedPID(self, num):
        temp = []
        for all in testing:
            for j in all:
                val = pack.lookupPID(num, testing)
                if val[1][1] == j[1][1]:
                    temp.append(j[0][1])
            return temp

#Read package file csv
pkg = readCSV("WGUPS Package File.csv")

#map package data to values in hash table
pack = Package(pkg.data[0][0], pkg.data[0][1], pkg.data[0][2], pkg.data[0][3], pkg.data[0][4], pkg.data[0][5],
               pkg.data[0][6], pkg.data[0][7])

#create hash table by feeding in mapped values
table = pack.createHash(pkg.data)
testing = []

#group package values so that each package has a set of values
out = pack.hashmap.table
testing.append(list(Package.Group(out, 8)))

