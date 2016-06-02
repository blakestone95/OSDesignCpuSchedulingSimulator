# Algorithms.py
# Author: Blake Sawyer
# 
# Classes for CPU scheduling algorithms
import Processes
#import Queue

# We will probably need some IO wait queue

# First come first serve - retrieve item from the top of the queue
class FCFS:
	pq = [] #queue.Queue() # Process Queue
	pt = ProcTbl() # Process Table

	# Constructor
	def __init__(self, procqueue, proctbl):
		self.pq = procqueue
		self.pt = proctbl

	# Insert process into queue
	def Insert(self, pid):
		self.pq.append(pid)

	# Get next pid to be run and remove it from the queue
	def NextPID(self):
	#return pq.get()
		return self.pq.pop(0)

	# Return first instance of cpu burst time from the PCB of current process
	def Run(self, currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime

# Round robin - retrieve item from top of queue, process for a time, 
# then return to queue unless finished
class RR:
	pq = [] # Process Queue
	pt = ProcTbl() # Process Table
	tq = 1 # Time Quantum
	
	# Constructor
	def __init__(self, procqueue, proctbl, timeq):
		self.pq = procqueue
		self.pt = proctbl
		self.tq = timeq
		
	# Insert process into queue
	def Insert(self, pid):
		self.pq.append(pid)
			
	# Get next pid to be run and remove it from the queue
	def NextPID(self, currentlyrunning):
		# Pop the next PID in the list
		return self.pq.pop(0)
		
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
			self.Insert(currentlyrunning)
		return runtime
		
# Shortest process next - retrieve item with shortest process time
class SPN:
	pq = [] # Process Queue
	pt = ProcTbl() # Process Table
	
	# Constructor
	def __init__(self, procqueue, proctbl):
		self.pq = procqueue
		self.pt = proctbl
		
	# Insert process into queue
	def Insert(self, pid):
		self.pq.append(pid)
		
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
		return self.pq.pop(index)
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self,currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime
				
			
# Shortest remaining time - retrieve item with shortest process time
# 							except preempt if incoming process is shorter
class SRT:
	pq = [] # Process queue
	pt = ProcTbl() # Process Table
	
	# Constructor
	def __init__(self, procqueue, proctbl):
		self.pq = procqueue
		self.pt = proctbl
		
	# Insert process into queue
	def Insert(self, pid):
		self.pq.append(pid)
		
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
		return self.pq.pop(index)
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self,currentlyrunning):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime
		
# Highest response ratio next - calculate response ratio for each process and 
#								choose the one with the highest
class HRRN:
	pq = [] # Process queue
	pt = ProcTbl() # Process Table
	
	# Constructor
	def __init__(self, procqueue, proctbl):
		self.pq = procqueue
		self.pt = proctbl
		
	# Insert process into queue
	def Insert(self, pid):
		self.pq.append(pid)
		
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
		return self.pq.pop(index)
		
	# Return first instance of cpu burst time from the PCB of current process
	def Run(self):
		index = self.pq.index(currentlyrunning)
		# Retrieve the cpu burst time
		runtime = pt.pcb(index).tburst.pop(0)
		return runtime
