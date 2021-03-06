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
    header = ["Protein ID","EMBL","CCDS","PIR","RefSeq",
            "PDB","PDBsum","BMRB","SMR",
            "BioGRID","CORUM","DIP","IntAct",
            "MINT","STRING","BindingDB","ChEMBL",
            "DrugBank","DrugCentral","GuidetoPHARMACOLOGY",
            "MoonDB","iPTMnet","PhosphoSitePlus",
            "BioMuta","DMDM","CPTAC","EPD","jPOST",
            "MassIVE","MaxQB","PaxDb","PeptideAtlas",
            "PRIDE","ProteomicsDB","Antibodypedia","DNASU",
            "Ensembl","GeneID","KEGG","UCSC","CTD",
            "DisGeNET","EuPathDB","GeneCards","GeneReviews","HGNC","HPA",
            "MalaCards","MIM","neXtProt","OpenTargets",
            "Orphanet","PharmGKB"]
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

        #1 EMBL IDs
        embl = []
        test = re.findall("DR   EMBL;.*",i)
        embl = str(test).replace("DR   EMBL; ","")
        # print(emblid)

        #2 CCDS IDs
        ccds = []
        test = re.findall("DR   CCDS;.*",i)
        ccds = str(test).replace("DR   CCDS; ","")
        # print(ccdsid)

        #3 PIR IDs
        pir =[]
        test = re.findall("DR   PIR;.*",i)
        pir = str(test).replace("DR   PIR; ","")
        # print(pirid) 

        #4 RefSeq IDs
        refseq =[]
        test = re.findall("DR   RefSeq;.*",i)
        refseq = str(test).replace("DR   RefSeq; ","")
        # print(refseqid)

        #5 PDB IDs
        pdb =[]
        test = re.findall("DR   PDB;.*",i)
        pdb = str(test).replace("DR   PDB; ","")
        # print(pdbis)

        #6 PDBsum IDs
        pdbsum = []
        test = re.findall("DR   PDBsum;.*",i)
        pdbsum = str(test).replace("DR   PDBsum; ","")
        # print(pdbsum)

        #7 BMRB IDs
        bmrb = []
        test = re.findall("DR   BMRB;.*",i)
        bmrb = str(test).replace("DR   BMRB; ","")
        # print(bmrb)

        #8 SMR IDs
        smr = []
        test = re.findall("DR   SMR;.*",i)
        smr = str(test).replace("DR   SMR; ","")
        # print(bmrb)

        #9 BioGRID IDs
        biogrid = []
        test = re.findall("DR   BioGRID;.*",i)
        biogrid = str(test).replace("DR   BioGRID; ","")
        # print(biogrid)

        #10 CORUM IDs
        corum = []
        test = re.findall("DR   CORUM;.*",i)
        corum = str(test).replace("DR   CORUM; ","")
        # print(corum)

        #11 DIP IDs
        dip = []
        test = re.findall("DR   DIP;.*",i)
        dip = str(test).replace("DR   DIP; ","")
        # print(dip)

        #12 IntAct IDs
        inact = []
        test = re.findall("DR   IntAct;.*",i)
        inact = str(test).replace("DR   IntAct; ","")
        # print(inact)

        #13 MINT IDs
        mint = []
        test = re.findall("DR   MINT;.*",i)
        mint = str(test).replace("DR   MINT; ","")
        # print(mint)

        #14 STRING IDs
        string = []
        test = re.findall("DR   STRING;.*",i)
        string = str(test).replace("DR   STRING; ","")
        # print(string)

        #15 BindingDB IDs
        bindingdb = []
        test = re.findall("DR   BindingDB;.*",i)
        bindingdb = str(test).replace("DR   BindingDB; ","")
        # print(bindingdb)

        #16 ChEMBL IDs
        chembl =[]
        test = re.findall("DR   ChEMBL;.*",i)
        chembl = str(test).replace("DR   ChEMBL; ","")
        # print(chembl)

        #17 DrugBank IDs
        drugbank = []
        test = re.findall("DR   DrugBank;.*",i)
        drugbank = str(test).replace("DR   DrugBank; ","")
        # print(drugbank)

        #18 DrugCentral IDs
        drugcentral =[]
        test = re.findall("DR   DrugCentral;.*",i)
        drugcentral = str(test).replace("DR   DrugCentral; ","")
        # print(drugcentral)

        #19 GuidetoPHARMACOLOGY IDs
        guid = []
        test = re.findall("DR   GuidetoPHARMACOLOGY;.*",i)
        guid = str(test).replace("DR   GuidetoPHARMACOLOGY; ","")
        # print(guid)

        #20 MoonDB IDs
        moondb =[]
        test = re.findall("DR   MoonDB;.*",i)
        moondb = str(test).replace("DR   MoonDB; ","")
        # print(moondb)

        #21 iPTMnet IDs
        iptm = []
        test = re.findall("DR   iPTMnet;.*",i)
        iptm = str(test).replace("DR   iPTMnet; ","")
        # print(iptm)

        #22 PhosphoSitePlus IDs
        phsite = []
        test = re.findall("DR   PhosphoSitePlus;.*",i)
        phsite = str(test).replace("DR   PhosphoSitePlus; ","")
        # print(phsite)

        #23 BioMuta IDs
        biomuta = []
        test = re.findall("DR   BioMuta;.*",i)
        biomuta = str(test).replace("DR   BioMuta; ","")
        # print(biomuta)

        #24 DMDM IDs
        dmdm = []
        test = re.findall("DR   DMDM;.*",i)
        dmdm = str(test).replace("DR   DMDM; ","")
        # print(dmdm)

        #25 CPTAC IDs
        cptac = []
        test = re.findall("DR   CPTAC;.*",i)
        cptac = str(test).replace("DR   CPTAC; ","")
        # print(cptac)  

        #26 EPD IDs
        epd = []
        test = re.findall("DR   EPD;.*",i)
        epd = str(test).replace("DR   EPD; ","")
        # print(epd)

        #27 jPOST IDs
        jpo = []
        test = re.findall("DR   jPOST;.*",i)
        jpo = str(test).replace("DR   jPOST; ","")
        # print(jpo)        
 
        #28 MassIVE IDs
        mass = []
        test = re.findall("DR   MassIVE;.*",i)
        mass = str(test).replace("DR   MassIVE; ","")
        # print(mass)          
        
        #29 MaxQB IDs
        maxqb = []
        test = re.findall("DR   MaxQB;.*",i)
        maxqb = str(test).replace("DR   MaxQB; ","")
        # print(maxqb)          

        #30 PaxDb IDs
        paxdb = []
        test = re.findall("DR   PaxDb;.*",i)
        paxdb = str(test).replace("DR   PaxDb; ","")
        # print(paxdb)          

        #31 PeptideAtlas IDs
        peotideat = []
        test = re.findall("DR   PeptideAtlas;.*",i)
        peotideat = str(test).replace("DR   PeptideAtlas; ","")
        # print(peotideat)          

        #32 PRIDE IDs
        pride = []
        test = re.findall("DR   PRIDE;.*",i)
        pride = str(test).replace("DR   PRIDE; ","")
        # print(pride)          

        #33 ProteomicsDB IDs
        prodb = []
        test = re.findall("DR   ProteomicsDB;.*",i)
        prodb = str(test).replace("DR   ProteomicsDB; ","")
        # print(prodb)          

        #34 Antibodypedia IDs
        antypedia = []
        test = re.findall("DR   Antibodypedia;.*",i)
        antypedia = str(test).replace("DR   Antibodypedia; ","")
        # print(antypedia)          

        #35 DNASU IDs
        dnasu = []
        test = re.findall("DR   DNASU;.*",i)
        dnasu = str(test).replace("DR   DNASU; ","")
        # print(dnasu)          

        #36 Ensembl IDs
        ensembl = []
        test = re.findall("DR   Ensembl;.*",i)
        ensembl = str(test).replace("DR   Ensembl; ","")
        # print(ensembl)          

        #37 GeneID IDs
        gid = []
        test = re.findall("DR   GeneID;.*",i)
        gid = str(test).replace("DR   GeneID; ","")
        # print(gid)          

        #38 KEGG IDs
        kegg = []
        test = re.findall("DR   KEGG;.*",i)
        kegg = str(test).replace("DR   KEGG; ","")
        # print(kegg)          

        #39 UCSC IDs
        ucsc = []
        test = re.findall("DR   UCSC;.*",i)
        ucsc = str(test).replace("DR   UCSC; ","")
        # print(ucsc)          

        #40 CTD IDs
        ctd = []
        test = re.findall("DR   CTD;.*",i)
        ctd = str(test).replace("DR   CTD; ","")
        # print(ctd)          

        #41 DisGeNET IDs
        disgenet = []
        test = re.findall("DR   DisGeNET;.*",i)
        disgenet = str(test).replace("DR   DisGeNET; ","")
        # print(disgenet)          

        #42 EuPathDB IDs
        eupath = []
        test = re.findall("DR   EuPathDB;.*",i)
        eupath = str(test).replace("DR   EuPathDB; ","")
        # print(eupath)          

        #43 GeneCards IDs
        genecards = []
        test = re.findall("DR   GeneCards;.*",i)
        genecards = str(test).replace("DR   GeneCards; ","")
        # print(genecards)

        #44 GeneReviews IDs
        genereviews = []
        test = re.findall("DR   GeneReviews;.*",i)
        genereviews = str(test).replace("DR   GeneReviews; ","")
        # print(genereviews)

        #45 HGNC IDs
        hgnc = []
        test = re.findall("DR   HGNC;.*",i)
        hgnc = str(test).replace("DR   HGNC; ","")
        # print(hgnc)          

        #46 HPA IDs
        hpa = []
        test = re.findall("DR   HPA;.*",i)
        hpa = str(test).replace("DR   HPA; ","")
        # print(hpa)

        #47 MalaCards IDs
        malacards = []
        test = re.findall("DR   MalaCards;.*",i)
        malacards = str(test).replace("DR   MalaCards; ","")
        # print(malacards)          

        #48 MIM IDs
        mim = []
        test = re.findall("DR   MIM;.*",i)
        mim = str(test).replace("DR   MIM; ","")
        # print(mim)

        #49 neXtProt IDs
        nextprot = []
        test = re.findall("DR   neXtProt;.*",i)
        nextprot = str(test).replace("DR   neXtProt; ","")
        # print(nextprot)          

        #50 OpenTargets IDs
        opentargets = []
        test = re.findall("DR   OpenTargets;.*",i)
        opentargets = str(test).replace("DR   OpenTargets; ","")
        # print(opentargets)

        #51 Orphanet IDs
        orphanet = []
        test = re.findall("DR   Orphanet;.*",i)
        orphanet = str(test).replace("DR   Orphanet; ","")
        # print(orphanet)          

        #52 PharmGKB IDs
        pharmgkb = []
        test = re.findall("DR   PharmGKB;.*",i)
        pharmgkb = str(test).replace("DR   PharmGKB; ","")
        # print(pharmgkb)


        datawriter.writerow([rem(pid),rem(embl),rem(ccds),rem(pir),rem(refseq),
                            rem(pdb),rem(pdbsum),rem(bmrb),rem(smr),
                            rem(biogrid),rem(corum),rem(dip),rem(inact),
                            rem(mint),rem(string),rem(bindingdb),rem(chembl),
                            rem(drugbank),rem(drugcentral),rem(guid),
                            rem(moondb),rem(iptm),rem(phsite),
                            rem(biomuta),rem(dmdm),rem(cptac),rem(epd),rem(jpo),
                            rem(mass),rem(maxqb),rem(paxdb),rem(peotideat),
                            rem(pride),rem(prodb),rem(antypedia),rem(dnasu),
                            rem(ensembl),rem(gid),rem(kegg),rem(ucsc),rem(ctd),
                            rem(disgenet),rem(eupath),rem(genecards),rem(genereviews),rem(hgnc),rem(hpa),
                            rem(malacards),rem(mim),rem(nextprot),rem(opentargets),
                            rem(orphanet),rem(pharmgkb)])













        
