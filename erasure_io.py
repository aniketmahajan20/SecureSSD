import csv
irp = {}
packet = []
time1 = []
with open('/Users/apple/Desktop/Research/Dr. NEERAJ GOEL/Logs/WannaCry3.csv', 'r') as file:
    for row in file:
        tokens = row.split(',')
        time = int(float(tokens[1]))
        req = int(tokens[2])
        address = int(tokens[3])
        length = int(tokens[4])
        packet.append([time, req, address, length])  
        
#%%

class persecond:
    def __init__(self):
        self.m0, self.m1, self.m2, self.m3, self.m4, self.m5, self.m6, self.m7, self.m8, self.m9 = ([] for i in range(10))
        self.n0, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9 = ([] for i in range(10))

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
                    
    def new_erasure_entry(self,packet):
            address = packet[2]
            flag = 0
            for i in range(packet[3]):
                h = address % 10
                if h == 0:
                    if address in ani0.m0 or address in ani1.m0 or address in ani2.m0 or address in ani3.m0 or address in ani4.m0 or address in ani5.m0 or address in ani6.m0 or address in ani7.m0 or address in ani8.m0 or address in ani9.m0:
                        if address in self.n0:
                            address = address + 1
                            continue
                        else:
                            self.n0.append(address)
                            address = address + 1
                elif h==1:
                    if address in ani0.m1 or address in ani1.m1 or address in ani2.m1 or address in ani3.m1 or address in ani4.m1 or address in ani5.m1 or address in ani6.m1 or address in ani7.m1 or address in ani8.m1 or address in ani9.m1:
                        if address in self.n1:
                            address = address + 1
                            continue
                        else:
                            self.n1.append(address)
                            address = address + 1
                elif h==2:
                    if address in ani0.m2 or address in ani1.m2 or address in ani2.m2 or address in ani3.m2 or address in ani4.m2 or address in ani5.m2 or address in ani6.m2 or address in ani7.m2 or address in ani8.m2 or address in ani9.m2:
                        if address in self.n2:
                            address = address + 1
                            continue
                        else:
                            self.n2.append(address)
                            address = address + 1
                elif h==3:
                    if address in ani0.m3 or address in ani1.m3 or address in ani2.m3 or address in ani3.m3 or address in ani4.m3 or address in ani5.m3 or address in ani6.m3 or address in ani7.m3 or address in ani8.m3 or address in ani9.m3:
                        if address in self.n3:
                            address = address + 1
                            continue
                        else:
                            self.n3.append(address)
                            address = address + 1
                elif h==4:
                   if address in ani0.m4 or address in ani1.m4 or address in ani2.m4 or address in ani3.m4 or address in ani4.m4 or address in ani5.m4 or address in ani6.m4 or address in ani7.m4 or address in ani8.m4 or address in ani9.m4:
                        if address in self.n4:
                            address = address + 1
                            continue
                        else:
                            self.n4.append(address)
                            address = address + 1
                elif h==5:
                    if address in ani0.m5 or address in ani1.m5 or address in ani2.m5 or address in ani3.m5 or address in ani4.m5 or address in ani5.m5 or address in ani6.m5 or address in ani7.m5 or address in ani8.m5 or address in ani9.m5:
                        if address in self.n5:
                            address = address + 1
                            continue
                        else:
                            self.n5.append(address)
                            address = address + 1
                elif h==6:
                    if address in ani0.m6 or address in ani1.m6 or address in ani2.m6 or address in ani3.m6 or address in ani4.m6 or address in ani5.m6 or address in ani6.m6 or address in ani7.m6 or address in ani8.m6 or address in ani9.m6:
                        if address in self.n6:
                            address = address + 1
                            continue
                        else:
                            self.n6.append(address)
                            address = address + 1
                elif h==7:
                    if address in ani0.m7 or address in ani1.m7 or address in ani2.m7 or address in ani3.m7 or address in ani4.m7 or address in ani5.m7 or address in ani6.m7 or address in ani7.m7 or address in ani8.m7 or address in ani9.m7:
                        if address in self.n7:
                            address = address + 1
                            continue
                        else:
                            self.n7.append(address)
                            address = address + 1
                elif h==8:
                   if address in ani0.m8 or address in ani1.m8 or address in ani2.m8 or address in ani3.m8 or address in ani4.m8 or address in ani5.m8 or address in ani6.m8 or address in ani7.m8 or address in ani8.m8 or address in ani9.m8:
                        if address in self.n8:
                            address = address + 1
                            continue
                        else:
                            self.n8.append(address)
                            address = address + 1
                else:
                    if address in ani0.m9 or address in ani1.m9 or address in ani2.m9 or address in ani3.m9 or address in ani4.m9 or address in ani5.m9 or address in ani6.m9 or address in ani7.m9 or address in ani8.m9 or address in ani9.m9:
                        if address in self.n9:
                            address = address + 1
                            continue
                        else:
                            self.n9.append(address)
                            address = address + 1
                
    def add_read(self):
        l = len(self.m0)+len(self.m1)+len(self.m2)+len(self.m3)+len(self.m4)+len(self.m5)+len(self.m6)+len(self.m7)+len(self.m8)+len(self.m9) 
        return l
    def add_erasure(self):
        l = len(self.n0)+len(self.n1)+len(self.n2)+len(self.n3)+len(self.n4)+len(self.n5)+len(self.n6)+len(self.n7)+len(self.n8)+len(self.n9) 
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


