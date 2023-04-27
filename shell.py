import os
import sys
import commandhandler


class Shell:
    def __init__(self):
        self.initstatus = False
        self.comhan = commandhandler.CommandHandler()
        # Start initialitation

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
                out = self.comhan.run_commands(a.split(" ")[0], arguments)

            except ValueError:
                print('not ok')
            except KeyboardInterrupt:
                print("Exiting...")
                exit(2)


shell = Shell()
shell.shell()
