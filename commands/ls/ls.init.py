import os
import sys
import colorama
# Process the commands

try:
    if len(sys.argv) > 2:
        pass
    flags = []
    lsf = []
    hidden = []
    new_argv = sys.argv.copy()
    for i in sys.argv:
 
        if i.replace("'","").startswith("-"):
            idx = sys.argv.index("'"+i.replace("'","")+"'")
            new_argv.pop(idx)
            flags.append(i.replace("'",""))
    if os.path.isdir(new_argv[1]):
        lsf = os.listdir(new_argv[1])
    else:    
        lsf = os.listdir(".")
    for x in lsf:
        if x.startswith("."):
            idx = lsf.index(x)
            hidden.append(colorama.Fore.YELLOW+x+colorama.Style.RESET_ALL())
            lsf.pop(idx)
            # print(hidden)
    if "-a" in flags:
        lsf = hidden + lsf
    # print(lsf)
    for x in lsf:
        print(x,end=" ")
except Exception as e:
    print("WOKE\n"+str(e))