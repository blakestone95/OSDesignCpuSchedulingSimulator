# -*- coding: utf-8 -*-

# Overlord
# Author: Blake Sawyer, Robert Berglund, Daniel Schiefer
# 
# Control process distribution, monitor cpu cores, manage queues, run simulation
import Processes
import Algorithms
import cpuScheduler
import Processors
import csv

currenttime = 0

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
        for i in range(2,len(row)):
            burst.append(row[i])
        masterpt.Insert(row[0],burst,row[1])

    incomingpid = masterpt.pid[0]

    while not done == True:
        for processor in processors:
            if processor.getstate() == "idle":

                # Get pid from queue
                
                # Give processor a process to do
                processor.execute(pid,runtime)



        



#------------------------------------------------------------------------------#
        # collect all times for comparison
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

        subtime = min(times)

        # Need to decrement current time from cpu's
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
                        # Set process to finished
                        finishedpcb.state = 4
                        finishedpcb.tfinish = currenttime + subtime
                        # Remove finished process from queue
                        for q in queues:
                            q.pq.remove(finishedpid)

        # Get next incoming process
        if subtime == tnextprocess and not incomingpid is None:
            queues[0].Insert(incomingpid)
            incomingpid = masterpt.NextPID(incomingpid)
            
        # Set wait time

#------------------------------------------------------------------------------#
        # Service queues
        


        # end of simulation conditions
        if incomingpid is None:
            done = True
            
        # Increment current time
        currenttime += subtime
    
    
processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
