n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    print(f"--- Process P{i+1} ---")
    at = int(input("Enter arrival time: "))
    bt = int(input("Enter burst time: "))
    processes.append([f"P{i+1}", at, bt, bt])  # [name, AT, BT, remaining]

quantum = int(input("\nEnter time quantum: "))

wt = [0] * n
tat = [0] * n
ct = [0] * n
time = 0
complete = 0
gantt = []
queue = []

while complete != n:
    for i in range(n):
        if processes[i][1] <= time and processes[i][3] > 0 and i not in queue:
            queue.append(i)
    
    if not queue:
        time += 1
        continue
    
    curr = queue.pop(0)
    start_time = time
    
    if processes[curr][3] <= quantum:
        time += processes[curr][3]
        processes[curr][3] = 0
    else:
        time += quantum
        processes[curr][3] -= quantum
        queue.append(curr)
    
    gantt.append([processes[curr][0], start_time, time])
    
    if processes[curr][3] == 0:
        complete += 1
        ct[curr] = time
        tat[curr] = ct[curr] - processes[curr][1]
        wt[curr] = tat[curr] - processes[curr][2]

print("\nGantt Chart:")
print("  ", end="")
for block in gantt:
    print(f"| {block[0]} ({block[1]}-{block[2]}) ", end="")
print("|\n")

print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    p = processes[i]
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")