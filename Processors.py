# Execute and loop function need work
# An IO queue needs to be created for the processor to hand processes.
# Processes might need to have the processslot associated with them

class CPU:
    #Initialize Variables
    state = "idle"      #State of processor
    twait = 0           #Time processor is idle
    tactive = 0         #Time processor is running
    processtime = 0     #Counter for processor to increment to burst time
    processslot = 0     #Place holder for burst time in list
    ProcTbl = None      #Process table 

    #Initialize process table to the same address as a passed variable
    def __init__(self,ProcTbl):
        self.ProcTbl = ProcTbl

    #Set processor to execute a specified process from the pid
    def execute(self,pid):
        index = self.ProcTbl.pid.index(pid)     #Get address of process in table
        PCB = self.ProcTbl.pcb[index]           #Get pcb from process table

        #Set process burst time to first in list
        self.processslot = 0
        self.processtime = 0
        state = "running"   #Set processor to running state

    #Return processor usage value
    def usage(self):
        return tactive/(tactive+twait)

    #Loop function to regularly update cpu state
    def loop(self):
        if state == "running":
            self.tactive += 1       #Increment active time
            self.processtime += 1   #Increment burst time and check if it is the final value
            if (self.processtime == PCB.tburst[self.processslot]):
                if self.processslot/2 < len(PCB.tburst)-1)/2:    #Move to the next burst slot if it exists
                    self.processslot += 2
                    state = "blocked"       #Processor goes into blocked state since next slot is IO
        else:
            self.twait += 1         #If processor is not running increment wait time
