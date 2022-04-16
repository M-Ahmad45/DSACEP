
def read_file(filename):
    data = dict()
    with open(filename,"r") as file:
        file.readline()
        file.readline()
        for record in file.readlines():
            print(record.split("\t"))

read_file("./data/data_100.txt")
