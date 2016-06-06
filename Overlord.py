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
    currenttime = 0
    # Hard code algorithms for testing purposes
    queues.append(Algorithms.RR(masterpt,5))
    queues.append(Algorithms.RR(masterpt,15))
    queues.append(Algorithms.SPN(masterpt))
    queues.append(Algorithms.FCFS(masterpt))
    # Hard code processors as well
    # This'll be easy to make choosable
    processors.append(Processors.CPU(masterpt))
    processors.append(Processors.CPU(masterpt))
    processors.append(Processors.CPU(masterpt))
    processors.append(Processors.CPU(masterpt))

#------------------------------------------------------------------------------#
    # Load processes into Process Table
    # Typecast elements to integers
    for row in datafilereader:
        
        burst = []
        for i in range(2,len(row)):
            burst.append(int(row[i]))
        masterpt.Insert(int(row[0]),burst,int(row[1]))

    # Get first pid
    incomingpid = masterpt.pid[0]
    
#------------------------------------------------------------------------------#
    while not done == True:

        # Allocate processes to CPU's and service preemptive queues
        if not len(queues[0].pq) == 0:
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
                    # If no processes are in the queues yet, insert into first queue
                    if not total == 0:
                        for a in range(1,len(queues)):
                            # Set priority such that first queues get higher priority and
                            # priority is also based on # elements in queue
                            probabilities.append(math.ceil(len(queues[a-1].pq)/total*100/(a*2)))
                            choices.append((queues[a-1],probabilities[a-1]))
                        chosenq = weighted_choice(choices)
                    else:
                        chosenq = queues[0]

                    # Get next PID from chosen queue
                    if type(chosenq) is Algorithms.RR:
                        print(str(chosenq.lastpid))
                        pid = chosenq.NextPID(chosenq.lastpid,chosenq.tq)
                    else:
                        pid = chosenq.NextPID()
                    pcb = masterpt.GetPCB(pid)
                    print("THING",pcb.state)
                    
                    # Give processor a process to do, also remove needed burst time from pcb
                    # Set process to running state
                    if not pcb.state == 2:

                        print("Process " + str(pid) + " sent to " + str(processors.index(processor)) +
                              " with qlvl " + str(queues.index(chosenq)))
                        print("Tburst " + str(pcb.tburst))
                        
                        processor.Execute(pid,pcb.tburst.pop(0),queues.index(chosenq))
                # Check if preemptive queue needs to run new process
                if processor.state == "running" and queues[processor.currentq].preempt == True:
                    if type(queues[processor.currentq]) is Algorithms.RR:
                        nextpid = queues[processor.currentq].NextPID(processor.pid,processor.processingtime)
                    else:
                        nextpid = queues[processor.currentq].NextPID()
                    if not nextpid == processor.pid and not nextpid is None:
                        # If next process is not the same as the current running process,
                        # halt execution
                        processinfo = processor.Halt()
                        
                        # Insert PID back into queue
                        queues[processor.currentq].InsertPID(processinfo[0])
                        
                        # Place the remaining burst time into the PCB and set to ready state
                        processpcb = masterpt.GetPCB(processinfo[0])
                        print("HALT!!!",processpcb.state)
                        processpcb.state = 1
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
        # Get the remaining time until next queue flush and time quantum of Algorithms.RR queues
        # if there is a process running in it
        for q in queues:
            times.append(q.tmax - q.tflush)
            print("Len " + str(queues.index(q) + 1) + " " + str(len(q.pq)))
            if type(q) is Algorithms.RR:
                if len(q.pq) > 0:
                    times.append(q.tq)
            
        print("Times:  " + str(times))

        subtime = min(times)
        print("Minimum time:  " + str(subtime))

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
                        print("PID ",finishedpid," blocked")
                        finishedpcb.state = 3
                        ioqueue.append([finishedpid, finishedpcb.tburst.pop(0)])
                    else:
                        # Set process to finished and store its finishing time
                        print("PID ",finishedpid," finished")
                        finishedpcb.state = 4
                        finishedpcb.tfinish = currenttime + subtime
                    # Remove finished process from queue
                    for q in queues:
                        q.RemovePID(finishedpid)

        # Service io queue
        if len(ioqueue) > 0:
            # Subtract run time from each io element and send back to first queue
            # if done io'ing
            for ios in ioqueue:
                ios[1] = ios[1] - subtime
                if ios[1] == 0:
                    queues[0].InsertPID(ios[0])

        # Get next incoming process and send to bottom queue
        if subtime == tnextprocess and not incomingpid is None:
            queues[0].InsertPID(incomingpid)
            incomingpid = masterpt.NextPID(incomingpid)
            
#------------------------------------------------------------------------------#
        # Service queues
        # Look at queues and move pids up levels if time met
        for q in range(0,len(queues) - 1):
            flushed = queues[q].Flush(subtime)
            print("Flushed " + str(q) + " " + str(flushed))
            if not flushed is None:
                for a in flushed:
                    queues[q+1].InsertPID(a)

        # Increment runtime on Algorithms.RR queue if it is running
        for q in queues:
            if type(q) is Algorithms.RR:
                if len(q.pq) > 0 and q.Running == True:
                    q.runtime += subtime
                    
#------------------------------------------------------------------------------#
        # End of simulation conditions
        if incomingpid is None and len(time) == 0:
            done = True
            
        # Increment current time
        currenttime += subtime
        for q in queues:
            print("Queue contents: " + str(q.pq))
        for p in processors:
            print("Processor " + str(processors.index(p)) + " pid: " + str(p.pid))
        print("Current time:  " + str(currenttime))
    
    
processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
