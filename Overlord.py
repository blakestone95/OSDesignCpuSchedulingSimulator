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

# Borrowed from internet (Bobby found it)
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

# Overlord of all cpu scheduling
def Overlord(datafilereader):
    # Instead of Overlord starting everything, Overlord will be called by GUI 
    # and then do the rest of the simulation

    # Initializataions
    masterpt = Processes.ProcTbl()
    done = False
    ioqueue = []
    queues = []
    processors = []
    # Hard code algorithms for testing purposes
    queues.append(Algorithms.RR(masterpt,1))
    queues.append(Algorithms.RR(masterpt,10))
    queues.append(Algorithms.SPN(masterpt))
    queues.append(Algorithms.FCFS(masterpt))
    # Hard code processors as well
    # This'll be easy to make choosable
    processors.append(Processors.CPU())
    processors.append(Processors.CPU())
    processors.append(Processors.CPU())
    processors.append(Processors.CPU())

#------------------------------------------------------------------------------#
    # Load processes into Process Table
    
    for row in datafilereader:
        
        burst = []
        for i in range(2,len(row) - 1):
            burst.append(row[i])
        masterpt.InsertPID(row[0],burst,row[1])

    # Get first pid
    incomingpid = masterpt.pid[0]
    
#------------------------------------------------------------------------------#
    while not done == True:

        # Allocate processes to CPU's and service preemptive queues
        for processor in processors:
            qlevel = 0
            if processor.state == "idle":

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
                pcb = masterpt.GetPCB(pid)
                
                # Give processor a process to do, also remove needed burst time from pcb
                processor.Execute(pid,pcb.tburst.pop(0),queues.index(chosenq))
            # Check if preemptive queue needs to run new process
            if processor.state == "running" and queues[processor.currentq].preempt == True:
                nextpid = queues[processor.currentq].NextPID
                
                if not nextpid == processor.pid:
                    # If next process is not the same as the current running process, halt execution
                    processinfo = processor.Halt()
                    
                    # Insert PID back into queue
                    queues[processor.currentq].InsertPID(processinfo[0])
                    
                    # Place the remaining burst time into the PCB
                    processpcb = masterpt.GetPCB(processinfo[0])
                    processpcb.tburst.insert(processinfo[1],0)
                    
                    # Execute new process
                    nextpcb = masterpt.GetPCB(pid)
                    processor.execute(nextpid,nextpcb.tburst.pop(0),processor.currentq)




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
            if not processor.state == "idle":
                times.append(processor.currentruntime())
        # Get the remaining io time for each item in io queue
        if not len(ioqueue) == 0:
            for ios in ioqueue:
                times.append(ios[1])
        # Get the remaining time until next queue flush
        for q in queues:
            times.append(q.tmax - q.tflush)

        subtime = min(times)

        # Need to decrement run time from cpu's
        for processor in processors:
            if not processor.state == "idle":
                finishedpid = processor.DecrementTime(subtime)
                # processor.DecrementTime returns 0 for non-finished processing
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
                        q.RemovePID(finishedpid)

        # Service io queue
        if not len(ioqueue) == 0:
            # Subtract run time from each io element and send back to first queue
            # if done io'ing
            for ios in ioqueue:
                ios[1] = ios[1] - subtime
                if ios[1] == 0:
                    queues[0].InsertPID(ios[0])

        # Get next incoming process
        if subtime == tnextprocess and not incomingpid is None:
            queues[0].InsertPID(incomingpid)
            incomingpid = masterpt.NextPID(incomingpid)
            
#------------------------------------------------------------------------------#
        # Service queues
        # Look at queues and move pids up levels if time met
        for q in range(0,len(queues) - 1):
            flushed = queues(q).Flush(subtime)
            if not flushed is None:
                for a in flushed:
                    queues(q+1).InsertPID(a)
                    
#------------------------------------------------------------------------------#
        # End of simulation conditions
        if incomingpid is None and len(time) = 0:
            done = True
            
        # Increment current time
        currenttime += subtime
    
    
processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
