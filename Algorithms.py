# Algorithms.py
# Author: Blake Sawyer
# 
# Classes for CPU scheduling algorithms
import Processes

# First come first serve - retrieve item from the top of the queue
class FCFS:
        preempt = False # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue
                self.tmax = 200 # Max time between flushes
                self.lastpid = -1 # Store the last pid that was returned from NextPID
                self.lastpidindex = -1
                self.tflush = 0 # Accumulated time since last flush

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
                else:
                        self.lastpid = self.pq[0]
                        
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
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                # OK to be over flush time
                if self.tflush >= self.tmax:
                        self.tflush = 0
                        # Set lastpid to default if it is within range to be flushed
                        if self.pq.index(self.lastpid) < 10:
                                self.lastpid = -1
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
                else:
                        return None
                                
	

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
                
        # InsertPID process into queue
        def InsertPID(self, pid):
                print("Insert " + str(pid) + " into RR w/ tq " + str(self.tq))
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
        # If all processes are running, return None
        # Set runningpid and runtime to 0 if getting getting next pid for idle cpu
        def NextPID(self,runningpid,runtime):
                # If the time quantum has not elapsed, return running process sent from cpu
                if not runningpid == 0 and runtime < self.tq:
                        return runningpid
                else:
                        '''lastrunning = 0
                        lastrunningindex = -1
                        # Set lastrunning if only element and running
                        if len(self.pq) == 1:
                                pcb = self.pt.GetPCB(self.pq[0])
                                if pcb.state == 2:
                                        lastrunning = self.pq[0]
                                        lastrunningindex = 0
                        # Otherwise, get the last running pid which has a ready process after
                        elif not len(self.pq) == 0:
                                for i in range(0,len(self.pq)):
                                        pcb = self.pt.GetPCB(self.pq[i])
                                        # Get pcb for next pid if not at end of list (zero index)
                                        if not i + 1 > len(self.pq) - 1:
                                                pcbnext = self.pt.GetPCB(self.pq[i + 1])
                                                if pcb.state == 2 and pcbnext.state == 1:
                                                        lastrunning = pcb.pid
                                                        lastrunningindex = i
                                        # If at end of list, get beginning of list
                                        else:
                                                # Check if end of list has running process
                                                # and if first process is ready
                                                print("RR looparound")
                                                pcbnext = self.pt.GetPCB(self.pq[0])
                                                if pcb.state == 2 and pcbnext.state == 1:
                                                        lastrunning = pcb.pid
                                                        lastrunningindex = i
                        else:
                                print("Error queue empty")'''
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
                        else:
                                self.lastpid = self.pq[0]
                                
                        pcb = self.pt.GetPCB(self.lastpid)
                        if pcb.state == 2:
                                # Return -2 if all running
                                return -2
                        else:
                                # Return new lastpid otherwise
                                return self.lastpid
                        # In case any of the other return statements aren't reached
                        return -1
                '''
                        print("Last running ",lastrunning," runtime ",runtime," lst rn index ",lastrunningindex," len ",len(self.pq))
                        if lastrunning == 0:
                                # Find out if contains non-running processes
                                isrunning = True
                                for pid in self.pq:
                                        pcb = self.pt.GetPCB(pid)
                                        if not pcb.state == 2:
                                                isrunning = False
                                                break
                                if isrunning == False:
                                        self.lastpid = self.pq[0]
                                        print("Empty list")
                                else:
                                        self.lastpid = runningpid
                                        print("Full list")
                        elif not runtime == self.tq and not len(self.pq) - 1 == lastrunningindex:
                                self.lastpid = self.pq[lastrunningindex + 1]
                                print("Normal Next process")
                        elif runtime == self.tq and not len(self.pq) - 1 == lastrunningindex:
                                self.lastpid = self.pq[lastrunningindex + 1]
                                print("On Halt Next process")
                        elif runtime == self.tq and len(self.pq) - 1 == lastrunningindex:
                                self.lastpid = self.pq[0]
                                print("Same process")
                        else:
                                print("Error no pid returned")
                                self.lastpid = -1
                return self.lastpid'''

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush >= self.tmax:
                        self.tflush = 0
                        # Set lastpid to default if it is within range to be flushed
                        if self.pq.index(self.lastpid) < 10:
                                self.lastpid = -1
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
                else:
                        return None
		
# Shortest process next - retrieve item with shortest process time
class SPN:
        preempt = False # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue

                self.tmax = 200 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                
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
                # Loop through process queue
                for pid in self.pq:
                        i += 1
                        pcb = self.pt.GetPCB(pid)
                        print("PIDS",pid,pcb.state)
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
                # Pop the pid stored in minpid
                index = self.pq.index(minpid)
                return self.pq[index]

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
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
                else:
                        return None
				
			
# Shortest remaining time - retrieve item with shortest process time
# 							except preempt if incoming process is shorter
class SRT:
        preempt = True # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue
                self.tmax = 200 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                
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
                # Loop through process queue
                for pid in self.pq:
                        i = i + 1
                        pcb = self.pt.GetPCB(pid)
                        # Choose processes that are ready
                        if pcb.state == 1:
                                # Record the first CPU burst time and pid on first iteration
                                if i == 1:
                                        mintime = pcb.tburst[0]
                                        minpid = pid
                                # On other pid's only replace minimum time and assoc pid if that
                                # process has a smaller brust time than the current smallest
                                if (not i == 1) and (pcb.tburst[0] < mintime):
                                        mintime = pcb.tburst[0]
                                        minpid = pid
                # Return the pid stored in minpid
                index = self.pq.index(minpid)
                return self.pq[index]

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
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
                else:
                        return None
		
# Highest response ratio next - calculate response ratio for each process and 
#								choose the one with the highest
class HRRN:
        preempt = False # Is the algorithm preemptive?

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                self.pq = [] # Process Queue
                self.tmax = 200 # Max time between flushes
                self.tflush = 0 # Accumulated time since last flush
                
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
                # Loop through process queue
                for pid in self.pq:
                        i = i + 1
                        pcb = self.pt.GetPCB(pid)
                        # Calculate the total required run time from pcb
                        for j in range(0,ceil(len(pcb.tburst)/2)):
                                sumtime = sumtime + pcb.tburst(2*j)
                        # Calculate response ratio
                        respratio = 1 + pcb.twait/sumtime
                        # Choose processes that are ready
                        if pcb.state == 1:
                                # Record the first CPU burst time and pid on first iteration
                                if i == 1:
                                        maxrr = respratio
                                        maxpid = pid
                                # On other pid's only replace minimum time and assoc pid if that
                                # process has a smaller brust time than the current smallest
                                if (not i == 1) and (respratio > maxrr):
                                        maxrr = respratio
                                        maxpid = pid
                # Pop the pid stored in minpid
                index = self.pq.index(maxpid)
                return self.pq[index]

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
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
                else:
                        return None
