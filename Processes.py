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
	tburst = [0]
	
	def __init__(self, processid, currstate, timearr, timewait, queuelvl, timeburst)
		# Constructor
		self.pid = processid
		self.state = currstate
		self.tarr = timearr
		self.twait = timewait
		self.qlvl = queuelvl
		self.tburst = timeburst
	
	def LoadProcess(self, filelocation)
		# Assume file is csv
		with open(filelocation) as csvfile:
			procreader = csv.reader(csvfile, delimiter=',')
			
		
	
class ProcTbl:
	pid = []
	
	def __init__(self, processid)
		self.pid = processid
	
	def 
	
