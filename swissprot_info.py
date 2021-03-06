import csv
import re
import tqdm

print("Reading...")
testfile = "The path to your TXT file"
file = open (testfile, "r").read()


def rem (sym):
    sym=str(sym).replace("[","")
    sym=sym.replace("]","")
    sym=sym.replace("'","")
    return sym


with open ("The path to your new-created CSV file","w") as output:
    datawriter = csv.writer(output,delimiter=',')
    header = ["Protein ID","Protein Name","Organism",
            "Gene Name","Gene ID","EC","Keywords","Cellular component GO",
            "Molecular function GO","Biological process GO",
            "Chromosome component","NCBI TaxID(Taxonomic identifier)","Subcellular location anno",
            "Function anno","Catalytic activity anno","Cofactor anno",
            "Pathway anno","Subunit anno","Similarity anno(Family)",
            "Diease anno","PTM anno","Tissue Specificity anno",
            "Developmental stage anno","Induction Anno","Sequence"]
    datawriter.writerow(header)

    file_delhttp = file.replace("https://","")
    file_delhttp = file_delhttp.replace("http://","")
    print("Splitting...")
    files = file_delhttp.split("//\n")

    for i in tqdm.tqdm(files):

        #1 Protein ID
        pid = []
        test = re.findall(r"A.\nAC   \w+;",i)
        pid = str(test).replace(r"A.\nAC   ","")
        pid = pid.replace(";","")
        # print(pid)

        #2 Protein Name
        proteinname = []
        test = re.findall("DE   RecName: Full=+.*", i)
        test = str(test).replace("DE   RecName: Full=","")
        test = test.replace(";","")
        if "{" in test:
            proteinname = re.sub("{.*}","",test)
        else:
            proteinname = test
        # print(proteinname)

        #3 Organism
        organism = []
        test = re.findall("OS   .*", i)
        organism = str(test).replace(".","")
        organism = organism.replace("OS   ","")
        # print(organism)

        #4 Gene Name
        genename= []
        test = re.findall("GN   .*?Name.*?=.*?;",i) 
        test = re.sub(r"GN.*=","",str(test))
        test = test.replace(";","")
        if "{" in test:
            genename = re.sub("{.*?}","",test)
        else:
            genename = test
        # print(genename)

        #5 Gene ID
        gid = []
        test = re.findall("DR   GeneID;.*;",i)
        gid = str(test).replace("DR   GeneID; ","")
        gid = gid.replace(";","")
        # print(gid)

        #6 EC
        ec = []
        test = re.findall(r"DE.*EC=.*;",i)
        test = re.sub(r"DE\s+EC=","",str(test))
        test = test.replace(";","")
        test = test.replace(" ","")        
        if "{" in test:
            ec = re.sub(r"{.*?}","",test)
        else:
            ec = test
        # print(ec)

        #7 Keywords
        kw = []
        test = re.findall(r"KW   .*",i)
        kw = str(test).replace("KW   ","")
        # print(kw)

        #8 Cellular component GO
        locgo = []
        test = re.findall("GO.*; C:.*;",i)
        locgo = re.sub(r"GO; GO:\d*; C:","",str(test))
        locgo = locgo.replace(";","")
        # print(locgo)

        #9 Molecular function GO
        mfgo = []
        test = re.findall("GO.*; F:.*;",i)
        mfgo = re.sub(r"GO; GO:\d*; F:","",str(test))
        mfgo = mfgo.replace(";","")
        # print(mfgo)

        #10 Biological process GO
        bpgo = []
        test = re.findall("GO.*; P:.*;",i)
        bpgo = re.sub(r"GO; GO:\d*; P:","",str(test))
        bpgo = bpgo.replace(";","")
        # print(bpgo)

        #11 Chromosome component
        chroco = []
        test = re.findall("Chromosome.*",i)
        chroco = test
        # print(chroco)

        #12 NCBI TaxID(Taxonomic identifier)
        taxid = []
        test = re.findall("NCBI_TaxID=.*;",i)
        test = str(test).replace("NCBI_TaxID=","")
        test = test.replace(";","")
        if "{" in test:
            taxid = re.sub("{.*?}","",test)
        else:
            taxid = test
        # print(taxid)

        #13 Subcellular location anno
        sublocanno =[]
        test = i.split("-!-")
        test = re.findall(r"SUBCELLULAR LOCATION:[\s\S]*?\.",str(test))
        test = str(test).replace("CC","")
        test= str(test).replace(r"\\n ","")
        test = test.replace(".","")
        test = re.sub(r"(  )+"," ",test)
        test = str(test).replace("SUBCELLULAR LOCATION: ","")
        if "{" in test:
            sublocanno = re.sub("{.*?}","",test)
        else:
            sublocanno = test
        # print(sublocanno)

        #14 Function anno
        fanno = []
        test = i.split("!-")
        test = re.findall(r"FUNCTION:[\s\S]*?CC   \-",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = test.replace(" -","")
        test = re.sub(r"(  )+"," ",test)
        test = test.replace("FUNCTION: ","")
        if "{" in test:
            fanno = re.sub("{.*?}\. ","",test)
        else:
            fanno = test
        # print(fanno)

        #15 Catalytic activity anno
        caanno = []
        test = i.split("-!-")
        test = re.findall(r"Reaction=[\s\S]*?;",str(test))
        test = str(test).replace("CC","")
        test= str(test).replace(r"\\n ","")
        test = re.sub(r"(  )+"," ",test)
        caanno = test.replace(";","")
        caanno = caanno.replace("Reaction=","")
        # print(caanno)

        #16 Cofactor anno
        cofanno = []
        test = i.split("-!-")
        test = re.findall(r"COFACTOR[\s\S]*?Name=[\s\S]*?;",str(test))
        test = str(test).replace("COFACTOR:","")
        test = str(test).replace("CC","")
        test= str(test).replace(r"\\n ","")
        test = re.sub(r"(  )+"," ",test)
        test = test.replace("Name=","")
        cofanno = test.replace(";","")
        # print(cofanno)

        #17 Pathway anno
        pathanno = []
        test = i.split("!-")
        test = re.findall(r"PATHWAY:[\s\S]*?CC   \-",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = test.replace(" -","")
        test = test.replace("PATHWAY: ","")
        test = re.sub(r"(  )+"," ",test)
        if "{" in test:
            pathanno = re.sub(r"{.*?}\. ","",test)
        else:
            pathanno = test
        # print(pathanno)

        #18 Subunit anno
        subanno =[]
        test = i.split("!-")
        test = re.findall(r"SUBUNIT:[\s\S]*?CC   \-",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = test.replace(" -","")
        test = test.replace("SUBUNIT: ","")
        test = re.sub(r"(  )+"," ",test)
        if "{" in test:
            subanno = re.sub(r"{.*?}\. ","",test)
        else:
            subanno = test
        # print(subanno)

        #19 Similarity anno(Family)
        simanno =[]
        test = i.split("!-")
        test = re.findall(r"SIMILARITY:[\s\S]*?CC   \-",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = test.replace(" -","") 
        test = re.sub(r"(  )+"," ",test)
        test = test.replace("SIMILARITY: ","")
        if "{" in test:
            simanno = re.sub(r"{.*?}\. ","",test)
        else:
            simanno = test
        # print(simanno)

        #20 Diease anno
        dianno = []
        test = i.split("-!-")
        test = re.findall(r"DISEASE:[\s\S]*?\[",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")   
        test = re.sub(r"(  )+"," ",test)
        test = str(test).replace("DISEASE: ","")
        test = test.replace(" [","")
        if "{" in test:
            dianno = re.sub(r"{.*?}\. ","",test)
        else:
            dianno = test        
        # print(dianno)

        #21 PTM anno
        ptmanno =[]
        test = i.split("!-")
        test = re.findall(r"PTM:[\s\S]*?CC   \-",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = test.replace(" -","") 
        test = re.sub(r"(  )+"," ",test)
        test = test.replace("PTM: ","")
        if "{" in test:
            ptmanno = re.sub(r"{.*?}\. ","",test)
        else:
            ptmanno = test
        # print(ptmanno)

        #22 Tissue Specificity anno
        tsanno =[]
        test = i.split("-!-")
        test = re.findall(r"TISSUE SPECIFICITY:[\s\S]*?\.",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = re.sub(r"(  )+"," ",test)
        test = test.replace("TISSUE SPECIFICITY: ","")
        test = test.replace(".","")
        tsanno = test  
        # print(tsanno)


        #23 Developmental stage anno
        dsanno =[]
        test = i.split("-!-")
        test = re.findall(r"DEVELOPMENTAL STAGE:[\s\S]*?\.",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = re.sub(r"(  )+"," ",test)
        dsanno = test.replace("DEVELOPMENTAL STAGE: ","")
        # print(dsanno)

        #24 Induction Anno
        inanno =[]
        test = i.split("!-")
        test = re.findall(r"INDUCTION:[\s\S]*?CC   \-",str(test))
        test = str(test).replace("CC","")
        test = str(test).replace(r"\\n ","")
        test = test.replace(" -","") 
        test = re.sub(r"(  )+"," ",test)
        test = test.replace("INDUCTION: ","")
        if "{" in test:
            inanno = re.sub(r"{.*?}\. ","",test)
        else:
            inanno = test
        # print(inanno)  



        #25 Sequence
        seq =[]
        test = re.findall(r"SQ   SEQUENCE[\s\S]*",i)
        test = re.sub("SQ.*;","",str(test))
        test = test.replace(r"\n","")
        seq = re.sub(r" +","",test)
        # print(seq)

        



        datawriter.writerow([rem(pid),rem(proteinname),rem(organism),
                            rem(genename),rem(gid),rem(ec),rem(kw),rem(locgo),
                            rem(mfgo),rem(bpgo),rem(chroco),rem(taxid),rem(sublocanno),
                            rem(fanno),rem(caanno),rem(cofanno),rem(pathanno),rem(subanno),
                            rem(simanno),rem(dianno),rem(ptmanno),rem(tsanno),
                            rem(dsanno),rem(inanno),rem(seq)])

