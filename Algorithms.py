# Algorithms.py
# Author: Blake Sawyer
# 
# Classes for CPU scheduling algorithms
import Processes
import math
import sys

# First come first serve - retrieve item from the top of the queue
class FCFS:
        preempt = False # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue
                self.tmax = 1000 # Max time between flushes
                self.lastpid = -1 # Store the last pid that was returned from NextPID
                self.lastpidindex = -1
                self.tflush = 0 # Accumulated time since last flush
                self.throughput = [0]

        # Increment the wait time of a process by "time"
        def IncWaitTime(self,time):
                for p in self.pq:
                        pcb = self.pt.GetPCB(p)
                        if not pcb.state == 2:
                                pcb.twait += time

        # InsertPID process into queue
        def InsertPID(self, pid):
                self.pq.append(pid)

        # Remove process from queue
        def RemovePID(self, procid):
                self.pq.remove(procid)

        # Get next pid to be run
        def NextPID(self):
                if self.lastpid == -1 and not len(self.pq) == 0:
                        self.lastpid = self.pq[0]
                        self.lastpidindex = 0
                try:
                        self.lastpidindex = self.pq.index(self.lastpid)
                except ValueError:
                        # Decrement one if last pid was deleted
                        self.lastpidindex -= 1
                if self.lastpidindex < len(self.pq) - 1:
                        self.lastpid = self.pq[self.lastpidindex + 1]
                        self.lastpidindex += 1
                else:
                        self.lastpid = self.pq[0]
                        self.lastpidindex = 0
                        
                pcb = self.pt.GetPCB(self.lastpid)
                if pcb.state == 2:
                        # Return -1 if full
                        return -2
                else:
                        # Return new lastpid otherwise
                        return self.lastpid
                # In case any of the other return statements aren't reached
                return -1

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                if len(self.pq) > 0:
                        self.tflush += runtime
                        # Flush top 10 processes from queue if particular time elapsed
                        if self.tflush >= self.tmax:
                                self.tflush = 0
                                # Set lastpid to previous if it is within range to be flushed
                                if self.lastpidindex < 10:
                                        if len(self.pq) > 10:
                                                self.lastpidindex = 10
                                        else:
                                                self.lastpidindex = -1
                                        if self.lastpidindex == -1:
                                                self.lastpid = -1
                                        else:
                                                self.lastpid = self.pq[self.lastpidindex]
                                tenprocesses = []
                                if len(self.pq) > 10:
                                        for a in range(0,10):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                                self.lastpidindex -= 1
                                        return tenprocesses
                                else:
                                        for a in range(0,len(self.pq)):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                                self.lastpidindex -= 1
                                        return tenprocesses
                return None
        
        def addThroughput(self):
                self.throughput[-1] += 1
        def throughputadv(self):
                self.throughput.append(0)       
                                
	

