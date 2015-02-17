#!/usr/bin/env python
# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################

import os
import sys
import subprocess
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


def run_cmd_with_system(weka_jar, path, fpath):
    command = "java -cp "+weka_jar+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+path+ "csv/" + fpath + " -o "+ path + "arff/" + fpath.replace('csv','arff')
    os.system(command)


def run_cmd_with_popen(weka_jar, path, fpath):
    command_arr = [
        "java -cp",
        weka_jar,
        "weka.filters.unsupervised.attribute.Remove",
        "-R 1,2",
        "-i", os.path.join(path, "csv", fpath),
        "-o", os.path.join(path, "arff", fpath.replace('csv','arff'))
    ]
    proc = subprocess.Popen(
        command_arr,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return proc.communicate()

def weka(path, f, weka_jar):
    trg = os.path.join(path, "csv", f.replace("csv","arff"))
    if os.path.exists(trg):
        print("arff exists")
        return 0

    return run_cmd_with_popen(
        weka_jar,
        f,
        trg
    )

# Convert csv to arff
def convert():
    print '***********CONVERTING FROM CSV TO ARFF - remove gene1 and gene2 attributes\n'
    results = []
    for a in l1:
        for b in l2:
            for c in l3:
                for d in l4:
                    for e in l5:
                        path = (folder+'%s/%s/%s/%s/%s/' % (a, b, c, d, e))
                        lista_files = os.listdir(path + 'csv/')
                        for fpath in lista_files:
                            res = run_cmd_with_popen(wekalocation, path, fpath)
                            results.append(res.returncode)
                        threadweka = Thread(target=weka, args=([fpath]))
                        thr.append(threadweka)
    [x.start() for x in thr]
    [x.join() for x in thr]

convert()



