n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    name = f"P{i+1}"
    at = int(input(f"Enter arrival time for {name}: "))
    bt = int(input(f"Enter burst time for {name}: "))
    processes.append([name, at, bt, bt])  # [name, AT, BT, remaining_time]

wt = [0] * n
tat = [0] * n
ct = [0] * n
time = 0
complete = 0
gantt = []

while complete != n:
    ready = []
    for i in range(n):
        if processes[i][1] <= time and processes[i][3] > 0:
            ready.append(i)
    
    if not ready:
        time += 1
        continue
    
    shortest = min(ready, key=lambda x: processes[x][3])
    
    if not gantt or gantt[-1][0] != processes[shortest][0]:
        gantt.append([processes[shortest][0], time])
    
    processes[shortest][3] -= 1
    time += 1
    
    if processes[shortest][3] == 0:
        complete += 1
        ct[shortest] = time
        tat[shortest] = ct[shortest] - processes[shortest][1]
        wt[shortest] = tat[shortest] - processes[shortest][2]
        gantt.append([processes[shortest][0], time])

print("\nGantt Chart:")
print("  ", end="")
for i in range(len(gantt)):
    if i % 2 == 0:
        print(f"| {gantt[i][0]} ({gantt[i][1]}) ", end="")
    else:
        print(f"| {gantt[i][0]} ({gantt[i][1]}) ", end="")
print("|\n")

print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    p = processes[i]
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")