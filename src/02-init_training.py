#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import random as rm
import networkx as nx

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1=['100','95','90','85']
l2=['ppi','reg','met','int']
l3=['babu','butland']
l4=['deg','bet','jc','complete']
l5=['cold','mix']
l6=['csv']


################################################

def readlist(c):
	f_pairs = open(folder + c +".tab")
	header - f_pairs.readline();
	dic_pairs = {} #dictionary of gene pairs
	for line in f_pairs:
		d = line.split()
		dic_pairs[(d[0],d[1])]=float(d[2])
	f_pairs.close()

dic_pairs_babu = readlist(l1[0])
dic_pairs_butland = readlist(l1[1])

#################################################




for a in l1: #['100','95','90','85']
	#define the sub-network percentage
	p = float(a)/100

	for b in l2: #['ppi','reg','met','int']
		#read interaction file, shuffle, keep it in a list
		l_int = [] #interaction list
		fint = open(folder+b+".tab")
		for line in fint:
			d = line.split()
			l_int.append((d[0],d[1]))
		rm.shuffle(l_int)
		#take only a percetage
		size = len(l_int)
		last = int(p*size)
		l_int = l_int[0:last] #replace list with only percentage
			#Build network
		G = None
		if b == "reg" or b == "met":
			G = nx.DiGraph()
		else:
			G = nx.Graph()
		for elem in l_int:
			G.add_edge(elem[0],elem[1])

		dic_deg = G.degree()
		dic_bet = nx.algorithms.centrality.betweenness_centrality(G)
		dic_jc_babu = {}
		dic_jc_butland = {}

		for c in l3: #['babu','butland']
			if c == "babu":
				for p in dic_pairs_babu:
					try:
						dic_jc_babu[p]=nx.jaccard_coefficient(G, [p[0], p[1]])
					except:
						print a,b,c,"  __jaccard"

				for d in l4:   #['deg','bet','jc','complete']
					output=[]
					if d == "deg":
						output.append("gene1,gene2,degree,score\n")
						for pa in dic_pairs_babu









			else:
				for p in dic_pairs_butland:
					try:
						dic_jc_butland[p]=nx.jaccard_coefficient(G, [p[0], p[1]])
					except:
						print a,b,c,"  __jaccard"


