# Round robin - retrieve item from top of queue, process for a time, 
# then return to queue unless finished
class RR:
        preempt = True # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl, timeq):
                self.pt = proctbl
                self.tq = timeq
                # only flush queue if 20 processed have been serviced
                self.tmax = timeq*20 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                self.pq = [] # Process Queue
                self.lastpid = -1 # Store the last pid that was returned from NextPID
                self.lastpidindex = -1
                self.tflush = 0 # Accumulated time since last flush
                self.throughput = [0]

        # Increment the wait time of a process by "time"
        def IncWaitTime(self,time):
                for p in self.pq:
                        pcb = self.pt.GetPCB(p)
                        if not pcb.state == 2:
                                pcb.twait += time
                
        # InsertPID process into queue
        def InsertPID(self, pid):
                #print("Insert " + str(pid) + " into RR w/ tq " + str(self.tq))
                self.pq.append(pid)

        # Remove process from queue
        def RemovePID(self, procid):
                self.pq.remove(procid)

        # Determine if any process in RR queue is running
        def Running(self):
                for i in self.pq:
                        pcb = self.pt.GetPCB(i)
                        if pcb.state == "running":
                                return True
                        else:
                                return False
                        
        # Get next pid to be run
        # Starting at the most recent pid returned from this, loop until
        # a non-running process is found and return that one
        def NextPID(self,runningpid,runtime):
                # If the time quantum has not elapsed, return running process sent from cpu
                if not runningpid == 0 and runtime < self.tq:
                        return runningpid
                # First time through
                elif self.lastpid == -1 and not len(self.pq) == 0:
                        self.lastpid = self.pq[0]
                        self.lastpidindex = 0
                else:
                                
                        # Get index of lastpid
                        try:
                                self.lastpidindex = self.pq.index(self.lastpid)
                        except ValueError:
                                self.lastpidindex -= 1
                        # If not at end of list, get next PID
                        if self.lastpidindex < len(self.pq) - 1:
                                self.lastpid = self.pq[self.lastpidindex + 1]
                                self.lastpidindex += 1
                        # Resets PID to first one in the list
                        else:
                                self.lastpid = self.pq[0]
                                self.lastpidindex = 0
                                
                        pcb = self.pt.GetPCB(self.lastpid)
                        if pcb.state == 2:
                                # Return -2 if all running
                                return -2
                        else:
                                # Return new lastpid otherwise
                                return self.lastpid
                # In case any of the other return statements aren't reached
                return self.lastpid

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                if len(self.pq) > 0:
                        self.tflush += runtime
                        # Flush top 10 processes from queue if particular time elapsed
                        if self.tflush >= self.tmax:
                                self.tflush = 0
                                # Set lastpid to previous if it is within range to be flushed
                                if self.lastpidindex < 10:
                                        if len(self.pq) > 10:
                                                self.lastpidindex = 10
                                        else:
                                                self.lastpidindex = -1
                                        if self.lastpidindex == -1:
                                                self.lastpid = -1
                                        else:
                                                self.lastpid = self.pq[self.lastpidindex]
                                tenprocesses = []
                                if len(self.pq) > 10:
                                        for a in range(0,10):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                                self.lastpidindex -= 1
                                        return tenprocesses
                                else:
                                        for a in range(0,len(self.pq)):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                                self.lastpidindex -= 1
                                        return tenprocesses
                return None
        
        def addThroughput(self):
                self.throughput[-1] += 1
        def throughputadv(self):
                self.throughput.append(0)       
		
# Shortest process next - retrieve item with shortest process time
class SPN:
        preempt = False # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue

                self.tmax = 1000 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                self.throughput = [0]

        # Increment the wait time of a process by "time"
        def IncWaitTime(self,time):
                for p in self.pq:
                        pcb = self.pt.GetPCB(p)
                        if not pcb.state == 2:
                                pcb.twait += time
                
        # InsertPID process into queue
        def InsertPID(self, pid):
                self.pq.append(pid)

        # Remove process from queue
        def RemovePID(self, procid):
                self.pq.remove(procid)
                
        # Get next pid to be run and remove it from the queue
        # Find minimum process time needed
        def NextPID(self):
                i = 0
                minpid = 0
                mintime = sys.maxsize
                # Loop through process queue
                for pid in self.pq:
                        i += 1
                        pcb = self.pt.GetPCB(pid)
                        #print("SPN PIDS",pid,pcb.state)
                        # Choose processes that are ready
                        if pcb.state == 1:
                                # Record the first CPU burst time and pid on first iteration
                                if i == 1:
                                        mintime = pcb.tburst[0]
                                        minpid = pid
                                # On other pid's only replace minimum time and assoc pid if that
                                # process has a smaller brust time than the current smallest
                                if not i == 1 and pcb.tburst[0] < mintime:
                                        mintime = pcb.tburst[0]
                                        minpid = pid
                # Return the pid stored in minpid
                return minpid

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                if len(self.pq) > 0:
                        self.tflush += runtime
                        # Flush top 10 processes from queue if particular time elapsed
                        # OK to be over flush time
                        if self.tflush >= self.tmax:
                                self.tflush = 0
                                tenprocesses = []
                                if len(self.pq) > 10:
                                        for a in range(0,10):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                        return tenprocesses
                                else:
                                        for a in range(0,len(self.pq)):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                        return tenprocesses
                return None
        
        def addThroughput(self):
                self.throughput[-1] += 1
        def throughputadv(self):
                self.throughput.append(0)        
				
			
