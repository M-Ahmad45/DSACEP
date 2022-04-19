from record import EmployeeRecord
from typing import List

def read_file(filename):
    data:List[EmployeeRecord] = []
    with open(filename,"r") as file:
        file.readline()
        record_count = int(file.readline())
        for record in file.readlines():
            rec = EmployeeRecord(*record.split("\t"))
            data.append(rec)
    return (data,record_count)
