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

end = 101

#cold uses training and test manualy
def metacold(path):
	for i in range(1,end):
		test = path+'cold/arff/'+str(i)+'_test.arff'
		train =path+'cold/arff/'+str(i)+'_train.arff'
		result =path+'cold/result/'+str(i)+'.txt'
		os.system('java -cp '+wekalocation+' -Xmx4000m weka.classifiers.meta.Vote \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.REPTree -- -M 2 -V 0.0010 -N 3 -S 1 -L -1" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.NBTree" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.RandomTree -- -K 1 -M 1.0 -S 1" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.RandomForest -- -I 10 -K 0 -S 1" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.J48 -- -C 0.5 -M 32"\
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.BFTree -- -S 1 -M 32 -N 5 -C 1.0 -P POSTPRUNED"\
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.ADTree --\
	-B 25 -E -2" -R AVG -t '+train+' -T '+test+' -i > '+result)


#mix does Weka cross-validation
def metamix(path):
	for i in range(1,end):
		train =path+'mix/arff/'+str(i)+'.arff'
		result =path+'mix/result/'+str(i)+'.txt'
		os.system('java -cp '+wekalocation+' -Xmx4000m weka.classifiers.meta.Vote \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.REPTree -- -M 2 -V 0.0010 -N 3 -S 1 -L -1" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.NBTree" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.RandomTree -- -K 1 -M 1.0 -S 1" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.RandomForest -- -I 10 -K 0 -S 1" \
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.J48 -- -C 0.5 -M 32"\
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.BFTree -- -S 1 -M 32 -N 5 -C 1.0 -P POSTPRUNED"\
	-B "weka.classifiers.meta.Bagging -P 100 -I 20 -W weka.classifiers.trees.ADTree --\
	-B 25 -E -2" -R AVG -t '+train+' -i > '+result)




#Runs everything
for a in l1:
	for b in l2:
		for c in l3:
			for d in l4:
				path = (folder+'%s/%s/%s/%s/' % (a, b, c, d))
				#threadmetacold = Thread(target=metacold, args=([path]))
				#threadmetacold.start()
				threadmetamix = Thread(target=metamix, args=([path]))
				threadmetamix.start()




