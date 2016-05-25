# Processes.py
# Author: Blake Sawyer
#
# Create process table and PCB
import csv

class PCB:
	pid = 1
	state = 1 # 1 -> ready; 2 -> running; 3 -> blocked; 4 -> finished
	tarr = 0
	twait = 0
	qlvl = 1 # May remove later
	tburst = []
	
	def __init__(self, processid, currstate, timearr, timewait, queuelvl, timeburst):
		# Constructor
		self.pid = processid
		self.state = currstate
		self.tarr = timearr
		self.twait = timewait
		self.qlvl = queuelvl
		self.tburst = timeburst
	
	def LoadProcess(self, filelocation):
		# Assume file is csv
		with open(filelocation) as csvfile:
			procreader = csv.reader(csvfile, delimiter=',')
			
		
	
class ProcTbl:
	pid = []
	pcb = []
	
	def __init__(self):
		self.pid = []
	
	# Create process control block with pid, arrival time, and burst time array
	# pid array and pcb arrays will match indexes
	def Insert(self, procid, currtime, timeburst):
		proc = PCB(procid,1,currtime,0,1,timeburst)
		self.pid.append(procid)
		self.pcb.append(proc)
	
	# Remove process and assoc PCB from process table
	def Delete(self, procid):
		i = self.pid.index(procid)
		self.pid.pop(i)
		self.pcb.pop(i)
		
	def GetPCB(self, procid):
		i = self.pid.index(procid)
		return self.pcb[i]
