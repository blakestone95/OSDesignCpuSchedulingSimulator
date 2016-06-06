# Algorithms.py
# Author: Blake Sawyer
# 
# Classes for CPU scheduling algorithms
import Processes

# First come first serve - retrieve item from the top of the queue
class FCFS:
        pq = [] # Process Queue
        pt = Processes.ProcTbl() # Process Table
        preempt = False # Is the algorithm preemptive?
        tmax = 200 # Max time between flushes
        tflush = 0 # Accumulated time since last flush

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl

        # InsertPID process into queue
        def InsertPID(self, pid):
                self.pq.append(pid)

        # Remove process from queue
        def RemovePID(self, procid):
                self.pq.remove(procid)

        # Get next pid to be run
        def NextPID(self):
                i = 0
                pcb = self.pt.GetPCB(self.pq[i])
                # Get first non-running process
                while not pcb.state == 1:
                        i += 1
                        pcb = self.pt.GetPCB(self.pq[i])
                return self.pq[i]

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                # OK to be over flush time
                if self.tflush > self.tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                else:
                        return None
                                
	

# Round robin - retrieve item from top of queue, process for a time, 
# then return to queue unless finished
class RR:
        pq = [] # Process Queue
        pt = Processes.ProcTbl() # Process Table
        preempt = True # Is the algorithm preemptive?
        lastpid = 0 # Store the last pid that was returned from NextPID
        tq = 1 # Time Quantum
        tmax = 50 # Max time between flushes
        tflush = 0 # Accumulated time since last flush

        # Constructor
        def __init__(self, proctbl, timeq):
                self.pt = proctbl
                self.tq = timeq
                # only flush queue if 20 processed have been serviced
                self.tmax = timeq*20
                
        # InsertPID process into queue
        def InsertPID(self, pid):
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
        def NextPID(self,currentlyrunning,runtime):
                if currentlyrunning == 0:
                        self.lastpid = self.pq[0]
                        return self.lastpid
                index = self.pq.index(currentlyrunning)
                # Return self if not needing replacement
                if runtime < self.tq:
                        self.lastpid = self.pq[index]
                        return self.lastpid
                # Return next ready process if does need replacement
                else:
                        pcb = self.pt.GetPCB(self.pq[index])
                        # Get first non-running process
                        while not pcb.state == 1:
                                index += 1
                                pcb = self.pt.GetPCB(self.pq[i])
                        self.lastpid = self.pq[index]
                        return self.lastpid

        # Increment flush time and decide if queue needs to be flushed
        def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush > self.tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                else:
                        return None
		
# Shortest process next - retrieve item with shortest process time
class SPN:
        pq = [] # Process Queue
        pt = Processes.ProcTbl() # Process Table
        preempt = False # Is the algorithm preemptive?
        tmax = 200 # Max time between flushes
        tflush = 0 # Accumulated time since last flush

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                
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
                # Loop through process queue
                for pid in self.pq:
                        i += 1
                        pcb = self.pt.GetPCB(pid)
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
                if self.tflush > self.tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                else:
                        return None
				
			
# Shortest remaining time - retrieve item with shortest process time
# 							except preempt if incoming process is shorter
class SRT:
        pq = [] # Process queue
        pt = Processes.ProcTbl() # Process Table
        preempt = True # Is the algorithm preemptive?
        tmax = 200 # Max time between flushes
        tflush = 0 # Accumulated time since last flush

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                
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
                if self.tflush > self.tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                else:
                        return None
		
# Highest response ratio next - calculate response ratio for each process and 
#								choose the one with the highest
class HRRN:
        pq = [] # Process queue
        pt = Processes.ProcTbl() # Process Table
        preempt = False # Is the algorithm preemptive?
        tmax = 200 # Max time between flushes
        tflush = 0 # Accumulated time since last flush

        # Constructor
        def __init__(self, proctbl):
                self.pt = proctbl
                
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
                if self.tflush > self.tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                else:
                        return None
