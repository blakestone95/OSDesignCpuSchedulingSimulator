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

# correct my syntax if it's wrong...
def Overlord(datafilereader):
    # Instead of Overlord starting everything, Overlord will be called by GUI 
    # and then do the rest of the simulation

    # Load processes into Process Table

    masterpt = Processes.ProcTbl()
    done = False
    ioqueue = []
    
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
                finishedpcb = masterpt.GetPCB(finishedpid)
                if not finishedpid == 0 and not len(finishedpcb.tburst) == 0:
                    iopcb = masterpt.GetPCB(finishedpid)
                    iopcb.state = 3
                    ioqueue.append([finishedpid, iopcb.tburst.pop(0)])

        # Get next 
        if subtime == tnextprocess and not incomingpid is None:
            incomingpid = masterpt.NextPID(incomingpid)
            
        # Increment current time
        currenttime += subtime
        
        if incomingpid is None:
            done = True
    
    
processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
