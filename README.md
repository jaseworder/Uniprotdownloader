# Uniprotdownloader
Get the Uniprot(Swissprot) data(information and cross-link IDs) and convert into a csv file. Convert the fasta file(swissprot,trembl,uniref90) into csv file.

You can get swissprot data through this **easy** program. It could be useful for someone. **This is only for my preliminary study, don't laugh at me, please:)**

1. Download the original data from https://www.uniprot.org/downloads .Reviewed (Swiss-Prot) text format for info and other ids ,fasta format for sequences.(If you download the txt file, you would get a dat format file, you can change it into txt format.)

2. The swissprot_info.py file could put the information into a csv file for further study. Information included "Protein ID","Protein Name","Organism","Gene Name","Gene ID","EC","Keywords","Cellular component GO","Molecular function GO","Biological process GO","Chromosome component" and more.

3. The swissprot_ids1/2.py are for the cross-link ids from other databases.

4. The ...fastatocsv.py are for convert the fasta file you download in to csv files.
