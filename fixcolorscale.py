#!/usr/bin/env python2
finaloutput =''
with open('ironbowscale') as f:
    line = f.readline()
    while line:
	ironbow = line.split(',')
        length = len(ironbow)
        length = length - 1
#        print(length)
        increment = 1.0 / length
#        print(increment)
        for idx, val in enumerate(ironbow):
            value = idx*increment
            output = '[' + str(value) + ', ' + str(val) + '], '
            finaloutput+=output
        break
    print(finaloutput)
    print('Out of loop.')
#   print('length =' + str(length))
