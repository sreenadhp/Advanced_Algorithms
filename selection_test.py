#!/usr/bin/python
# -*- coding: utf-8 -*-


from selection_det import select_det
from selection_rand import select_rand
import random
import time

if __name__ == '__main__':
    start = time.clock()
    listSize = 10000000
    index    = random.randint(0, listSize/2)
    bigList = [random.randint(0, listSize) for i in xrange(listSize)]

    print index, "time: ", (time.clock()-start)
    start = time.clock()
    print "Selection rand:", select_rand(index, bigList), "time: ", (time.clock()-start)
    start = time.clock()
    print "Selection det :", select_det(index, bigList), "time: ", (time.clock()-start)

