import os
class SysShell():
    def __init__(self):
        self.version = "1.0"
        self.name = "OKUS SHELL"
        self.base_ = "shell.py"
        self.commands_ = "commands/"
        self.cmd_H = "commandhandler.py"
        
    def clear_shell(self) -> None:
        os.system("cls")
        
    def get_shell_history(self) -> list:
        history = []
        try:
            with open("history.bck","r") as f:
                history = f.readlines()
                
            return history
        except FileNotFoundError:
            print("No history was found")
            return []