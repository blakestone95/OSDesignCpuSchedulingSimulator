# -*- coding: utf-8 -*-

# Overlord
# Author: Blake Sawyer, Robert Berglund, Daniel Schiefer
# 
# Control process distribution, monitor cpu cores, manage queues, run simulation
import Processes
import Algorithms
import Processors
import csv
from bisect import bisect
import random
import math

currenttime = 0

def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    i = bisect(cum_weights, x)
    return values[i]

def Overlord(datafilereader):
    # Instead of Overlord starting everything, Overlord will be called by GUI 
    # and then do the rest of the simulation

    # Initializataions
    masterpt = Processes.ProcTbl()
    done = False
    ioqueue = []
    queues = []
    # Hard code algorithms for testing purposes
    queues.append(Algorithms.RR(masterpt,1))
    queues.append(Algorithms.RR(masterpt,10))
    queues.append(Algorithms.SPN(masterpt))
    queues.append(Algorithms.FCFS(masterpt))

#------------------------------------------------------------------------------#
    # Load processes into Process Table
    
    for row in datafilereader:
        
        burst = []
        for i in range(2,len(row) - 1):
            burst.append(row[i])
        masterpt.Insert(row[0],burst,row[1])

    incomingpid = masterpt.pid[0]

    while not done == True:
        for processor in processors:
            if processor.getstate() == "idle":

                # Get pid from queue
                # Choose queue based on a probability distribution
                probabilities = []
                choices = []
                total = 0
                for q in queues:
                    total += len(q.pq)
                for a in range(1,len(queues)):
                    # Set priority such that first queues get higher priority and
                    # priority is also based on # elements in queue
                    probabilities.append(math.ceil(len(queues[a-1].pq)/total*100/(a*2)))
                    choices.append((queues[a-1],probabilities[a-1]))
                chosenq = weighted_choice(choices)

                # Get next PID from chosen queue
                pid = chosenq.NextPID()
                
                # Give processor a process to do
                processor.execute(pid,runtime)



        



#------------------------------------------------------------------------------#
        # Collect all times for comparison
        times = []
        # Get time from now to time of next arriving process
        if not incomingpid is None:
            incomingpcb = masterpt.GetPCB(incomingpid)
            tnextprocess = incomingpcb.tarr - currenttime
            times.append(tnextprocess)
        # Get remaining processing time for each processor
        for processor in processors:
            if not processor.getstate() == "idle":
                times.append(processor.currentruntime())
        if not len(ioqueue) == 0:
            for ios in ioqueue:
                times.append(ios[1])

        subtime = min(times)

        # Need to decrement run time from cpu's
        for processor in processors:
            if not processor.getstate() == "idle":
                finishedpid = processor.decrementtime(subtime)
                # processor.decrementtime returns 0 for non-finished processing
                if not finishedpid == 0:
                    # Geting pcb of finished process
                    finishedpcb = masterpt.GetPCB(finishedpid)
                    if not len(finishedpcb.tburst) == 0:
                        # If not finished, block the process and send it to the io q
                        finishedpcb.state = 3
                        ioqueue.append([finishedpid, finishedpcb.tburst.pop(0)])
                    elif:
                        # Set process to finished and store its finishing time
                        finishedpcb.state = 4
                        finishedpcb.tfinish = currenttime + subtime
                    # Remove finished process from queue
                    for q in queues:
                        q.pq.remove(finishedpid)

        # Service ioqueue
        if not len(ioqueue) == 0:
            # Subtract run time from each io element and send back to first queue
            # if done io'ing
            for ios in ioqueue:
                ios[1] = ios[1] - subtime
                if ios[1] == 0:
                    queues[0].Insert(ios[0])

        # Get next incoming process
        if subtime == tnextprocess and not incomingpid is None:
            queues[0].Insert(incomingpid)
            incomingpid = masterpt.NextPID(incomingpid)
            
        # Set wait time

#------------------------------------------------------------------------------#
        # Service queues
        # Look at queues and move pids up levels if time met
        for q in range(0,len(queues) - 1):
            flushed = queues(q).Flush(subtime)
            if not flushed is None:
                queues(q+1).pq.append(flushed)

        # 


        # End of simulation conditions
        if incomingpid is None and len(time) = 0:
            done = True
            
        # Increment current time
        currenttime += subtime
    
    
processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
