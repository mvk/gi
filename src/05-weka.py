#!/usr/bin/env python
# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################

import os
import sys
import subprocess

finput = open("config.txt")
folder = finput.readline().rstrip("\n")
wekalocation = finput.readline().rstrip('\n')

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['babu', 'butland']
l4 = ['deg', 'bet', 'complete']
l5 = ['cold', 'mix']
l6 = ['csv']

end = 2


def run_cmd_with_system(wekalocation, path, fpath):
    command = "java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+path+ "csv/" + fpath + " -o "+ path + "arff/" + file.replace('csv','arff')
    os.system(command)


def run_cmd_with_popen(wekalocation, path, fpath):
    command_arr = [
        "java -cp",
        wekalocation,
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

convert()

