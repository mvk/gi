# ################################
# AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import random as rm

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['babu', 'butland']
l4 = ['deg', 'bet', 'complete']
l5 = ['cold/training', 'cold/test', 'mix']
l6 = ['csv']

for a in l1:
	for b in l2:
		for c in l3:
			for d in l4:
				path = ('%s/%s/%s/%s/' % (a, b, c, d))
				fcomplete = open(folder + path + "training.csv")  #sai 3 csvs daqui
				head_complete = fcomplete.readline()
				listacomplete = []

				for line in fcomplete:
					listacomplete.append(line)

				rm.shuffle(listacomplete)

				dic_unique = {}
				for elem in listacomplete:
					dic_unique[elem[0:12]] = elem

				l_agg = []
				l_all = []

				for v in dic_unique.values():
					d = v.split(",")
					score = d[-1].rstrip()
					if float(score) < 0:
						l_agg.append(v.replace(score, "AGG"))
					else:
						l_all.append(v.replace(score, "ALL"))

				s1 = len(l_agg)
				s2 = len(l_all)

				size = min(s1,s2)

				for i in range(100):
					output = open(folder + path+"cold/"+str(i+1)+".csv","w")
					output.write(head_complete)
					for j in range(size):
						output.write(l_agg[j])
					for j in range(size):
						output.write(l_all[j])










