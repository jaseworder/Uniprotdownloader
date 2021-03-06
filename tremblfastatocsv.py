import csv
import re
import tqdm


def rem (sym):
    sym=str(sym).replace("[","")
    sym=sym.replace("]","")
    sym=sym.replace("'","")
    return sym
print("Reading...")
testfile = "The path to your FASTA file"
file = open (testfile, "r").read()

with open ("The path to your new-created CSV file","w") as output:
    datawriter = csv.writer(output,delimiter=',')
    header = ["Trembl ID","Sequence"]
    datawriter.writerow(header)

    print("Splitting...")
    files = file.split(">")
    del files[0]
    for i in tqdm.tqdm(files):
        
        pid = []
        pid = re.findall(r"tr\|\S*",i)


        seq = []
        testseq = re.findall(r"\n[\s\S]*",i)
        seq = str(testseq).replace(r"\n","")


        datawriter.writerow([rem(pid),rem(seq)])
        
