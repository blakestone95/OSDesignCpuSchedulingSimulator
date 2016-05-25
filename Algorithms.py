# Algorithms.py
# Author: Blake Sawyer
# 
# Create classes for CPU scheduling algorithms
# For now, I am doing the basic idea of each. 
# These classes will evolve as the project comes together
# Really though, I don't know what I am doing...
import Processes

# First come first serve - retrieve item from the top of the queue
class FCFS:
	pq = [] # Process Queue
	
	def __init__(self, procqueue):
		self.pq = procqueue
	
	def Insert(self, pid):
		self.pq.append(pid)
		
	def NextPID(self):
		return self.pq.pop(1)
		
# Round robin - retrieve item from top of queue, process for a time, 
# then return to queue unless finished
class RR:
	pq = [] # Process Queue
	tq = 1 # Time Quantum
	
	def __init__(self, procqueue, timeq):
		self.pq = procqueue
		self.tq = timeq
		
	def Insert(self, pid):
		self.pq.append(pid)
		
	def NextPID(self, currentlyrunning):
		# Pop the next PID in the list
		# only insert if currently running proc hasn't finished
		self.Insert(currentlyrunning)
		return self.pq.pop(1)
		
# Shortest process next - retrieve item with shortest process time
class SPN:
	pq = [] # Process Queue
	
	def __init__(self, procqueue):
		self.pq = procqueue
		
	def Insert(self, pid):
		self.pq.append(pid)
		
	# Find minimum process time needed
	def NextPID(self, proctable):
		i = 0
		# Loop through process queue
		for pid in pq:
			i = i + 1
			proccontblk = proctable.GetPCB(pid)
			# Record the first CPU burst time and pid on first iteration
			if i == 1:
				mintime = proccontblk.tburst[1]
				minpid = pid
			# On other pid's only replace minimum time and assoc pid if that
			# process has a smaller brust time than the current smallest
			if not i == 1 and proccontblk.tburst[1] < mintime:
				mintime = proccontblk.tburst[1]
				minpid = pid
		# Pop the pid stored in minpid
		index = self.pq.index(minpid)
		return self.pq.pop(index)
				
			
# Shortest remaining time - retrieve item with shortest process time
# 							except preempt if incoming process is shorter
class SRT:
	pq = [] # Process queue
	
	def __init__(self, procqueue):
		self.pq = procqueue
		
	def Insert(self, pid):
		self.pq.append(pid)
		
	# Find minimum process time needed
	def NextPID(self, proctable):
		i = 0
		# Loop through process queue
		for pid in pq:
			i = i + 1
			proccontblk = proctable.GetPCB(pid)
			# Record the first CPU burst time and pid on first iteration
			if i == 1:
				mintime = proccontblk.tburst[1]
				minpid = pid
			# On other pid's only replace minimum time and assoc pid if that
			# process has a smaller brust time than the current smallest
			if not i == 1 and proccontblk.tburst[1] < mintime
				mintime = proccontblk.tburst[1]
				minpid = pid
		# Pop the pid stored in minpid
		index = self.pq.index(minpid)
		return self.pq.pop(index)
		
# Highest response ratio next - calculate response ratio for each process and 
#								choose the one with the highest
class HRRN:
	pq = [] # Process queue
	
	def __init__(self, procqueue):
		self.pq = procqueue
		
	def Insert(self, pid):
		self.pq.append(pid)
		
	# Find highest response ratio
	def NextPID(self, proctable):
		i = 0
		# Loop through process queue
		for pid in pq:
			i = i + 1
			proccontblk = proctable.GetPCB(pid)
			respratio = 1 + proccontblk.twait/sum(proccontblk.cpuburst)
			# Record the first CPU burst time and pid on first iteration
			if i == 1:
				maxrr = respratio
				maxpid = pid
			# On other pid's only replace minimum time and assoc pid if that
			# process has a smaller brust time than the current smallest
			if not i == 1 and respratio > maxrr
				maxrr = respratio
				maxpid = pid
		# Pop the pid stored in minpid
		index = self.pq.index(maxpid)
		return self.pq.pop(index)
