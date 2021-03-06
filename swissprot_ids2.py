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
    header = ["Protein ID","eggNOG","GeneTree","HOGENOM","InParanoid",
            "OMA","PhylomeDB","TreeFam","BRENDA",
            "PathwayCommons","Reactome","SignaLink","SIGNOR",
            "BioGRID-ORCS","ChiTaRS","EvolutionaryTrace","GeneWiki",
            "GenomeRNAi","Pharos","PRO",
            "Proteomes","RNAct","Bgee",
            "ExpressionAtlas","Genevisible","CDD","Gene3D","IDEAL",
            "InterPro","PANTHER","Pfam","PRINTS",
            "SMART","SUPFAM","PROSITE","OrthoDB","BioCyc",
            "TIGRFAMs"]
    datawriter.writerow(header)

    file_delhttp = file.replace("https://","")
    file_delhttp = file_delhttp.replace("http://","")
    print("Splitting...")
    files = file_delhttp.split("//\n")

    for i in tqdm.tqdm(files):

        #Protein ID
        pid = []
        test = re.findall(r"A.\nAC   \w+;",i)
        pid = str(test).replace(r"A.\nAC   ","")
        pid = pid.replace(";","")

        # print(pid)

        #1 eggNOG IDs
        eggnog = []
        test = re.findall("DR   eggNOG;.*",i)
        eggnog = str(test).replace("DR   eggNOG; ","")
        # print(eggnog)

        #2 GeneTree IDs
        genetree = []
        test = re.findall("DR   GeneTree;.*",i)
        genetree = str(test).replace("DR   GeneTree; ","")
        # print(genetree)

        #3 HOGENOM IDs
        hogenom =[]
        test = re.findall("DR   HOGENOM;.*",i)
        hogenom = str(test).replace("DR   HOGENOM; ","")
        # print(hogenom) 

        #4 InParanoid IDs
        inparanoid =[]
        test = re.findall("DR   InParanoid;.*",i)
        inparanoid = str(test).replace("DR   InParanoid; ","")
        # print(inparanoid)

        #5 OMA IDs
        oma =[]
        test = re.findall("DR   OMA;.*",i)
        oma = str(test).replace("DR   OMA; ","")
        # print(oma)

        #6 PhylomeDB IDs
        phylome = []
        test = re.findall("DR   PhylomeDB;.*",i)
        phylome = str(test).replace("DR   PhylomeDB; ","")
        # print(phylome)

        #7 TreeFam IDs
        treefam = []
        test = re.findall("DR   TreeFam;.*",i)
        treefam = str(test).replace("DR   TreeFam; ","")
        # print(treefam)

        #8 BRENDA IDs
        brenda = []
        test = re.findall("DR   BRENDA;.*",i)
        brenda = str(test).replace("DR   BRENDA; ","")
        # print(brenda)

        #9 PathwayCommons IDs
        pathwaycom = []
        test = re.findall("DR   PathwayCommons;.*",i)
        pathwaycom = str(test).replace("DR   PathwayCommons; ","")
        # print(pathwaycom)

        #10 Reactome IDs
        reatome = []
        test = re.findall("DR   Reactome;.*",i)
        reatome = str(test).replace("DR   Reactome; ","")
        # print(reatome)

        #11 SignaLink IDs
        signalink = []
        test = re.findall("DR   SignaLink;.*",i)
        signalink = str(test).replace("DR   SignaLink; ","")
        # print(signalink)

        #12 SIGNOR IDs
        signor = []
        test = re.findall("DR   SIGNOR;.*",i)
        signor = str(test).replace("DR   SIGNOR; ","")
        # print(signor)

        #13 BioGRID-ORCS IDs
        bioorc = []
        test = re.findall("DR   BioGRID-ORCS;.*",i)
        bioorc = str(test).replace("DR   BioGRID-ORCS; ","")
        # print(bioorc)

        #14 ChiTaRS IDs
        chitar = []
        test = re.findall("DR   ChiTaRS;.*",i)
        chitar = str(test).replace("DR   ChiTaRS; ","")
        # print(chitar)

        #15 EvolutionaryTrace IDs
        evotrace = []
        test = re.findall("DR   EvolutionaryTrace;.*",i)
        evotrace = str(test).replace("DR   EvolutionaryTrace; ","")
        # print(evotrace)

        #16 GeneWiki IDs
        genewiki =[]
        test = re.findall("DR   GeneWiki;.*",i)
        genewiki = str(test).replace("DR   GeneWiki; ","")
        # print(genewiki)

        #17 GenomeRNAi IDs
        genrna = []
        test = re.findall("DR   GenomeRNAi;.*",i)
        genrna = str(test).replace("DR   GenomeRNAi; ","")
        # print(genrna)

        #18 Pharos IDs
        pharo =[]
        test = re.findall("DR   Pharos;.*",i)
        pharo = str(test).replace("DR   Pharos; ","")
        # print(pharo)

        #19 PRO IDs
        pro = []
        test = re.findall("DR   PRO;.*",i)
        pro = str(test).replace("DR   PRO; ","")
        # print(pro)

        #20 Proteomes IDs
        promes =[]
        test = re.findall("DR   Proteomes;.*",i)
        promes = str(test).replace("DR   Proteomes; ","")
        # print(promes)

        #21 RNAct IDs
        rnact = []
        test = re.findall("DR   RNAct;.*",i)
        rnact = str(test).replace("DR   RNAct; ","")
        # print(rnact)

        #22 Bgee IDs
        bgee = []
        test = re.findall("DR   Bgee;.*",i)
        bgee = str(test).replace("DR   Bgee; ","")
        # print(bgee)

        #23 ExpressionAtlas IDs
        expat = []
        test = re.findall("DR   ExpressionAtlas;.*",i)
        expat = str(test).replace("DR   ExpressionAtlas; ","")
        # print(expat)

        #24 Genevisible IDs
        genble = []
        test = re.findall("DR   Genevisible;.*",i)
        genble = str(test).replace("DR   Genevisible; ","")
        # print(genble)

        #25 CDD IDs
        cdd = []
        test = re.findall("DR   CDD;.*",i)
        cdd = str(test).replace("DR   CDD; ","")
        # print(cdd)  

        #26 Gene3D IDs
        gen3d = []
        test = re.findall("DR   Gene3D;.*",i)
        gen3d = str(test).replace("DR   Gene3D; ","")
        # print(gen3d)

        #27 IDEAL IDs
        ideal = []
        test = re.findall("DR   IDEAL;.*",i)
        ideal = str(test).replace("DR   IDEAL; ","")
        # print(ideal)        
 
        #28 InterPro IDs
        interpro = []
        test = re.findall("DR   InterPro;.*",i)
        interpro = str(test).replace("DR   InterPro; ","")
        # print(interpro)          
        
        #29 PANTHER IDs
        panther = []
        test = re.findall("DR   PANTHER;.*",i)
        panther = str(test).replace("DR   PANTHER; ","")
        # print(panther)          

        #30 Pfam IDs
        pfam = []
        test = re.findall("DR   Pfam;.*",i)
        pfam = str(test).replace("DR   Pfam; ","")
        # print(pfam)          

        #31 PRINTS IDs
        prints = []
        test = re.findall("DR   PRINTS;.*",i)
        prints = str(test).replace("DR   PRINTS; ","")
        # print(prints)          

        #32 SMART IDs
        smart = []
        test = re.findall("DR   SMART;.*",i)
        smart = str(test).replace("DR   SMART; ","")
        # print(smart)          

        #33 SUPFAM IDs
        supfam = []
        test = re.findall("DR   SUPFAM;.*",i)
        supfam = str(test).replace("DR   SUPFAM; ","")
        # print(supfam)          

        #34 PROSITE IDs
        prosite = []
        test = re.findall("DR   PROSITE;.*",i)
        prosite = str(test).replace("DR   PROSITE; ","")
        # print(prosite)          
        #************************************
        #35 OrthoDB IDs
        otherdb = []
        test = re.findall("DR   OrthoDB;.*",i)
        otherdb = str(test).replace("DR   OrthoDB; ","")
        # print(otherdb)          

        #36 BioCyc IDs
        biocyc = []
        test = re.findall("DR   BioCyc;.*",i)
        biocyc = str(test).replace("DR   BioCyc; ","")
        # print(biocyc)          

        #37 TIGRFAMs IDs
        tigrfam = []
        test = re.findall("DR   TIGRFAMs;.*",i)
        tigrfam = str(test).replace("DR   TIGRFAMs; ","")
        # print(tigrfam)          

        

        datawriter.writerow([rem(pid),rem(eggnog),rem(genetree),rem(hogenom),rem(inparanoid),
                            rem(oma),rem(phylome),rem(treefam),rem(brenda),
                            rem(pathwaycom),rem(reatome),rem(signalink),rem(signor),
                            rem(bioorc),rem(chitar),rem(evotrace),rem(genewiki),
                            rem(genrna),rem(pharo),rem(pro),
                            rem(promes),rem(rnact),rem(bgee),
                            rem(expat),rem(genble),rem(cdd),rem(gen3d),rem(ideal),
                            rem(interpro),rem(panther),rem(pfam),rem(prints),
                            rem(smart),rem(supfam),rem(prosite),rem(otherdb),rem(biocyc),
                            rem(tigrfam)])













        
