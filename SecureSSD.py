import csv
irp = {}
packet = []
eps = []
with open('/Users/apple/Desktop/Research/Dr. NEERAJ GOEL/Logs/WannaCry3.csv', 'r') as file:
    for row in file:
        tokens = row.split(',')
        time = int(float(tokens[1]))
        req = int(tokens[2])
        address = int(tokens[3])
        length = int(tokens[4])
        packet.append([time, req, address, length])  
with open('/Users/apple/Desktop/Research/Dr. NEERAJ GOEL/Logs/Wannacry3_eps.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
  
    # extracting each data row one by one
    for row in csvreader:
        eps.append(int(row[0]))


#%%
class persecond:
    def __init__(self):
        self.m0, self.m1, self.m2, self.m3, self.m4, self.m5, self.m6, self.m7, self.m8, self.m9 = ([] for i in range(10))
        self.n0, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9 = ([] for i in range(10))
        self.rps = []
        self.wps = []
        self.time = 0
        self.m = []
        
        #function for managing incoming requests
    def new_entry(self,packet):
        if packet[0] > self.time:
            self.time = self.time + 1
            self.m.append(self.time)
            self.rps.append(self.add_read())
            self.wps.append(self.add_write())
            self.delete()
            
            while self.time != packet[0]:
                self.m.append(self.time)
                self.rps.append(0)
                self.wps.append(0)
                self.time = self.time + 1
            
            
        if packet[1] == 0:
            self.new_read_entry(packet)
        else:
            self.new_write_entry(packet)
            
    def new_read_entry(self, packet):
        #defining a local list to expand every request    
            address = packet[2]
            for i in range(packet[3]):
                h = address % 10
                if h == 0:
                    if address in self.m0:
                        address = address + 1
                        continue
                    else:
                        self.m0.append(address)
                        address = address + 1
                elif h==1:
                    if address in self.m1:
                        address = address + 1
                        continue
                    else:
                        self.m1.append(address)
                        address = address + 1
                elif h==2:
                    if address in self.m2:
                        address = address + 1
                        continue
                    else:
                        self.m2.append(address)
                        address = address + 1
                elif h==3:
                    if address in self.m3:
                        address = address + 1
                        continue
                    else:
                        self.m3.append(address)
                        address = address + 1
                elif h==4:
                    if address in self.m4:
                        address = address + 1
                        continue
                    else:
                        self.m4.append(address)
                        address = address + 1
                elif h==5:
                    if address in self.m5:
                        address = address + 1
                        continue
                    else:
                        self.m5.append(address)
                        address = address + 1
                elif h==6:
                    if address in self.m6:
                        address = address + 1
                        continue
                    else:
                        self.m6.append(address)
                        address = address + 1
                elif h==7:
                    if address in self.m7:
                        address = address + 1
                        continue
                    else:
                        self.m7.append(address)
                        address = address + 1
                elif h==8:
                    if address in self.m8:
                        address = address + 1
                        continue
                    else:
                        self.m8.append(address)
                        address = address + 1
                elif h==9:
                    if address in self.m9:
                        address = address + 1
                        continue
                    else:
                        self.m9.append(address)
                        address = address + 1
    
    def new_write_entry(self, packet):
        #defining a local list to expand every request    
            address = packet[2]
            for i in range(packet[3]):
                h = address % 10
                if h == 0:
                    if address in self.n0:
                        address = address + 1
                        continue
                    else:
                        self.n0.append(address)
                        address = address + 1
                    
                elif h==1:
                    if address in self.n1:
                        address = address + 1
                        continue
                    else:
                        self.n1.append(address)
                        address = address + 1
                    
                elif h==2:
                    if address in self.n2:
                        address = address + 1
                        continue
                    else:
                        self.n2.append(address)
                        address = address + 1
                elif h==3:
                    if address in self.n3:
                        address = address + 1
                        continue
                    else:
                        self.n3.append(address)
                        address = address + 1
                elif h==4:
                    if address in self.n4:
                        address = address + 1
                        continue
                    else:
                        self.n4.append(address)
                        address = address + 1
                elif h==5:
                    if address in self.n5:
                        address = address + 1
                        continue
                    else:
                        self.n5.append(address)
                        address = address + 1
                elif h==6:
                    if address in self.n6:
                        address = address + 1
                        continue
                    else:
                        self.n6.append(address)
                        address = address + 1
                elif h==7:
                    if address in self.n7:
                        address = address + 1
                        continue
                    else:
                        self.n7.append(address)
                        address = address + 1
                elif h==8:
                    if address in self.n8:
                        address = address + 1
                        continue
                    else:
                        self.n8.append(address)
                        address = address + 1
                elif h==9:
                    if address in self.n9:
                        address = address + 1
                        continue
                    else:
                        self.n9.append(address)
                        address = address + 1
                        
                  
                
                
    def add_read(self):
        l = len(self.m0) + len(self.m1) + len(self.m2) + len(self.m3) + len(self.m4) + len(self.m5) + len(self.m6) + len(self.m7) + len(self.m8) + len(self.m9) 
        return l
    def add_write(self):
        l = len(self.n0) + len(self.n1) + len(self.n2) + len(self.n3) + len(self.n4) + len(self.n5) + len(self.n6) + len(self.n7) + len(self.n8) + len(self.n9) 
        return l
    def delete(self):
        self.m0.clear()
        self.m1.clear()
        self.m2.clear()
        self.m3.clear()
        self.m4.clear()
        self.m5.clear()
        self.m6.clear()
        self.m7.clear()
        self.m8.clear()
        self.m9.clear()
        self.n0.clear()
        self.n1.clear()
        self.n2.clear()
        self.n3.clear()
        self.n4.clear()
        self.n5.clear()
        self.n6.clear()
        self.n7.clear()
        self.n8.clear()
        self.n9.clear()
ani = persecond()
for i in range(len(packet)):
    print(i)
    row = packet[i]
    ani.new_entry(row)

#%% Plotting read addresses
from operator import truediv
import numpy as np
import matplotlib.pyplot as plt
plt.plot(ani.m,ani.rps)
plt.title("Read addresses")
plt.xlabel("Time in sec.")
plt.ylabel("Read Adresses")
#%% Plotting write I/O
plt.plot(ani.m,ani.wps)
plt.title("Write addresses")
plt.xlabel("Time in sec.")
plt.ylabel("Write Adresses")
#%% Plotting erasure I/O
plt.plot(ani.m,eps)
plt.title("Erasure I/O for 10 sec")
plt.xlabel("Time in sec.")
plt.ylabel("Erasure addresses")
#%% Plotting eps/write addresses
new_write = []
for i in range(len(ani.wps)):
    if ani.wps[i]==0:
        new_write.append(1)
    else:
        new_write.append(ani.wps[i])
eps_over_write = list(map(truediv, eps, new_write))
plt.plot(ani.m,eps_over_write)
plt.title("Fraction EPS/Write")
plt.xlabel("Time in sec.")
plt.ylabel("Fraction value")
#%% Plotting eps/total addresses
new_read = []
for i in range(len(ani.rps)):
    if ani.rps[i]==0:
        new_read.append(1)
    else:
        new_read.append(ani.rps[i])
total = np.add(new_read,new_write)
eps_over_total = list(map(truediv, eps, total))
plt.plot(ani.m,eps_over_total)
plt.title("Fraction EPS/total")
plt.xlabel("Time in sec.")
plt.ylabel("Fraction value")
#%% Plotting accumulatied write addresses
acc_write = []
acc_write.append(0)
for i in range(1,len(ani.wps)):
    acc_write.append(acc_write[i-1]+ ani.wps[i])
plt.plot(ani.m,acc_write)
plt.title("Accumulated Writes per second")
plt.xlabel("Time in sec.")
plt.ylabel("Acc. Writes")   
#%% Plotting slope of writes
write_slope = []
write_slope.append(0)
sum = 0
for i in range(1,len(ani.wps)):
    sum = ani.wps[i-1] + sum
    avg = sum/i
    write_slope.append(ani.wps[i-1]/(avg+1))
plt.plot(ani.m,write_slope)
plt.title("Slope of write addresses")
plt.xlabel("Time in sec.")
plt.ylabel("Write addresses")   