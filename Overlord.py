# Overlord
# Author: Blake Sawyer, Robert Berglund, Daniel Schiefer
# 
# Control process distribution, monitor cpu cores, manage queues, run simulation
import Processes
import Algorithms
import cpuScheduler
import Processors

currenttime = 0

# correct my syntax if it's wrong...
def Overlord(datafilereader):
    # Instead of Overlord starting everything, Overlord will be called by GUI 
    # and then do the rest of the simulation
    for row in datafilereader:
        print(str(row))
    #print("Hello World!")

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
    currenttime += subtime
    
