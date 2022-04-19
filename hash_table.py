
from record import EmployeeRecord
from typing import List

class HashTable:
    def __init__(self, size):
        #self.size = self.get_required_size(size) 
        self.size = int(size+0.4*size)
        self.data:List[EmployeeRecord] = [None]*self.size

    def insert(self, record: EmployeeRecord):
        slot = self.find_empty(record.ID)
        self.data[slot] = record
    
    def get(self, recordId):
        slot = self.find_record(recordId)
        if slot is not None:
            return self.data[slot]
        else:
            return None

    def delete(self,record:EmployeeRecord):
        slot = self.find_record(record)
        if slot is not None:
            self.data[slot] = None


    def hash(self, recordId):
        return recordId%self.size
    
    def probe(self,recordId,i):
        return (self.hash(recordId)+i**2)%self.size
    
    def find_empty(self,key):
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
            if self.data[i].ID == key:
                break
            i = self.probe(key,j)
            j+=1
        if self.data[i]==None:
            return None
        else:
            return i
    
    def get_required_size(self, size):
        double_size = size*2
        def isPrime(num):
            prime =1
            x = num-1
            while x>1:
                if x%num==0:
                    prime = 0
                    break
                x-=1
            return prime
        next_prime = double_size+1
        while not isPrime(next_prime):
            next_prime+=1
        return next_prime