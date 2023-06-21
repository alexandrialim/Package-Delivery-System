# import and link files
import csv

# Read CSV File
class readCSV:
    def __init__(self, file: str):
        self.data = []
        with open(file) as datafile:
            info = csv.reader(datafile, delimiter=",")
            for rows in info:
                self.data.append(rows)
            for o in range(8):
                del self.data[0]