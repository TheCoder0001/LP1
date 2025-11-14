MDT = []
MNT = {}
program = [
"        START   200",
"        MACRO",
"        INCR    &X,&Y",
"        LOAD    =1",
"        ADD     &X",
"        STORE   &Y",
"        MEND",
"        MACRO",
"        DECR    &A",
"        LOAD    &A",
"        SUB     =1",
"        STORE   &A",
"        MEND",
"        MAIN    START",
"        INCR    DATA1,DATA2",
"        DECR    COUNT",
"        INCR    VAL1,VAL2",
"        END"
]

mdt_ptr = 0
in_macro = False
macro_name = ""
params = []

for line in program:
    line = line.strip()
    if not line:
        continue
    tokens = line.split()
    op = tokens[0]
    if op == "MACRO":
        in_macro = True
        continue
    if op == "MEND":
        in_macro = False
        macro_name = ""
        params = []
        continue
    if in_macro:
        if macro_name == "":
            macro_name = tokens[0]
            param_str = tokens[1]
            params = [p.lstrip('&') for p in param_str.split(',')]
            MNT[macro_name] = [mdt_ptr, len(params)]
        MDT.append(line)
        mdt_ptr += 1
    else:
        if op in MNT:
            args = tokens[1].split(',')
            for i in range(MNT[op][1]):
                pass

print("Macro Name Table (MNT):")
print("Name\tIndex\tParams")
for name in MNT:
    print(name, "\t", MNT[name][0], "\t", MNT[name][1])

print("\nMacro Definition Table (MDT):")
for i in range(len(MDT)):
    print(i, ":", MDT[i])