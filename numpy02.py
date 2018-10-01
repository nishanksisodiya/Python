import numpy as np
import numpy.matrixlib as ml
def main():
    l1=list()
    for i in range(3):
        l1.append(list())
        for j in range(3):
            if(i==j):
                l1[i].append(1)
            else:
                l1[i].append(0)
    m1=ml.matrix(l1)
    print(m1)

main()
