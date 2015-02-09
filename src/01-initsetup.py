#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

def makedir(namedir):
	if not os.path.exists(namedir):
		os.makedirs(namedir)

#Levels

l1=['ppi','reg','met','int']
l2=['deg','bet','jc','complete']
l3=['100','95','90','85']
l4=['19-20','39']
l5=['csv']


for a in l1:
    for b in l2:
        for c in l3:
            for d in l4:
                for e in l5:
                    path =('%s/%s/%s/%s/%s' %(a,b,c,d,e))
                    makedir(folder+path)


