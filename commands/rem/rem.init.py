import shutil
import sys
import os

class Remove:
    def __init__(self, path):
        if not os.path.exists(path):
            print("Cannot remove dest, dest no exist")
            exit(2)
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
        except shutil.Error as err:
            print("Cannot remove the dest, error on internal programs\nEE_STATUS:"+str(err))

# Process arguments
try:
    if len(sys.argv) < 2:
        print("NO ARGUMENTS FOUND")
    else:
        os.chdir(sys.argv[-1])
        # print(os.getcwd())
        # shutil.copy2(src.replace("'","").replace(",",""), dest.replace("'",""))
        print(sys.argv[1])
        src = os.getcwd()+"/"+sys.argv[1].replace("'","").replace(",","")
        Remove(src)        
except Exception as e:
    print(e)