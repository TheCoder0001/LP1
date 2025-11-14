n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    print(f"--- Process P{i+1} ---")
    at = int(input("Enter arrival time: "))
    bt = int(input("Enter burst time: "))
    prio = int(input("Enter priority (lower number = higher priority): "))
    processes.append([f"P{i+1}", at, bt, prio, bt])  # [name, AT, BT, priority, remaining]

wt = [0] * n
tat = [0] * n
ct = [0] * n
time = 0
complete = 0
gantt = []

while complete != n:
    ready = []
    for i in range(n):
        if processes[i][1] <= time and processes[i][4] > 0:
            ready.append(i)
    
    if not ready:
        time += 1
        continue
    
    highest_prio = min(ready, key=lambda x: processes[x][3])
    
    if not gantt or gantt[-1][0] != processes[highest_prio][0]:
        gantt.append([processes[highest_prio][0], time])
    
    exec_time = processes[highest_prio][4]
    time += exec_time
    processes[highest_prio][4] = 0
    
    ct[highest_prio] = time
    tat[highest_prio] = ct[highest_prio] - processes[highest_prio][1]
    wt[highest_prio] = tat[highest_prio] - processes[highest_prio][2]
    gantt.append([processes[highest_prio][0], time])
    complete += 1

print("\nGantt Chart:")
print("  ", end="")
for i in range(0, len(gantt), 2):
    print(f"| {gantt[i][0]} ({gantt[i][1]}) ", end="")
    if i+1 < len(gantt):
        print(f"{gantt[i+1][0]} ({gantt[i+1][1]}) ", end="")
print("|\n")

print("Process\tAT\tBT\tPrio\tCT\tTAT\tWT")
for i in range(n):
    p = processes[i]
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")