n = int(input("Enter number of memory blocks: "))
blocks = []
print("Enter size of each block:")
for i in range(n):
    size = int(input(f"Block {i+1}: "))
    blocks.append([size, False, ""]) 

m = int(input("\nEnter number of processes: "))
processes = []
print("Enter size of each process:")
for i in range(m):
    size = int(input(f"Process P{i+1}: "))
    processes.append([f"P{i+1}", size, -1]) 

for proc in processes:
    best_idx = -1
    best_size = 999999
    for i in range(n):
        if not blocks[i][1] and blocks[i][0] >= proc[1] and blocks[i][0] < best_size:
            best_size = blocks[i][0]
            best_idx = i
    if best_idx != -1:
        blocks[best_idx][1] = True
        blocks[best_idx][2] = proc[0]
        proc[2] = best_idx

print("BEST FIT MEMORY ALLOCATION")
print(f"{'Block':<8} {'Size':<8} {'Status':<12} {'Process'}")
total_frag = 0
for i in range(n):
    size = blocks[i][0]
    status = "Allocated" if blocks[i][1] else "Free"
    proc = blocks[i][2] if blocks[i][1] else "-"
    frag = 0
    if blocks[i][1]:
        allocated_proc_size = next(p[1] for p in processes if p[2] == i)
        frag = size - allocated_proc_size
        total_frag += frag
    print(f"{i+1:<8} {size:<8} {status:<12} {proc}")
    if blocks[i][1]:
        print(f"{'':<18} {'Fragment':<8} {frag}")
print(f"Total Internal Fragmentation: {total_frag}")
print(f"Total External Fragmentation: {sum(b[0] for b in blocks if not b[1])}")

print("\nProcess Allocation Table:")
print(f"{'Process':<10} {'Size':<8} {'Block Allocated'}")
for p in processes:
    block = p[2] + 1 if p[2] != -1 else "Not Allocated"
    print(f"{p[0]:<10} {p[1]:<8} {block}")
    