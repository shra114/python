import random
#hardware modelling in python

#outputs
counter = 0
inc     = False

def cntr ():
    global inc
    global counter
    if (inc):
        counter_next = counter+1
    else :
        counter_next = counter
    return counter_next

for clk in range(0,200):
    #print ("clk = ",clk)
    #print ("inc = ", inc)
    #print ("counter = ", counter)
    if (clk == 0): #reset
        None
    else:
        #stimulus
        inc = random.choice([True, False])#bool(random.getrandbits(1))

    #VCD dumps
    print ("#"+str(clk*10))
    #clk
    print (bin(1).replace('0b','b'),"$")

    #IOs
    print (bin(inc).replace('0b','b'),"*")
    print (bin(counter).replace('0b','b'),"(")


    #Instantiate combos
    counter_next = cntr()

    #clk
    print ("#"+str(clk*10+5))
    print (bin(0).replace('0b','b'),"$")
    counter = counter_next
