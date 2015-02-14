# ################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import random as rm

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['babu','butland']
l4 = ['deg', 'bet', 'complete']
l5 = ['cold/training', 'cold/test', 'mix']
l6 = ['csv']

for a in l1:
    for b in l2:
        for c in l3:
            for d in l4:
                path = ('%s/%s/%s/%s/' % (a, b, c, d))
                fcomplete = open(folder+path+"training.csv") #sai 3 csvs daqui
                head_complete = fcomplete.readline()

                l_agg = []
                l_all = []

                for line in fcomplete:
                    d = line.split(",")
                    score = d[-1].rstrip()
                    if float(score) < 0:
                        l_agg.append(line.replace(score,"AGG"))
                    else:
                        l_all.append(line.replace(score,"ALL"))

                rm.shuffle(l_agg)
                rm.shuffle(l_all)

                dicagg={}
                dicall={}

                for elem in l_agg:
                    dicagg[elem[0:12]]=[elem]

                for elem in l_all:
                    dicall[elem[0:12]]=[elem]

                s1 = len(dicagg)
                s2 = len(dicall)


                print "lindo"


