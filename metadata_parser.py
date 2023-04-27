import inspect
import os


class MetadataParser:
    # metadata_content : a byte of metadata file, usually after metadata reader then goes here
    def __init__(self, metadata_content):
        # if not inspect.isclass(metadata_content):
        #     exit(2)

        # $> METADATA START
        # name Akustik
        # usage akus
        # version 1
        # author Agus Efendi
        # init akustik.init.py
        # $> METADATA ENDS

        # Read the bytes
        contents = []
        self.metadata = {}
        self.load_fails = []
        call_started = False
        hasEnded = False
        name = None
        version = None
        usage = None
        arguments = None
        author = None
        init = None
        attemps = 0
        COMMANDS_DIR = "commands/"
        for content in metadata_content.readlines():
            con = content.replace("\n", "")
            print(con)

            if con.strip().startswith("$>"):
                raw = con.split(" ")
                if len(raw) == 0:
                    pass
                try:
                    # Check if the commands is correct
                    # $ ([0]) METADATA ([1]) START|ENDS ([2])
                    subject = raw[1]
                    status = raw[2]
                    if subject == "metadata" and status == "start":
                        call_started = True
                        continue
                    elif subject == "metadata" and status == "ends":
                        hasEnded = True
                        if name == None or author == None or version == None or usage == None:
                            print(
                                "Missing values in a keys, registering value again\nAttemps: "+str(attemps+1))
                            break
                        # Pack all to one variable
                        self.metadata = {"name": name, "version": version,
                                         "author": author, "usage": usage, "args": arguments, "init": init}
                        break
                except IndexError:
                    self.load_fails.append((True, "Invalid file type!"))
                    break

            # Parse name, and other information

            if con.startswith("name "):

                raw = con.split(" ")
                try:
                    name = raw[1]
                except IndexError:
                    self.load_fails.append((True,
                                           "No name of the commands, INVALID PACKAGE STACK"))
                    break
                # If the registrating of this value, we need to skip
                continue

            if con.startswith("version "):
                raw = con.split(" ")
                try:
                    version = raw[1]
                except IndexError:
                    self.load_fails.append((True,
                                           "No version of the commands, default version is: 1"))
                    version = 1
                    pass
                continue

            if con.startswith("usage "):
                raw = con.split(" ")
                try:
                    usage = raw[1]
                except IndexError:
                    self.load_fails.append((True,
                                           "No usage of the commands, INVALID PACKAGE STACK"))
                    break
                continue

            if con.startswith("author "):
                raw = con.split(" ")
                try:
                    author = raw[1]

                except IndexError:
                    self.load_fails.append((True,
                                           "No author defined, used John Doe/Jane Doe instead"))
                    author = "John Doe / Jane Doe"
                    pass
                continue

            if con.startswith("init "):

                raw = con.split(" ")
                try:
                    init = raw[1]
                    if os.path.isfile(COMMANDS_DIR+init):
                        pass
                    else:
                        self.load_fails.append(
                            (False, "Invalid init file location / invalid init file"))

                except IndexError:
                    self.load_fails.append((False,
                                           "There is no init file [IGNORE]"))
                    init = ""
                    pass

                continue

            if con.startswith("arguments "):
                raw = con.split(" ")

                try:

                    # arguments (name)(tag1 / :)(desc)(endoftag1 / ;) (space)
                    # ,space for delimiter

                    # Sort the name first
                    tags = 0
                    before_tags = -1
                    arguments = []
                    tmp = 1
                    tmp2 = None
                    for i in raw:
                        if tmp == 1:
                            tmp = 0
                            continue
                    # before_tags : one value behind the tags
                    # tags : used to process arguments

                    # Same tags : (desc) ;
                        if before_tags != tags and (tags - before_tags) == 1:
                            # Load description
                            if i.strip().endswith(";"):
                                arguments.append(
                                    (tmp2, i.replace(":", "").replace(";", "").replace("-", " ")))

                                # print(arguments)
                        if i.strip().endswith(":"):
                            # TAG 1
                            tmp2 = i.replace(":", "")
                            tags += 1
                            before_tags += 1
                            continue

                except Exception:
                    print("E")

    def get_metadata(self): return self.metadata
    def debug_fail(self): return self.load_fails
# test unit

