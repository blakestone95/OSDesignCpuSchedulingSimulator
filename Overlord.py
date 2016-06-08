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
    incomingpcb = masterpt.GetPCB(incomingpid)

    thingamajig = 0
#------------------------------------------------------------------------------#
    while not done == True:

        # Allocate processes to CPU's and service preemptive queues
        if not len(queues[0].pq) == 0:
            for processor in processors:
                qlevel = 0
                # Check if preemptive queue needs halting
                if processor.state == "running" and queues[processor.currentq].preempt == True:
                    nextpid = queues[processor.currentq].NextPID(processor.pid,processor.processingtime)
                    #print("Next PID on running:",nextpid)
                    if not nextpid == processor.pid or (nextpid == -2 and queues[processor.currentq].tq == processor.processingtime):
                        # If next process is not the same as the current running process,
                        # halt execution
                        # Store current queue before halting
                        procq = queues[processor.currentq]
                        #print("Current queue ",procq)
                        processinfo = processor.Halt()
                        
                        # Place the remaining burst time into the PCB and set to ready state
                        processpcb = masterpt.GetPCB(processinfo[0])
                        #print("HALT!!!",processinfo)
                        processpcb.state = 1
                        processpcb.tburst.insert(0,processinfo[1])

                        try:
                            procq.lastpidindex -= 1
                            procq.lastpid = procq.index(procq.lastpidindex)
                        except:
                            "hi"
                        
                        # Execute new process
                        #nextpcb = masterpt.GetPCB(nextpid)
                        #print("Process ",nextpid," sent to ",processors.index(processor)
                        #      ," with qlvl ",procq)
                        #print("Tburst " + str(pcb.tburst))
                        #processor.Execute(nextpid,nextpcb.tburst.pop(0),procq)
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
                    if type(chosenq) is Algorithms.RR or type(chosenq) is Algorithms.SRT:
                        #print(str(chosenq.lastpid))
                        # Only need running pid and process time if checking if needs replacement
                        nextpid = chosenq.NextPID(0,0)
                    else:
                        nextpid = chosenq.NextPID()
                    #print("Next PID on idle:",nextpid)
                        
                    if nextpid > 0:
                        nextpcb = masterpt.GetPCB(nextpid)
                        
                        # Give processor a process to do, also remove needed burst time from pcb
                        # Set process to running state
                        if not nextpcb.state == 2:

                            #print("Process " + str(pid) + " sent to " + str(processors.index(processor)) +
                            #      " with qlvl " + str(queues.index(chosenq)))
                            #print("Tburst " + str(pcb.tburst))

                            if nextpcb.tresp == -1:
                                nextpcb.tresp = currenttime
                            processor.Execute(nextpid,nextpcb.tburst.pop(0),queues.index(chosenq))
                    

