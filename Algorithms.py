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
	tmax = 42 # Max time between flushes
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
		return self.pq[0]

	# Return first instance of cpu burst time from the PCB of current process
	def Run(self, currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime

	# Increment flush time and decide if queue needs to be flushed
	def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush > tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                elif:
                        return None
                                
	

# Round robin - retrieve item from top of queue, process for a time, 
# then return to queue unless finished
class RR:
	pq = [] # Process Queue
	pt = Processes.ProcTbl() # Process Table
	preempt = True # Is the algorithm preemptive?
	tq = 1 # Time Quantum
	tmax = 42 # Max time between flushes
        tflush = 0 # Accumulated time since last flush
	
	# Constructor
	def __init__(self, proctbl, timeq):
		self.pt = proctbl
		self.tq = timeq
		
	# InsertPID process into queue
	def InsertPID(self, pid):
		self.pq.append(pid)

	# Remove process from queue
	def RemovePID(self, procid):
                self.pq.remove(procid)
			
	# Get next pid to be run
	def NextPID(self, currentlyrunning):
		# Pop the next PID in the list
		return self.pq[0]
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self,currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		remainingtime = pt.pcb(index).tburst[0]
		if remainingtime < tq:
			remainingtime = pt.pcb(index).tburst.pop(0)
			runtime = remainingtime
		else:
			runtime = tq
			pt.pcb(index).tburst[0] = pt.pcb(index).tburst[0] - tq
			self.InsertPID(currentlyrunning)
		return runtime

	# Increment flush time and decide if queue needs to be flushed
	def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush > tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                elif:
                        return None
		
# Shortest process next - retrieve item with shortest process time
class SPN:
	pq = [] # Process Queue
	pt = Processes.ProcTbl() # Process Table
	preempt = False # Is the algorithm preemptive?
	tmax = 42 # Max time between flushes
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
		for pid in pq:
			i = i + 1
			proccontblk = self.pt.GetPCB(pid)
			# Record the first CPU burst time and pid on first iteration
			if i == 1:
				mintime = proccontblk.tburst[0]
				minpid = pid
			# On other pid's only replace minimum time and assoc pid if that
			# process has a smaller brust time than the current smallest
			if not i == 1 and proccontblk.tburst[0] < mintime:
				mintime = proccontblk.tburst[0]
				minpid = pid
		# Pop the pid stored in minpid
		index = self.pq.index(minpid)
		return self.pq[index]
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self,currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime

	# Increment flush time and decide if queue needs to be flushed
	def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush > tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                elif:
                        return None
				
			
# Shortest remaining time - retrieve item with shortest process time
# 							except preempt if incoming process is shorter
class SRT:
	pq = [] # Process queue
	pt = Processes.ProcTbl() # Process Table
	preempt = True # Is the algorithm preemptive?
	tmax = 42 # Max time between flushes
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
		for pid in pq:
			i = i + 1
			proccontblk = self.pt.GetPCB(pid)
			# Record the first CPU burst time and pid on first iteration
			if i == 1:
				mintime = proccontblk.tburst[0]
				minpid = pid
			# On other pid's only replace minimum time and assoc pid if that
			# process has a smaller brust time than the current smallest
			if (not i == 1) and (proccontblk.tburst[0] < mintime):
				mintime = proccontblk.tburst[0]
				minpid = pid
		# Pop the pid stored in minpid
		index = self.pq.index(minpid)
		return self.pq[index]
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self,currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime

	# Increment flush time and decide if queue needs to be flushed
	def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush > tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                elif:
                        return None
		
# Highest response ratio next - calculate response ratio for each process and 
#								choose the one with the highest
class HRRN:
	pq = [] # Process queue
	pt = Processes.ProcTbl() # Process Table
	preempt = False # Is the algorithm preemptive?
	tmax = 42 # Max time between flushes
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
		for pid in pq:
			i = i + 1
			proccontblk = self.pt.GetPCB(pid)
			for j in range(0,ceil(len(proccontblk.tburst)/2)):
				sumtime = sumtime + proccontblk.tburst(2*j)
			respratio = 1 + proccontblk.twait/sumtime
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
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime

	# Increment flush time and decide if queue needs to be flushed
	def Flush(self, runtime):
                self.tflush += runtime
                # Flush top 10 processes from queue if particular time elapsed
                if self.tflush > tmax:
                        tenprocesses = []
                        for a in range(0,9):
                                tenprocesses.append(self.pq[a])
                                self.pq.pop(a)
                        return tenprocesses
                elif:
                        return None
