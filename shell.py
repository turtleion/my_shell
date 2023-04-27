import os
import sys
import commandhandler


class Shell:
    def __init__(self):
        self.initstatus = False
        self.comhan = commandhandler.CommandHandler()
        # Start initialitation
        self.history = []
    def exit(self):
        # Save history
        try:
            with open("history.bck", "w") as f:
                for i in self.history:
                    f.writelines(i)
                    
                f.close()
        except (FileExistsError, FileNotFoundError) as f:
            print("Unknown error")
            pass
        exit(2)
    def issempty(self, vval):
        if len(vval) == 0 or vval.isspace():
            return True
        else:
            return False

    def shell(self):
        os.system("cls")

        while True:
            try:
                a = input('> ')
                raw = a.split(" ")
                cmd = raw[0]
                raw.pop(0)
                arguments = raw[:]
                if self.issempty(a):
                    continue
                self.history.append(a)
                
                out = self.comhan.run_commands(a.split(" ")[0], arguments)

            except ValueError:
                print('not ok')
            except KeyboardInterrupt:
                print("Exiting...")
                self.exit()


shell = Shell()
shell.shell()
