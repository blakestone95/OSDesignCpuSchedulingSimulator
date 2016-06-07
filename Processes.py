# Processes.py
# Author: Blake Sawyer
#
# Create process table and PCB
import csv

# Process Control Block - Store information associated with processes
class PCB:
	pid = 1
	state = 1 # 1 -> ready; 2 -> running; 3 -> blocked; 4 -> finished
	tarr = 0
	twait = 0
	tfinish = 0
	qlvl = 1 # May remove later
	tburst = []
	
	# Constructor needs only process id and tburst array, other args are optional
	def __init__(self, processid, timeburst, timearr = None, currstate = None, timewait = None, queuelvl = None):
		
		self.pid = processid
		
		if currstate is None:
			self.state = 1
		else:
			self.state = currstate
			
		if timearr is None:
			self.tarr = 0
		else:
			self.tarr = timearr
			
		if timewait is None:
			self.twait = 0
		else:
			self.twait = timewait
			
		if queuelvl is None:
			self.qlvl = 1
		else:
			self.qlvl = queuelvl
			
		self.tburst = timeburst
			
		
# Process Table - Store current processes and their associated PCB
class ProcTbl:
	pid = []
	pcb = []
	
	# Construct PT to empty lists
	def __init__(self):
		self.pid = []
		self.pcb = []
	
	# Create process control block with pid, arrival time, and burst time array
	# pid array and pcb arrays will match indexes
	def Insert(self, procid, timeburst, currtime = None):
		if currtime is None:
			proc = PCB(procid,timeburst)
		else:
			proc = PCB(procid,timeburst,currtime)
		self.pid.append(procid)
		self.pcb.append(proc)
	
	# Remove process and assoc PCB from process table
	def Delete(self, procid):
		i = self.pid.index(procid)
		self.pid.pop(i)
		self.pcb.pop(i)

        # Return next pid in the process table (for keeping track of next process)
        # Doesn't delete elements unlike similarly named functions in Algorithms
	def NextPID(self, procid):
                i = self.pid.index(procid)
                if i == len(self.pid) - 1:
                        return None
                else:
                        return self.pid[i+1]
		
	# Retrieve the PCB associated with a particular process id
	def GetPCB(self, procid):
		i = self.pid.index(procid)
		return self.pcb[i]
