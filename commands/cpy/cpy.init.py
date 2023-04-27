import os
import shutil
import sys
class Copy:
    def get_result(self) -> tuple:
        return self.result
    def __init__(self, path, dest):
        self.result = ()
        path = path.replace("'","")
        if os.path.isfile(path) and os.path.isdir(dest):
            if os.path.exists(dest):
                try:
                    shutil.copy2(path, dest)
                    if os.path.exists(path) and os.path.exists(dest):
                        self.result = (True, "no_result")
                except shutil.Error as e:
                    print("Copy error : "+ str(e))
                    self.result = (False, "e_fail_copy")
            else:
                print("Copy error, destination not exist")
                self.result = (False, "e_dest_noexist")
        else:
            print(path+":"+dest)
            print("Copy error, invalid destination or source path")
            self.result = (False, "e_destorsrc_nofound")
     
# Process arguments
try:
    if len(sys.argv) < 3:
        print("NO ARGUMENTS FOUND")
    else:
        os.chdir(sys.argv[-1])
        # print(os.getcwd())
        # shutil.copy2(src.replace("'","").replace(",",""), dest.replace("'",""))
        
        src = os.getcwd()+"/"+sys.argv[1].replace("'","").replace(",","")
        dest = os.getcwd()+"/"+sys.argv[2].replace("'","")
        Copy(src, dest)        
except Exception as e:
    print(e)