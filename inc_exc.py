#! /usr/bin/env python

import math
from matplotlib import pyplot
#from decimal import Decimal

#A Za joint.

"""Problem Statement:
i socks are tossed independently at n gaping sock-eating crocodile maws 
(sockodile), each maw is equally attractive to socks, and hence equally 
likely to be hit.

How many socks must a person toss until there is a 50% probability that 
each sockodile has eaten at least one sock?

The compound event that at least one sockodile has eaten 0 socks on the ith 
toss is the union of the events for particular sockodiles.
I.E."Sockodile A ate 0" OR "Sockodile B ate 0" OR... (where OR is INCLUSIVE).

I call this Union: HUNGRYCROC  (recall sockodiles are crocodiles)

If all of the sockodiles have eaten at least one sock then the event
HUNGRYCROC is not current. I call this FULLCROCS.  FULLCROCS, and
HUNGRYCROC form a partition of the outcome space, that is either one or the
other is true.

Let P(HUNGRYCROC) be the probability of HUNGRYCROC, then (by axiom 3):

P(FULLCROCS) = 1 - P(HUNGRYCROC)

The probability that a particular sockodile has eaten 0 socks on the ith 
toss is: [(n-1)/n]^i

The analytical solution to the P(HUNGRYCROC) can be calculated from the
inclusion-exclusion principle: https://en.wikipedia.org/wiki/Inclusion-exclusion  

Because the atomic probabilities are identical the problem is simplified.

The calculation of values for P(HUNGRYCROC) relies on the multiplication of
the independent 'atomic' probabilities.  For a sufficiently large number of
sockodiles and socks this becomes intractable.
"""

def choose(n, k):
    numerator = math.factorial(n)
    denomlhs = math.factorial(n-k)
    denomrhs = math.factorial(k)
    return ( numerator )  / (denomlhs*denomrhs)

def prob_atleastonemiss(num_atomic_independent_outcomes, num_trials):
    """
    n simple events i.e.:
    choose(n, 1) singles
    choose(n, 2) pairs
    choose(n, 3) triples
    ...
    choose(n,k) kiples
    ...
    choose(n,n) all-in <--  BUT THIS CASE MAKES NO SENSE FOR US SINCE THERE'S NO
    PLACE FOR THE SOCK!!!

    The leading coefficient is (-1)^(k+1)

    P(OF UNION) = reduce(sum, [LC*atomic_prob^num_events])
    """
    compound_probs = []
    for k in range(1, num_atomic_independent_outcomes):
        sign = (-1)**(k+1)
        atomic_probability = ((num_atomic_independent_outcomes-k)*1.0)/(num_atomic_independent_outcomes*1.0)
        print "atomic_probability: %s" % atomic_probability
        num_events = choose(num_atomic_independent_outcomes, k)
        print "num_events is %s" % num_events
        logRHS = math.log(num_events) + num_trials * math.log(atomic_probability)
        compound_prob = sign * math.exp(logRHS)
        #compound_prob = num_events * atomic_probability**num_trials
        #print "compound_prob: %s" % compound_prob
        compound_probs.append(compound_prob)
        #print compound_probs
    probofunion = sum(compound_probs)
    return probofunion

def grapher(NUMBERSTATES):
    x = range(1,NUMBERSTATES+1)
    y = [prob_atleastonemiss(n, n) for n in x]
    print x
    print y
    pyplot.plot(x,y)
    pyplot.xlabel('Number of States')
    pyplot.ylabel('Probability at Least One State Unvisited')
    pyplot.title('One Trial per state, e.g. for a coin flip 2 trials, for a die 6')
    pyplot.show()

def main():
    import sys
    N = int(sys.argv[1])
    t = int(sys.argv[2])

    print "The probability of not seeing a particular event on a trial is:\t %s." % ( (N-1) / N)
    print "The number of mutually exclusive identically probable outcomes is:\t %s." % N
    print "The number of indepent, identical trials is:\t\t\t%s" % t
    print "The probability at least one event is unseen: %s" % prob_atleastonemiss(N, t)
    #grapher(N)
    
if __name__ == '__main__':
    main()

"""
def joint_union_prob(atomic_probability, num_independent_events):
    XXX
    This function returns the probability of the union of
    num_independent_events where each event has probability
    atomic_probability, and the events are independent.
    XXX
    probslist = [atomic_probability]*num_independent_events
    #If a probability calculation becomes impractically small it will be
    #because it is the product of too many 0<val<1 numbers.  The smallest
    #such number (in this context) is the product of the whole list 
    #probslist, so I test whether that number is tractable.
    totalintersection = reduce(lambda x,y:x*y, probslist)
    compoundprobs = []
    

    return totalintersection
"""
