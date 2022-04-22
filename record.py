from sys import getsizeof
class EmployeeRecord:
    def __init__(self,ID,name,city,cat):
        self.ID = int(ID)
        self.name = name
        self.city = city
        self.cat = cat
    def __sizeof__(self):
        return getsizeof(self.ID)+ getsizeof(self.name) + getsizeof(self.city) + getsizeof(self.cat)
