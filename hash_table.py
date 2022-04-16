
from record import EmployeeRecord
from typing import List

class HashTable:
    def __init__(self, size):
        self.size = size
        self.len = 0
        self.data:List[EmployeeRecord] = [None]*(size+size*0.4) #40 prcnt more space allocated

    def insert(self, record: EmployeeRecord):
        slot = self.find_empty(record)
        self.data[slot] = record
    
    def get(self, record: EmployeeRecord):
        slot = self.find_record(record)
        if slot is not None:
            return self.data[slot]
        else:
            return None

    def delete(self,record:EmployeeRecord):
        slot = self.find_record(record)
        if slot is not None:
            self.data[slot] = None


    def hash(self, record:EmployeeRecord):
        return record.ID%self.size
    
    def probe(self,record:EmployeeRecord,i):
        return (self.hash(record)+i**2)%self.size
    
    def find_empty(self,key:EmployeeRecord):
        i = self.hash(key)
        j = 1
        while (self.data[i]!=None) and j<=self.size:
            i = self.probe(key,j)
            j+=1
        return i
    
    def find_record(self,key:EmployeeRecord):
        i = self.hash(key)
        j = 1
        while j<=self.size and self.data[i]!=None:
            if self.data[i].ID == key.ID:
                break
            i = self.probe(key,j)
            j+=1
        if self.data[i]==None:
            return None
        else:
            return i