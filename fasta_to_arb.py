import os
import string
from Bio import SeqIO
input_file = raw_input('Path to file (/Users/g/..): ')
path = input_file[0:string.rfind(input_file,'/')+1]
name = input_file[string.rfind(input_file,'/')+1:string.rfind(input_file,'.')]
os.chdir(path)
out_name = name + "_arb.fasta"
output_file=open(out_name, "w")
for seq_record in SeqIO.parse(input_file, "fasta"):
    seq=str(seq_record.seq)
    seq_cropped = seq.strip("-")
    first = seq_cropped[0]  #First character that isn't "-"
    last = seq_cropped[-1]  #Last character that isn't "-"
    first_index = seq.find(first) #Position of first in original sequence
    last_index =seq.rfind(last)  #Position of last in original sequence
    seq_arb="."*first_index+seq_cropped+"."*(len(seq)-last_index-1)  #make final sequence adding the "." back in place of the "-"
    output_file.write(">")
    output_file.write(seq_record.id)
    output_file.write("\n")
    output_file.write(seq_arb)
    output_file.write("\n")
