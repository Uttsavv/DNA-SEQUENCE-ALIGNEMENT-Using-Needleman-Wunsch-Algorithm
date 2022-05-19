from alignerFunctions import *
from menuFunctions import * 


while(True):
	os.system('cls')

	seq1,seq2 = mainMenu()

	seqs = os.listdir('sequences')

	firstSeqPath = 'sequences/'+seqs[seq1-1]
	secondSeqPath = 'sequences/'+seqs[seq2-1]


	seq1 = open(firstSeqPath,"r").readline()
	seq2 = open(secondSeqPath,"r").readline()



	print('\n Sequences Before Alignment :- \n')
	print(f' Sequence 1 : {seq1}\n')
	print(f' Sequence 2 : {seq2}\n')
	print_alignment(seq1,seq2, alignmentMatrix(seq1, seq2))
	input("\n Press Enter to return to Main Menu...")

