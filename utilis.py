from record import EmployeeRecord
from typing import List
from time import perf_counter
from hash_table import HashTable
from sys import getsizeof

def read_file(filename):
    data:List[EmployeeRecord] = []
    with open(filename,"r") as file:
        file.readline()
        record_count = int(file.readline())
        for record in file.readlines():
            rec = EmployeeRecord(*record.split("\t"))
            data.append(rec)
    return (data,record_count)

def timer(func):
    def inner(*args):
        t1 = perf_counter()
        func(*args)
        t2 = perf_counter()
        return t2-t1
    return inner
@timer
def insert(table:HashTable, data):
    for i in data:
        table.insert(i)

def get_keys(data:List[EmployeeRecord])->List[int]:
    keys = []
    for i in data:
        keys.append(i.ID)
    return keys

@timer
def sort_traverse(table:HashTable,data:List[EmployeeRecord],print_on=True):
    keys = get_keys(data)
    print(getsizeof(keys))
    keys.sort()
    for i in keys:
        d = table.get(i)
        if print_on:
            print(d)
@timer
def find(table:HashTable,data,print_on=True):
    for i in range(len(data)):
        if i%2==0:
            d = table.get(i)
            if print_on:
                print(d)