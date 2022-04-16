from record import EmployeeRecord
from typing import List
def read_file(filename):
    data:List[EmployeeRecord] = []
    with open(filename,"r") as file:
        file.readline()
        file.readline()
        for record in file.readlines():
            rec = EmployeeRecord(*record.split("\t"))
            data.append(rec)
    return data

print(read_file("./data/data_10.txt"))