# Shortest remaining time - retrieve item with shortest process time
# 							except preempt if incoming process is shorter
class SRT:
        preempt = True # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue
                self.tmax = 1000 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                self.throughput = [0]

        # Increment the wait time of a process by "time"
        def IncWaitTime(self,time):
                for p in self.pq:
                        pcb = self.pt.GetPCB(p)
                        if not pcb.state == 2:
                                pcb.twait += time
                
        # InsertPID process into queue
        def InsertPID(self, pid):
                self.pq.append(pid)

        # Remove process from queue
        def RemovePID(self, procid):
                self.pq.remove(procid)
                
        # Get next pid to be run and remove it from the queue
        # Find minimum process time needed
        # --runtime not needed--
        def NextPID(self,runningpid,*runtime):
                i = 0
                minpid = 0
                mintime = sys.maxsize
                # Loop through process queue
                for pid in self.pq:
                        i += 1
                        pcb = self.pt.GetPCB(pid)
                        #print("SPN PIDS",pid,pcb.state)
                        # Choose processes that are ready
                        if pcb.state == 1:# or pid == runningpid:
                                # Record the first CPU burst time and pid on first iteration
                                if i == 1:
                                        mintime = pcb.tburst[0]
                                        minpid = pid
                                # On other pid's only replace minimum time and assoc pid if that
                                # process has a smaller brust time than the current smallest
                                if not i == 1 and pcb.tburst[0] < mintime:
                                        mintime = pcb.tburst[0]
                                        minpid = pid
                # Return the pid stored in minpid
                return minpid

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                if len(self.pq) > 0:
                        self.tflush += runtime
                        # Flush top 10 processes from queue if particular time elapsed
                        # OK to be over flush time
                        if self.tflush >= self.tmax:
                                self.tflush = 0
                                tenprocesses = []
                                if len(self.pq) > 10:
                                        for a in range(0,10):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                        return tenprocesses
                                else:
                                        for a in range(0,len(self.pq)):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                        return tenprocesses
                return None
        
        def addThroughput(self):
                self.throughput[-1] += 1
        def throughputadv(self):
                self.throughput.append(0)       
		
# Highest response ratio next - calculate response ratio for each process and 
#								choose the one with the highest
class HRRN:
        preempt = False # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue
                self.tmax = 1000 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                self.throughput = [0]

        # Increment the wait time of a process by "time"
        def IncWaitTime(self,time):
                for p in self.pq:
                        pcb = self.pt.GetPCB(p)
                        if not pcb.state == 2:
                                pcb.twait += time
                
        # InsertPID process into queue
        def InsertPID(self, pid):
                self.pq.append(pid)

        # Remove process from queue
        def RemovePID(self, procid):
                self.pq.remove(procid)
                
        # Get next pid to be run and remove it from the queue
        # Find highest response ratio
        def NextPID(self):
                i = 0
                j = 0
                sumtime = 0
                maxpid = 0
                maxrr = 0
                # Loop through process queue
                for pid in self.pq:
                        i = i + 1
                        pcb = self.pt.GetPCB(pid)
                        #print("HRRN PIDS",pid,pcb.state)
                        #print(pcb.tburst)
                        # Choose processes that are ready
                        if pcb.state == 1:
                                # Calculate the total required run time from pcb
                                for j in range(0,math.ceil(len(pcb.tburst)/2)):
                                        sumtime = sumtime + pcb.tburst[2*j]
                                # Calculate response ratio
                                respratio = 1 + pcb.twait/sumtime
                                # Record the first CPU burst time and pid on first iteration
                                if i == 1:
                                        maxrr = respratio
                                        maxpid = pid
                                # On other pid's only replace minimum time and assoc pid if that
                                # process has a smaller brust time than the current smallest
                                if (not i == 1) and (respratio > maxrr):
                                        maxrr = respratio
                                        maxpid = pid
                # Return the pid stored in minpid
                return maxpid

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                if len(self.pq) > 0:
                        self.tflush += runtime
                        # Flush top 10 processes from queue if particular time elapsed
                        # OK to be over flush time
                        if self.tflush >= self.tmax:
                                self.tflush = 0
                                tenprocesses = []
                                if len(self.pq) > 10:
                                        for a in range(0,10):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                        return tenprocesses
                                else:
                                        for a in range(0,len(self.pq)):
                                                tenprocesses.append(self.pq[0])
                                                self.pq.pop(0)
                                        return tenprocesses
                return None

        def addThroughput(self):
                self.throughput[-1] += 1
        def throughputadv(self):
                self.throughput.append(0)
        