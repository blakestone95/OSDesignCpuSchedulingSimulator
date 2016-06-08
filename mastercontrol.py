import Overlord
import csv
import random
import math
import Algorithms

#files = []
#files.append('C:\\Users\\Blake\\Documents\\GitHub\\SchedulerForDayz\\randomdata.csv')
#flag = "RR 10,RR 20,SPN,SRT,HRRN,FCFS"


results = {}
def mastercontrol(results,flag,pnum,files):
    results[flag] = []
    for processInputLocation in files:
        with open(processInputLocation) as f:
                datafilereader = csv.reader(f)
                results[flag].append(Overlord(datafilereader,flag,pnum))
                
                print("Simulation Complete. Results:",results)

def takeaverage(results):
    for element in results:
        sum(element)

