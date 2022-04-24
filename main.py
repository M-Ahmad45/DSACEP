from utilis import *

files = ["./data/data_100.txt","./data/data_1000.txt","./data/data_10000.txt","./data/data_100000.txt",
        "./data/data_1000000.txt"]

def run(file):
    data,r_count = read_file(file)
    print(f"\nNumber of records = {r_count}")
    table = HashTable(r_count)
    i_time,i_mem = insert(table,data)
    f_time,f_mem = find(table,data, False)
    s_time, s_mem = sort_traverse(table,data,False)
    d_time, d_mem = delete(table,data)
    i_mem = get_kb_mb(i_mem)
    f_mem = get_kb_mb(f_mem)
    s_mem = get_kb_mb(s_mem)
    d_mem = get_kb_mb(d_mem)
    print("{:24s}Execution Time: {:.3e}s   Memory Consumption:{:12s}".format("Insert",i_time,i_mem))
    print("{:24s}Execution Time: {:.3e}s   Memory Consumption:{:12s}".format("Find",f_time,f_mem))
    print("{:24s}Execution Time: {:.3e}s   Memory Consumption:{:12s}".format("Sorted Traversal",s_time,s_mem))
    print("{:24s}Execution Time: {:.3e}s   Memory Consumption:{:12s}".format("Delete",d_time,d_mem))
    print()
for file in files:
    run(file)