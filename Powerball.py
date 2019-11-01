# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random

def powerball():
    a = random.randrange(1,60)
    b = random.randrange(1,60)
    c = random.randrange(1,60)
    d = random.randrange(1,60)
    e = random.randrange(1,60)
    pb = random.randrange(1,36)
    print "Today's numbers are "+str(a)+', '+str(b)+',', str(c)+',', str(d)+',', 'and '+str(e)+'. The Powerball number is '+str(pb)+'.'

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
