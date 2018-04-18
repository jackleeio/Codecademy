"""
This program does the function of DNA Analysis

Author: Jack Lee
"""
sample = ['GTA','GGG','CAC']

def read_dna(dna_file):#dna_file is a string stand for .txt document
  dna_data = ""
  with open(dna_file, "r") as f:
    for i in f:
      dna_data += i
  return dna_data

def dna_codons(dna):#add the codon from dna_data into a list where each codon are 3 letters
  codons = []
  for i in range(0, len(dna), 3):
    if i + 3 <= len(dna):
      codons.append(dna[i:i + 3])
  return codons

def match_dna(dna):# there, dna is a list
  matches = 0 
  for codon in dna:
    if codon in sample:
      matches += 1 
  return matches

def is_criminal(dna_sample): #dna_sample is the .txt document
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print("# of codon matches: %s. DNA profile matches. Continue investigation." % num_matches)
  else:
    print("# of codon matches: %s. DNA profile matches. The suspect can be set free." % num_matches)
    
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
      
