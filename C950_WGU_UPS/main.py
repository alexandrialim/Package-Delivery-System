#Alexandria Lim 001452263

import datetime
import packagefile
import truck


#time complexity: O(n^2) multiple nested for loops
#space complexity O(n^2) nested dictionary
def update_status(truckobj, hrs, mins):  # time inputed by user
        #initialize table and variables to store output data
        updatedict = {'Delivered': [], 'En Route': [], 'At Hub': []}
        usertime = datetime.datetime(2022, 11, 24, int(hrs), int(mins))
        departuretime = truckobj.currenttime - datetime.timedelta(minutes=((truckobj.distance_traveled / truckobj.speed) * 60))
        status = ''
        value = {'Package': {}, 'delivery time': {}}
        valuearr = []
        val1 = ''
        global v, j
        #iterate through data to update address for package 9 at 10:20am
        for j in truckobj.packages_delivered: break
        for k_index, k in enumerate(j):
            if k_index % 2 == 0:
                val1 = k
                if usertime <= datetime.datetime(2022,11,24,10,20):
                    if val1[0] == ('PID', 9):
                        val1[1] = ('Address', '300 State St')
                elif usertime >= datetime.datetime(2022,11,24,10,20):
                    if val1[0] == ('PID', 9):
                        val1[1] = ('Address', '410 S State St')
                value.update({'Package': val1})
            #iterate through data to add delivery time info to output list for each package
            if k_index % 2 != 0:
                if truckobj != truck.truck3:
                    new_k = str(k)
                    if new_k[11] == '0':
                        new_k = new_k[:11] + ' ' + new_k[12:]
                        value.update({'delivery time': new_k})
                        valuearr.append(value)
                    else:
                        value.update({'delivery time': str(k)})
                        valuearr.append(value)
                else:
                    value.update({'delivery time': str(k)})
                    valuearr.append(value)
            for v in valuearr: break
            #iterate through output list and return status of a package with the package list values
            #status delivered
            if type(k) == datetime.datetime and usertime >= k > departuretime:
                k2 = str(k)
                if k2[11] != '0':
                    pass
                else:
                    k2 = k2[:11] + ' ' + k2[12:]
                if k2 in v.get('delivery time'):
                    status = 'Delivered'
                    updatedict[status].append(v.copy())
            #status en route
            elif type(k) == datetime.datetime and k >= usertime > departuretime:
                k3 = str(k)
                if k3[11] != '0':
                    pass
                else:
                    k3 = k3[:11] + ' ' + k3[12:]
                if k3 == v.get('delivery time'):
                    status = 'En Route'
                    updatedict[status].append(v.copy())
            #status at hub
            elif type(k) == datetime.datetime and k > usertime < departuretime:
                k4 = str(k)
                if k4[11] != '0':
                    pass
                else:
                    k4 = k4[:11] + ' ' + k4[12:]
                if k4 == v.get('delivery time'):
                    status = 'At Hub'
                    updatedict[status].append(v.copy())
        #print data on individual lines for each package for the truck
        for row1 in updatedict['Delivered']:
            print('Delivered', end=': ')
            print(row1)
        for row2 in updatedict['En Route']:
            print('En Route', end=':  ')
            print(row2)
        for row3 in updatedict['At Hub']:
            print('At Hub: ', end=':  ')
            print(row3)
        return updatedict

#time complexity: O(n^5)
#space complexity: O(n)
if __name__ == '__main__':
    print("Welcome to the Western Governors University Parcel Service")
    total_miles = truck.truck1.distance_traveled + truck.truck2.distance_traveled + truck.truck3.distance_traveled
    print('total mileage across 3 trucks: ' + str(total_miles))
    print("Please enter the hour of day(1 - 24): ")
    usercurrent_hr = input()
    print("Please enter minutes(0 - 59): ")
    usercurrent_minutes = input()
    usertime = datetime.timedelta(hours=int(usercurrent_hr), minutes=int(usercurrent_minutes))
    print('Current user time is: ' + str(usertime))
    print('Input 1 for individual package data (per address), or 2 for all 40 packages data')
    selection = input()
    if selection == '2':
        #print all package data for the 3 trucks
        print('All Package Data:')
        print('Truck 1:')
        update_status(truck.truck1, usercurrent_hr, usercurrent_minutes)
        print()
        print('Truck 2:')
        update_status(truck.truck2, usercurrent_hr, usercurrent_minutes)
        print()
        print('Truck 3:')
        update_status(truck.truck3, usercurrent_hr, usercurrent_minutes)
        print()
        exit()
    elif selection == '1':
        print('Input Address')
        addressinput = input()
        d_time = datetime.time
        data = []
        print('Package(s) data by address:')
        print()
        #create copy of updata status list to pull and modify data for individual packages
        data.append(update_status(truck.truck1, usercurrent_hr, usercurrent_minutes))
        data.append(update_status(truck.truck2, usercurrent_hr, usercurrent_minutes))
        data.append(update_status(truck.truck3, usercurrent_hr, usercurrent_minutes))
        for index, i in enumerate(data):
            for j in i.values():
                for k in j:
                    packageinfo = packagefile.pack.lookup_package(str(addressinput), packagefile.testing)[0][1]
                    for m in packagefile.pack.getrelatedPID(str(packageinfo)):
                        for n in packagefile.testing:
                            if n[8][0] == ('PID', 9):
                                #update address at 10:20am if not already updated
                                if usertime < datetime.timedelta(hours=int(10), minutes=int(20)):
                                        n[8][1] = ('Address', '300 State St')
                                elif usertime >= datetime.timedelta(hours=int(10), minutes=int(20)):
                                        n[8][1] = ('Address', '410 S State St')
                        newPackageInfo = packagefile.pack.lookupPID(str(m), packagefile.testing)
                        #associate truck 0,1,2, with an int value as a index to assign departure times
                        if newPackageInfo == k['Package']:
                            if index == 0:
                                d_time = datetime.timedelta(hours=8, minutes=0)
                            elif index == 1:
                                d_time = datetime.timedelta(hours=9, minutes=5)
                            else:
                                d_time = datetime.timedelta(hours=10, minutes=0)
                            if k['delivery time'][11] == '1':
                                d_hr = int(k['delivery time'][11:13])
                            else:
                                d_hr = int(k['delivery time'][12:13])
                            d_min = int(k['delivery time'][14:16])
                            delivertime = datetime.timedelta(hours=d_hr,minutes=d_min)
                            #return package status based on user time, departure time, and calculated delivery time
                            if d_time <= usertime <= delivertime:
                                print('En Route', end=': ')
                                print(k)
                            elif d_time <= usertime >= delivertime:
                                print('Delivered', end=': ')
                                print(k)
                            elif usertime <= d_time:
                                print('At Hub', end=': ')
                                print(k)
        exit()
    else:
        print('invalid input')
        exit()
