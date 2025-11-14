MDT = [
"INCR    &X,&Y",
"LOAD    =1",
"ADD     &X",
"STORE   &Y",
"DECR    &A",
"LOAD    &A",
"SUB     =1",
"STORE   &A"
]

MNT = {
"INCR": [0, 2],
"DECR": [4, 1]
}

intermediate_code = [
"        START   200",
"        MAIN    START",
"        INCR    DATA1,DATA2",
"        DECR    COUNT",
"        INCR    VAL1,VAL2",
"        END"
]

expanded = []

for line in intermediate_code:
    line = line.strip()
    if not line:
        expanded.append("")
        continue
    tokens = line.split()
    op = tokens[0]
    if op in MNT:
        start_idx = MNT[op][0]
        param_cnt = MNT[op][1]
        actual_args = tokens[1].split(',')
        ala = {}
        mdt_line_idx = start_idx
        header_processed = False
        while mdt_line_idx < len(MDT):
            current_mdt_line = MDT[mdt_line_idx]
            mdt_tokens = current_mdt_line.split()
            if not header_processed:
                formal_params = [p.lstrip('&') for p in mdt_tokens[1].split(',')]
                for i in range(param_cnt):
                    ala[formal_params[i]] = actual_args[i]
                header_processed = True
                mdt_line_idx += 1
                continue
            expanded_line = current_mdt_line
            for param in ala:
                expanded_line = expanded_line.replace("&" + param, ala[param])
            expanded.append(expanded_line)
            mdt_line_idx += 1
            if mdt_tokens[0] == "MEND":
                break
    else:
        expanded.append(line)

print("Final Expanded Code:")
for x in expanded:
    print(x)