#make program that folds proteins in all possible ways
#start with first element, assign it coordinate 0, 0
#next element can be assigned (1, 0), (0, 1), (-1, 0), (0, -1) and so on
#after all have been assigned coordinates, count the number of h bonds

#idea for counting h bonds: remove all p's, compare first h to rest of h's to see what its bonded with

#what this will do is take in the length of a protein
#then fold each protein of that length in all possible ways, noting
#the optimal number of h-bonds for each protein, adding that optimal
#number to the running total
#then at the end divide running total by 2^numE the number of possible proteins
#this should get the average number of bonds for each optimal protein


def initFolding(numE):
	#0 is p and 1 is h
	
	#list of length numE that contains all 0's at start

def proteinFolder(protein):
	
