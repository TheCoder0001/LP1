frames = int(input("Enter number of frames: "))
ref_str = list(map(int, input("Enter reference string (space-separated): ").strip().split()))

n = len(ref_str)
frame = [-1] * frames
time = [0] * frames
faults = 0
hits = 0
lru_index = ()*frames

print("LRU PAGE")
print(f"{'Step':<6} {'Ref':<6} {'Frames':<25} {'Status':<10} {'Faults':<6}")

for i in range(n):
    page = ref_str[i]
    hit = False
    
    if page in frame:
        hits += 1
        hit = True
        time[frame.index(page)] = i
    else:
        faults += 1
        if -1 in frame:
            idx = frame.index(-1)
            frame[idx] = page
            time[idx] = i
        else:
            lru_idx = time.index(min(time))
            frame[lru_idx] = page
            time[lru_idx] = i
    
    frame_state = " | ".join([str(x) if x != -1 else "-" for x in frame])
    status = "HIT" if hit else "FAULT"
    
    print(f"{i+1:<6} {page:<6} {frame_state:<25} {status:<10} {faults:<6}")

print(f"Total Page Faults : {faults}")
print(f"Total Hits        : {hits}")
print(f"Page Fault Ratio  : {faults/n:.3f}")
print(f"Hit Ratio         : {hits/n:.3f}")