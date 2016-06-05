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

    masterpc = Processes.ProcTbl()
    
    for row in datafilereader:
        
        burst = []
        for i in range(2,len(row)):
            burst.append(row[i])
        masterpc.Insert(row[0],burst,row[1])
        
'''
    for processor in processors:
        if processor.getstate() == "idle":
            #Give something to do
            processor.execute(pid,runtime)

    #collect all times for comparison
    times = []
    #Get time from now to time of next arriving process
    times.append(currenttime-waitqueue[0])
    #Get remaining processing time for each processor
    for processor in processors:
        times.append(processor.currentruntime())

    subtime = min(times)

    #Need to decrement current time
    for processor in processors:
        processor.decrementtime(subtime)
    currenttime += subtime'''
    
processInputLocation = 'C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv'
with open(processInputLocation) as f:
        datafilereader = csv.reader(f)
        Overlord(datafilereader)
