import packagefile
from distancefile import df
import re
from datetime import datetime, time, timedelta


class Truck:
    # initialize values and lists
    # time complexity: O(1)
    # space complexity: 3*O(1)
    def __init__(self, truckID):
        self.id = truckID
        self.speed = 18.0
        self.capacity = 16
        self.packages_loaded = []
        self.packages_delivered = []
        self.distance_traveled = float()
        self.address = "4001 South 700 East"
        self.timetraveled = time()
        self.currenttime = time()
        self.packages_unloaded_at = []

    # time complexity: O(n^3)
    # space complexity: O(n)
    #load data into truck 1
    def loadtruck1(self, arr, arr1):
        #initialize variables and lists
        A = ''
        val = None
        eachval = None
        eachvalue = None
        eachitem = None
        vals = None
        item = None
        num1 = []
        temparr = []
        temparr1 = []
        templist1 = []
        l1_list = []
        temp2 = []
        temp1 = arr.copy()
        #check notes for 'must be delivered with' and append all packages to the list with that note
        for i in temp1[0]:
            for j in i:
                if "Must be delivered with " in i[7][1]:
                    A = (re.findall("[0-9]+", i[7][1]))
                    A.append(str(i[0][1]))
                    for n in A:
                        temparr.append(n)
                        temparr = list(dict.fromkeys(temparr))
                    #grab Package ID and append to list
                    for m in temparr:
                        val = packagefile.pack.lookupPID(m, packagefile.testing)
                        if val not in arr1:
                            arr1.append(val)
        #check if appended Package ID has other package IDs going to the same address
        #append additional Package IDs if there are other ones
        for o in temparr:
            temparr1.extend(packagefile.pack.getrelatedPID(o))
            temparr1 = list(dict.fromkeys(temparr1))
        for p in temparr1:
            p = str(p)
            val2 = packagefile.pack.lookupPID(p, packagefile.testing)
            if val2 not in arr1:
                arr1.append(val2)
        for l in arr1:
            l1 = df.nextclosest(l[1][1])
            l1_list.append(l1)
            l1_list = list(dict.fromkeys(l1_list))
        for q in arr1:
            templist1.append(q[1][1])
            r = set(l1_list).difference(set(templist1))
        HUB = "4001 South 700 East,"
        r = list(r)
        tempval = ''
        #make sure that the addresses being appended aren't the hub's address
        if HUB in r:
            if HUB == r[1]:
                tempval = r[0]
            elif HUB == r[0]:
                tempval = r[1]
            num1.append(packagefile.pack.lookup_package(tempval, packagefile.testing))
            tempnum1 = num1[0][0][1]
            tempnum1 = str(tempnum1)
            s = packagefile.pack.getrelatedPID(tempnum1)
            for t in s:
                arr1.append(packagefile.pack.lookupPID(str(t), packagefile.testing))
        #check if original list has already been added to new list or not
        #if not added yet, add to the list
        for abc in arr:
            for eachvalue in range(len(arr1)):
                for ab in range(len(abc)):
                    if eachvalue >= len(arr1):
                        break
                    eachitem = arr1[eachvalue]
                    if ab >= len(abc):
                        break
                    item = abc[ab]
                    if eachitem == item:
                        temp2.append(ab)
                        temp2.sort()
                        temp2.reverse()
        #remove any values that have been added to the new list from the old list
        for eachval in temp2:
            try:
                arr[0].pop(eachval)
            except:
                pass

        #add package information to list for packages going to 1330 2100 S
        for rs in packagefile.pack.getrelatedPID(
                str(packagefile.pack.lookup_package("1330 2100 S", packagefile.testing)[0][1])):
            arr1.append(packagefile.pack.lookupPID(str(rs), packagefile.testing))
            arr[0].remove(packagefile.pack.lookupPID(str(rs), packagefile.testing))

        # add package information to list for packages going to 380 W 2880 S
        for tu in packagefile.pack.getrelatedPID(
                str(packagefile.pack.lookup_package("380 W 2880 S", packagefile.testing)[0][1])):
            arr1.append(packagefile.pack.lookupPID(str(tu), packagefile.testing))
            arr[0].remove(packagefile.pack.lookupPID(str(tu), packagefile.testing))

        # add package information to list for packages going to 195 W Oakland Ave
        for uv in packagefile.pack.getrelatedPID(
                str(packagefile.pack.lookup_package("195 W Oakland Ave", packagefile.testing)[0][1])):
            arr1.append(packagefile.pack.lookupPID(str(uv), packagefile.testing))
            arr[0].remove(packagefile.pack.lookupPID(str(uv), packagefile.testing))

    # load data into truck 2
    # time complexity: O(n^2)
    # space complexity: O(n)
    def loadtruck2(self, arr, arr1):
        # initialize variables and lists
        A = ''
        B = ''
        C = ''
        D = ''
        mval1 = []
        mlist = []
        nlist = []
        clist = []
        dlist = []
        elist = []
        oval1 = []
        oval2list = []
        dval1 = None
        dval3 = None
        ovalue = None
        temp1 = arr.copy()
        # check notes for all packages that have 'truck 2' and append package data to the new list
        for i in temp1[0]:
            if "truck 2" in i[7][1]:
                arr1.append(i)
        # check for any related packages that have the same addresses that are already appended to the list
        for j in arr1:
            k = packagefile.pack.getrelatedPID(str(j[0][1]))
            for l in k:
                appendval1 = packagefile.pack.lookupPID(str(l), packagefile.testing)
                if appendval1 not in arr1:
                    arr1.append(appendval1)
        # iterate through the list of package addresses to find the next closest address
        # once next closest is found, append package data to the list
        for m in arr1:
            mval = df.nextclosest(m[1][1])
            mval1.append(mval)
            mlist.append(m[1][1])
            B = set(mval1).difference(set(mlist))
        for n in B:
            nlist.extend(
                packagefile.pack.getrelatedPID(str(packagefile.pack.lookup_package(n, packagefile.testing)[0][1])))
        for o in nlist:
            o = str(o)
            oval = packagefile.pack.lookupPID(o, packagefile.testing)
            if oval[0] != ('PID', 9):
                arr1.append(oval)
            else:
                pass
            ovalue = df.nextclosest(oval[1][1])
            oval1.append(ovalue)
        for oval2 in arr1:
            oval2list.append(oval2[1][1])
            oval2list = list(dict.fromkeys(oval2list))
            C = set(oval2list).difference(set(oval1))
        for cval in C:
            cval2 = df.nextclosest(cval)
            clist.append(cval2)
        for cval3 in arr1:
            dlist.append(cval3[1][1])
            D = set(clist).difference(set(dlist))
        for dval in D:
            arr1.append(packagefile.pack.lookup_package(dval, packagefile.testing))
            dval1 = df.nextclosest(dval)
        for dval2 in arr1:
            if dval1 not in dval2[1][1]:
                dval2 = packagefile.pack.getrelatedPID(
                    str(packagefile.pack.lookup_package(dval1, packagefile.testing)[0][1]))
                for dv in dval2:
                    dval3 = packagefile.pack.lookupPID(str(dv), packagefile.testing)
                    if len(elist) < 2:
                        elist.append(dval3)
                    else:
                        pass
        for e in elist:
            if e in arr1:
                continue
            arr1.append(e)

        # add package data for 600 E 900 South
        for f in packagefile.pack.getrelatedPID(
                str(packagefile.pack.lookup_package("600 E 900 South", packagefile.testing)[0][1])):
            arr1.append(packagefile.pack.lookupPID(str(f), packagefile.testing))
            arr[0].remove(packagefile.pack.lookupPID(str(f), packagefile.testing))

        # remove all package data in new list from old list to avoid having the same package on different trucks
        for eachval in arr1:
            try:
                arr[0].remove(eachval)
            except:
                pass

        pass

    #load remaining packages into truck 3
    #time complexity: O(n)
    #space complexity: O(1)
    def loadTruck(self, arr, arr1):
        temp = arr[0].copy()
        for all in temp:
            arr1.append(all)
            arr[0].remove(all)

    # Method for ordering packages on a specific truck
    # This method also calculates the distance a truck drives after the packages are sorted
    # time complexity: O(n log n)
    # space complexity: O(n)
    def delivering_packages(self, arr, truckarr, leavehr, leavemin):
        arr1 = arr[0].copy()
        copytruck = truckarr.copy()
        delivered = []
        stop = float
        back_home = float()
        departat = time(leavehr, leavemin)
        for i in arr1:
            self.packages_loaded.append(i[0])
        for packageID in self.packages_loaded:
            packagefile.pack.lookupPID(str(packageID[1]), packagefile.testing)

        # Clear the package list of a given truck so the packages can be placed back into the truck in the order
        # of the next nearest location within the list of packages on the truck
        self.packages_loaded.clear()

        # Adds the nearest package into the delivered list one by one
        # And calculates the time and distance traveled for each package location and the truck
        # Cycles through the list of packages until none remain in the list
        previousindex = None
        tempval = list()
        for t in copytruck:
            if t[1][1] in truckarr[0][1]:
                tempval.append(t)
                copytruck.remove(t)
                stop = float(df.getdistance(self.address, t[1][1]))
        self.distance_traveled += stop
        travel = '{0:02.0f}:{1:02.0f}'.format(
            *divmod((self.distance_traveled / self.speed) * 60, 60))  # distance in minutes
        self.timetraveled = datetime.strptime(travel, '%H:%M').time()  # converts into readable time
        self.currenttime = datetime(2022, 11, 24) + timedelta(days=0, hours=departat.hour,
                                                              minutes=departat.minute) + timedelta(days=0,
                                                                                                   hours=self.timetraveled.hour,
                                                                                                   minutes=self.timetraveled.minute)
        for s in tempval:
            delivered.append(s)
            delivered.append(self.currenttime)
        # continue cycling through the list and checking for distance between 2 points and calculate travel time
        while len(copytruck) > 0:
            for t2 in copytruck:
                if df.nextclosest(truckarr[0][1][1]) in t2[1][1]:
                    previousindex = truckarr.index(t2)
                    delivered.append(t2)
                    delivered.append(self.currenttime)
                    copytruck.remove(t2)
                    stop = float(df.getdistance(truckarr[0][1][1], df.nextclosest(truckarr[0][1][1])))
            self.distance_traveled += stop
            travel = '{0:02.0f}:{1:02.0f}'.format(
                *divmod((self.distance_traveled / self.speed) * 60, 60))  # distance in minutes
            self.timetraveled = datetime.strptime(travel, '%H:%M').time()  # converts into readable time
            self.currenttime = datetime(2022, 11, 24) + timedelta(days=0, hours=departat.hour,
                                                                  minutes=departat.minute) + timedelta(days=0,
                                                                                                       hours=self.timetraveled.hour,
                                                                                                       minutes=self.timetraveled.minute)

            # continue cycling through the list and checking for distance between 2 points and calculate travel time
            for t3 in copytruck:
                if df.nextclosest(truckarr[previousindex - 1][1][1]) in t3[1][1]:
                    delivered.append(t3)
                    delivered.append(self.currenttime)
                    copytruck.remove(t3)
                    stop = float(df.getdistance(truckarr[previousindex - 1][1][1],
                                                df.nextclosest(truckarr[previousindex - 1][1][1])))
                    break
                elif df.nextclosest(truckarr[previousindex + 1][1][1]) in t3[1][1]:
                    delivered.append(t3)
                    delivered.append(self.currenttime)
                    copytruck.remove(t3)
                    stop = float(df.getdistance(truckarr[previousindex + 1][1][1],
                                                df.nextclosest(truckarr[previousindex + 1][1][1])))
                    break
                else:
                    delivered.append(t3)
                    delivered.append(self.currenttime)
                    copytruck.remove(t3)
                    stop = float(
                        df.getdistance(truckarr[previousindex][1][1],
                                       df.nextclosest(truckarr[previousindex][1][1])))
                    continue
            # if truck is finished with delivering packages, calculate distance and time back to hub
            if len(copytruck) == 1:
                back_home = df.getdistance(copytruck[0][1][1], self.address)
                back_home = float(back_home)

            # add all data to lists and calculate totals of time and distance
            self.distance_traveled += stop
            self.distance_traveled = self.distance_traveled + back_home
            self.currenttime = datetime(2022, 11, 24) + timedelta(days=0, hours=departat.hour,
                                                                  minutes=departat.minute) + timedelta(days=0,
                                                                                                       hours=(self.distance_traveled / self.speed))
            self.packages_unloaded_at.append(self.currenttime)
            self.packages_delivered = [p for p in self.packages_delivered if p[0][1] != delivered[0][1]]
            self.packages_delivered.append(delivered)






# variables
truck1arr = []
truck2arr = []
truck3arr = []
allPkgs = []
copyPkgs = []

#add data to lists to be able to modify any information that may be needed
copyPkgs.append(list(packagefile.Package.Group(packagefile.pack.hashmap.table, 8)))
allPkgs.append(list(packagefile.Package.Group(packagefile.pack.hashmap.table, 8)))

#initialize truck objects
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

#load trucks with packages
truck1.loadtruck1(allPkgs, truck1arr)
truck2.loadtruck2(allPkgs, truck2arr)
truck3.loadTruck(allPkgs, truck3arr)

#create delivery route and calculate delivery time and mileage
truck1.delivering_packages(copyPkgs, truck1arr, 8, 0)
truck2.delivering_packages(copyPkgs, truck2arr, 9, 5)
truck3.delivering_packages(copyPkgs, truck3arr, 10, 0)

#print(len(truck1arr))
#print(len(truck2arr))
#print(len(truck3arr))