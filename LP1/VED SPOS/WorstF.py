n = int(input("Enter number of memory blocks: "))
blocks = []
print("Enter size of each block:")
for i in range(n):
    while True:
        try:
            size = int(input(f"Block {i+1}: ").strip())
            if size > 0:
                blocks.append([size, False, ""])
                break
            else:
                print("Size must be > 0!")
        except:
            print("Enter a valid number!")

m = int(input("\nEnter number of processes: "))
processes = []
print("Enter size of each process:")
for i in range(m):
    while True:
        try:
            size = int(input(f"Process P{i+1}: ").strip())
            if size > 0:
                processes.append([f"P{i+1}", size, -1])  
                break
            else:
                print("Size must be > 0!")
        except:
            print("Enter a valid number!")

for proc in processes:
    worst_idx = -1
    worst_size = -1
    for i in range(n):
        if not blocks[i][1] and blocks[i][0] >= proc[1] and blocks[i][0] > worst_size:
            worst_size = blocks[i][0]
            worst_idx = i
    if worst_idx != -1:
        blocks[worst_idx][1] = True
        blocks[worst_idx][2] = proc[0]
        proc[2] = worst_idx

print("WORST FIT MEMORY ALLOCATION")
print(f"{'Block':<8} {'Size':<10} {'Status':<12} {'Process':<10} {'Fragment':<10}")
total_internal = 0
total_external = 0
for i in range(n):
    size = blocks[i][0]
    status = "Allocated" if blocks[i][1] else "Free"
    proc_name = blocks[i][2] if blocks[i][1] else "-"
    frag = 0
    if blocks[i][1]:
        proc_size = next(p[1] for p in processes if p[2] == i)
        frag = size - proc_size
        total_internal += frag
    else:
        total_external += size
    frag_str = str(frag) if blocks[i][1] else ""
    print(f"{i+1:<8} {size:<10} {status:<12} {proc_name:<10} {frag_str:<10}")
print(f"Total Internal Fragmentation : {total_internal}")
print(f"Total External Fragmentation : {total_external}")

print("\nProcess Allocation Table:")
print(f"{'Process':<10} {'Size':<10} {'Block':<10} {'Status'}")
for p in processes:
    block_no = p[2] + 1 if p[2] != -1 else "None"
    status = "Allocated" if p[2] != -1 else "Not Allocated"
    print(f"{p[0]:<10} {p[1]:<10} {block_no:<10} {status}")