
from record import EmployeeRecord
from typing import List
from sys import getsizeof

class HashTable:
    def __init__(self, size):
        self.size = self.get_required_size(size) 
        self.data:List[EmployeeRecord] = [None]*self.size
        self._memory = getsizeof(self.data)

    def get_mem(self):
        return self._memory
    def insert(self, record: EmployeeRecord):
        slot = self.find_empty(record.ID)
        self.data[slot] = record
        self._memory+=getsizeof(record)
    
    def get(self, recordId:int):
        slot = self.find_record(recordId)
        if slot is not None:
            return self.data[slot]
        else:
            return None

    def delete(self,recordId:int):
        slot = self.find_record(recordId)
        if slot is not None:
            self._memory-=getsizeof(self.data[slot]) #exclude record memory
            self.data[slot] = -1 #deleted marker
            self._memory+=getsizeof(self.data[slot]) #add memory for marker

    def hash(self, recordId:int):
        return recordId%self.size
    
    def probe(self,recordId:int,i):
        return (self.hash(recordId)+i**2)%self.size
    
    def find_empty(self,recordId:int):
        i = self.hash(recordId)
        j = 1
        while (self.data[i]!=None and self.data[i]!=-1) and j<=self.size:
            i = self.probe(recordId,j)
            j+=1
        return i
    
    def find_record(self,recordId:int):
        i = self.hash(recordId)
        j = 1
        while j<=self.size and self.data[i]!=None:
            if self.data[i]!=-1:
                if self.data[i].ID == recordId:
                    break
            i = self.probe(recordId,j)
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
                if num%x==0:
                    prime = 0
                    break
                x-=1
            return prime
        next_prime = double_size+1
        while not isPrime(next_prime):
            next_prime+=1
        return next_prime