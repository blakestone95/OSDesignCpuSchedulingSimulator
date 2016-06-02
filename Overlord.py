# Overlord
# Author: Blake Sawyer, Robert Berglund, Daniel Schiefer
# 
# Control process distribution, monitor cpu cores, manage queues, run simulation
import Processes
import Algorithms
import cpuScheduler
import Processors

# correct my syntax if it's wrong...
def Overlord(datafilereader):
    # Instead of Overlord starting everything, Overlord will be called by GUI 
    # and then do the rest of the simulation
    for row in datafilereader:
        print(str(row))
    #print("Hello World!")
