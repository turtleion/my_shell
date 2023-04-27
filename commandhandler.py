import os
import metadata_parser
import subprocess


class CommandHandler:
    def __init__(self):
        # Define the basic information
        self.version = "1.0"
        self.cmd_path = "commands/"
        # if "CMD_SHELL_PATHe" in os.environ():
        #     self.cmd_path = os.getenv("CMD_SHELL_PATHe")
        cmds = os.listdir(self.cmd_path)
        if len(cmds) == 0:
            print("No commands were loaded")
            exit(2)

        # Get all metadata of the commands
        self.command = {}
        # commands = {
        #     alias: get-from-metadata
        #     arguments-needed: get-from-metadata
        #     base-file: get-from-metadata known as init file
        # }

        for i in cmds:
            m_source = self.cmd_path+i+"/"+i+".metadata"
            if os.path.isfile(m_source):

                # Read the metadata
                with open(m_source) as f:
                    parser = metadata_parser.MetadataParser(f)
                    if len(parser.debug_fail()) != 0:
                        print(parser.debug_fail())
                        pass
                    try:
                        parser = parser.get_metadata()
                        self.command[parser["usage"]] = {
                            "name": parser["name"], "arguments": parser["args"], "init": parser["init"]}
                    except KeyError:
                        print("Failed loading keys")

    def run_commands(self, commands, arguments: list=[]):
        # Check if the commands are available
        if commands not in self.command.keys():
            # print(self.command.keys())
            print("Command with name: "+commands+" has not found")
            return (False, "cmd_notfound")
        # Check the arguments
        if self.command[commands]["arguments"] is None:
            self.command[commands]["arguments"] = []
        if not self.command[commands]["arguments"] == [] and len(arguments) == 0 or len(self.command[commands]["arguments"]) > len(arguments):
            print("Arguments needed!\n")
            for i in self.command[commands]["arguments"]:
                print(i[0] + ": " + i[1])
            print(str(len(arguments)) + " found")
            return (False, "argue_notcomplete")
        # Check the base commands and start executing it
        # print("commands/"+self.command[commands]["init"])
        if os.path.isfile("commands/"+self.command[commands]["init"]):
            try:
                # Change the env variable
                env = os.environ.copy()
                env["PYTHONUSERBASE"] = os.getcwd()+"/commands"+";"+env["PYTHONUSERBASE"]
                d = subprocess.run(
                    "python3 commands/"+self.command[commands]["init"]+" "+str(arguments).replace("[", "").replace("]", "")+" "+os.getcwd(), shell=True, env=env)
            except (subprocess.CalledProcessError, subprocess.SubprocessError) as e:
                print("Failed executing the commands : "+str(e))
                return (False, "process_call_err")
