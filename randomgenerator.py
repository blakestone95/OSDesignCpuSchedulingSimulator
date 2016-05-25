#random process generator
#Will output processes in the following format
#First cell is PID
#Second cell is arrival time
#Remaining cells will alternate between CPU time and IO time
#Odd cells are CPU time and even cells are IO time

import random
import csv

#Set number of processes to be created
numberOfProcesses = 1000

def generaterandomlist(PID,arrivaltime):
    #Controlling variables
    minarrivalincrement = 0
    maxarrivalincrement = 100
    minbursttime = 2
    maxbursttime = 500
    maxIO = 6
    minIOtime = 2
    maxIOtime = 100

    #Set burst time value for the whole process
    bursttime = random.randrange(maxbursttime-minbursttime)+minbursttime

    #Randomly select a number of IO to use between 0 and 6
    #If bursttime is really small don't do IO
    IOnum = random.randrange(7)
    if bursttime < 10:
        IOnum = 0

    IOtimes = []
    CPUtimes = []
    a = 0

    #Determine if the last time will be IO or CPU
    extracpu = 0
    if IOnum > 0:
        extracpu = random.randrange(2)

    #Randomly select times in the burst cycle
    while a != IOnum+extracpu:
        settime = random.randrange(bursttime-1)+1
        if not(settime in CPUtimes):
            CPUtimes.append(settime)
            a += 1

    #Sort the times in accending order
    CPUtimes.sort()

    #Create list of time splices CPU is running
    CPUcalc = []
    counter = 0
    for element in CPUtimes:
        CPUcalc.append(element-counter)
        counter = element

    #Generate a new process with pid and arrival time
    newprocess = [PID,arrivaltime]

    #Alternate between adding a cpu time and adding IO
    #Add CPU time at the end if appropriate
    #Add CPU time if no IO
    for i in range(0,IOnum):
        newprocess.append(CPUcalc[i])
        newprocess.append(random.randrange(maxIOtime-minIOtime)+minIOtime)
    if extracpu == 1:
        newprocess.append(CPUcalc[len(CPUcalc)-1])
    elif IOnum == 0:
        newprocess.append(bursttime)
    return newprocess

#Initialize activation time
currenttime = 0

#Write to csv file
with open('randomdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1,numberOfProcesses+1):
        #Randomly increment activation time
        currenttime += random.randrange(30)
        #Write a generated process to csv
        writer.writerow(generaterandomlist(i,currenttime))
