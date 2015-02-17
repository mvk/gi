# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################

import os
import sys
from threading import Thread

finput = open("config.txt")
folder = finput.readline().rstrip("\n")
wekalocation = finput.readline().rstrip('\n')

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['babu', 'butland']
l4 = ['deg', 'bet', 'complete']
l5 = ['cold', 'mix']
l6 = ['csv']


def weka(path):
	if not os.path.exists(path+"csv/"+file.replace("csv","arff")):
		command = "java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+path+ "csv/" + file + " -o "+ path + "arff/" + file.replace('csv','arff')
		os.system(command)
	else:
		print "arff exists"

# Convert csv to arff
for a in l1:
	for b in l2:
		for c in l3:
			for d in l4:
				for e in l5:
					path = (folder+'%s/%s/%s/%s/%s/' % (a, b, c, d, e))
					lista_files = os.listdir(path + 'csv/')
					thr = []
					for file in lista_files:
						threadweka = Thread(target=weka, args=([path]))
						thr.append(threadweka)
					[x.start() for x in thr]
					[x.join() for x in thr]
				print d
			print c
		print b