ani0 = persecond()
ani1 = persecond()
ani2 = persecond()
ani3 = persecond()
ani4 = persecond()
ani5 = persecond()
ani6 = persecond()
ani7 = persecond()
ani8 = persecond()
ani9 = persecond()
rps = []
eps = []
time = 0
m = []
for i in range(len(packet)):
    print(i)
    row = packet[i]
    if row[0] > time:
          time = time + 1
          m.append(time)
          if time % 10 == 0:
              ani0.delete()
          elif time % 10 == 1:
              ani1.delete()
          elif time % 10 == 2:
              ani2.delete()
          elif time % 10 == 3:
              ani3.delete()
          elif time % 10 == 4:
              ani4.delete()
          elif time % 10 == 5:
              ani5.delete()
          elif time % 10 == 6:
              ani6.delete()
          elif time % 10 == 7:
              ani7.delete()
          elif time % 10 == 8:
              ani8.delete()
          else:
              ani9.delete()
          rps.append(ani0.add_read() + ani1.add_read() + ani2.add_read() + ani3.add_read() + ani4.add_read() + ani5.add_read() + ani6.add_read() + ani7.add_read() + ani8.add_read() + ani9.add_read( ))
          eps.append(ani0.add_erasure() + ani1.add_erasure() + ani2.add_erasure() + ani3.add_erasure() + ani4.add_erasure() + ani5.add_erasure() + ani6.add_erasure() + ani7.add_erasure() + ani8.add_erasure() + ani9.add_erasure())
          while time != row[0]:
              m.append(time)
              rps.append(0)
              eps.append(0)
              time = time + 1
          

    if time % 10 == 0:
        if row[1] == 0:
            ani0.new_read_entry(row)
        else:
            ani0.new_erasure_entry(row)
    elif time % 10 == 1:
        if row[1] == 0:
            ani1.new_read_entry(row)
        else:
            ani1.new_erasure_entry(row)
    elif time % 10 == 2:
        if row[1] == 0:
            ani2.new_read_entry(row)
        else:
            ani2.new_erasure_entry(row)
    elif time % 10 == 3:
        if row[1] == 0:
            ani3.new_read_entry(row)
        else:
            ani3.new_erasure_entry(row)
    elif time % 10 == 4:
        if row[1] == 0:
            ani4.new_read_entry(row)
        else:
            ani4.new_erasure_entry(row)
    elif time % 10 == 5:
        if row[1] == 0:
            ani5.new_read_entry(row)
        else:
            ani5.new_erasure_entry(row)
    elif time % 10 == 6:
        if row[1] == 0:
            ani6.new_read_entry(row)
        else:
            ani6.new_erasure_entry(row)
    elif time % 10 == 7:
        if row[1] == 0:
            ani7.new_read_entry(row)
        else:
            ani7.new_erasure_entry(row)
    elif time % 10 == 8:
        if row[1] == 0:
            ani8.new_read_entry(row)
        else:
            ani8.new_erasure_entry(row)
    else:
        if row[1] == 0:
            ani9.new_read_entry(row)
        else:
            ani9.new_erasure_entry(row)
          

    

#%%
#plotting erasure I/o
from operator import truediv
import numpy as np
import matplotlib.pyplot as plt
plt.plot(m,eps)
plt.title("Erasure I/O in last ten sconds")
plt.xlabel("Time in sec.")
plt.ylabel("Erasure addresses")