#------------------------------------------------------------------------------#
        # Collect all times for comparison
        times = []
        tnextprocess = 0
        # Get time from now to time of next arriving process
        if not incomingpid is None:
            incomingpcb = masterpt.GetPCB(incomingpid)
            tnextprocess = incomingpcb.tarr - currenttime
            times.append((tnextprocess,"NP"))
        # Get remaining processing time for each processor
        for processor in processors:
            #print(processor.state)
            if not processor.state == "idle":
                times.append((processor.processtime,"P"+str(processors.index(processor))))
        # Get the remaining io time for each item in io queue
        if not len(ioqueue) == 0:
            for ios in ioqueue:
                times.append((ios[1],"IO"))
        # Get the remaining time until next queue flush and time quantum of Algorithms.RR queues
        # if there is a process running in it
        for q in queues:
            times.append(((q.tmax - q.tflush),"Q"+str(queues.index(q))))
            #print("Len " + str(queues.index(q) + 1) + " " + str(len(q.pq)))
            if type(q) is Algorithms.RR:
                if len(q.pq) > 0:
                    for processor in processors:
                        if queues[processor.currentq] == q:
                            times.append((q.tq - processor.processingtime,
                                          "tq Q"+str(queues.index(q))))
            
        #print("Times:  " + str(times))

        subtime = min(times, key = lambda t: t[0])
        subtime = subtime[0]
        #print("Minimum time: ",subtime)

        # Need to decrement run time from cpu's
        for processor in processors:
            if not processor.state == "idle":
                # Store queue level in case process finishes
                qlvl = processor.currentq
                finishedpid = processor.DecrementTime(subtime)
                # processor.DecrementTime returns 0 for non-finished processing
                if not finishedpid == 0:
                    # Geting pcb of finished process
                    finishedpcb = masterpt.GetPCB(finishedpid)
                    
                    # Remove pid from queue if finished or blocked
                    #print("Processor ",processors.index(processor)," finished PID ",finishedpid," Current q ",qlvl)
                    queues[qlvl].RemovePID(finishedpid)
                    
                    if not len(finishedpcb.tburst) == 0:
                        # If not finished, block the process and send it to the io q
                        #print("PID ",finishedpid," blocked")
                        finishedpcb.state = 3
                        ioqueue.append([finishedpid, finishedpcb.tburst.pop(0)])
                    else:
                        # Set process to finished and store its finishing time
                        #print("PID ",finishedpid," finished")
                        finishedpcb.state = 4
                        finishedpcb.tfinish = currenttime + subtime
                    # Remove finished process from queue
                    #for q in queues:
                        #q.RemovePID(finishedpid)

        # Service io queue
        if len(ioqueue) > 0:
            # Subtract run time from each io element
            for ios in ioqueue:
                ios[1] = ios[1] - subtime
                iopcb = masterpt.GetPCB(ios[0])
                # Delete from io and send back to first queue if done io'ing
                # and more cpu time needed
                if ios[1] == 0 and len(iopcb.tburst) > 0:
                    iopcb.state = 1
                    queues[0].InsertPID(ios[0])
                    ioqueue.remove(ios)
                # If no cpu time after IO, finish process
                elif len(iopcb.tburst) == 0:
                    #print("PID ",ios[0]," finished in IO")
                    iopcb.state = 4
                    iopcb.tfinish = currenttime + subtime
                    ioqueue.remove(ios)

        # Get next incoming process and send to bottom queue
        if not incomingpid is None and tnextprocess == subtime:
            queues[0].InsertPID(incomingpid)
            incomingpid = masterpt.NextPID(incomingpid)
            
#------------------------------------------------------------------------------#
        # Service queues
        # Look at queues and move pids up levels if time met
        for q in range(0,len(queues) - 1):
            flushed = queues[q].Flush(subtime)
            #print("Flushed " + str(q) + " " + str(flushed))
            if not flushed is None:
                for a in flushed:
                    queues[q+1].InsertPID(a)
                    # Replace queue level if a processor is running pid in flushed queue
                    for p in processors:
                        #print("FLUSH ",p.pid," ",a)
                        if p.pid == a:
                            p.currentq = q + 1
                            #print("Flush caused processor ",processors.index(p)," to change")

        # Increment runtime on Algorithms.RR queue if it is running
        for q in queues:
            if type(q) is Algorithms.RR:
                if len(q.pq) > 0 and q.Running == True:
                    q.runtime += subtime
                    
#------------------------------------------------------------------------------#
        # End of simulation conditions
        # If there is no next process and the only things in the times list are
        # the queue flush times, then the simulation is done
        if incomingpid is None and len(times) == len(queues):
            done = True
            
        # Increment current time
        currenttime += subtime
        '''for q in queues:
            print("Queue contents: " + str(q.pq))
        for p in processors:
            print("Processor #",processors.index(p),"State:",p.state,"pid:",p.pid,"Queue lvl:",p.currentq,"Time spent processing:",p.processingtime)
        print("I/O queue ",ioqueue)'''
        '''if currenttime > thingamajig:
            print("Current time:  " + str(currenttime))
            thingamajig += 100
            if currenttime > 19000:
                for q in queues:
                    print("Queue contents: " + str(q.pq))
                for p in processors:
                    print("Processor #",processors.index(p),"State:",p.state,"pid:",p.pid,"Queue lvl:",p.currentq,"Time spent processing:",p.processingtime)
        '''
        if subtime == 0:
            print("Error subtime 0 --ISBROKEEEEEEN--")
            print("Times:  " + str(times))
            for q in queues:
                print("Queue contents: " + str(q.pq))
            for p in processors:
                print("Processor #",processors.index(p),"State:",p.state,"pid:",p.pid,"Queue lvl:",p.currentq,"Time spent processing:",p.processingtime)
            print("I/O queue ",ioqueue)
            print("Current time:  " + str(currenttime))
            break
        
    

processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata2.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
        print("Simulation Complete")

