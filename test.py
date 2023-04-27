tags = 0
raw = "arguments kku: Best-intheworld; humankind: kakau;".split(" ")
before_tags = -1
args = []
tmp = 1
tmp2 = None
for i in raw:
    if tmp == 1:
        tmp = 0
        continue
    # before_tags : one value behind the tags
    # tags : used to process args

    # Same tags : (desc) ;
    if before_tags != tags and (tags - before_tags) == 1:
        # Load description
        if i.strip().endswith(";"):
            args.append((tmp2, i.replace(":",
                                         "").replace(";", "").replace("-", " ")))

            print(args)
    if i.strip().endswith(":"):
        # TAG 1
        tmp2 = i.replace(":", "")
        tags += 1
        before_tags += 1
        continue
