import imp
sysinf = imp.load_source("sysinfo","../sysinfo.py")
class ApplicationAPI:
    def __init__(self):
        print("ApplicationAPI prototype v1")

    def get_system_version(self):
        print("")