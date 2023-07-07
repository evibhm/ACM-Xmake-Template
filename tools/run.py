if __name__ == "__main__":
    import os
    import sys
    from subprocess import call
    
    if len(sys.argv) < 3:
        print("Error: <python run scripts> not enough arguments")
        sys.exit(1)

    _, obj, dirname = sys.argv

    inpath = os.path.join(dirname, "in")
    outpath = os.path.join(dirname, "out")
    anspath = os.path.join(dirname, "ans")

    if not os.path.exists(inpath):
        print("Error: <python run scripts> input file not found")
        sys.exit(1)

    if not os.path.exists(anspath):
        print("Error: <python run scripts> answer file not found")
        sys.exit(1)

    if not os.path.exists(outpath):
        os.mkdir(outpath)

    for infile in os.listdir(inpath):
        if not infile.endswith(".in"):
            continue

        outfile = infile.replace(".in", ".out")
        ansfile = infile.replace(".in", ".ans")

        if not os.path.exists(os.path.join(anspath, ansfile)):
            print("Error: <python run scripts> answer file not found")
            sys.exit(1)

        fin = open(os.path.join(inpath, infile), "r")
        fout = open(os.path.join(outpath, outfile), "w")
        call(obj,stdin=fin, stdout=fout)

        with open(os.path.join(outpath, outfile), "r") as f:
            out = f.read()

        with open(os.path.join(anspath, ansfile), "r") as f:
            ans = f.read()

        if out.split() != ans.split():
            print("Error: <python run scripts> {} and {} not match".format(outfile, ansfile))
            sys.exit(1)

    print("Success: <python run scripts> all testcases passed")
    