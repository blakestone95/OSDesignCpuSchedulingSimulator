# Execute and loop function need work
# An IO queue needs to be created for the processor to hand processes.
# Processes might need to have the processslot associated with them

class CPU:

    #Initialize process table to the same address as a passed variable
    def __init__(self,ProcTbl):
        self.ProcTbl = ProcTbl
        #Initialize Variables
        self.state = "idle"      #State of processor
        self.twait = 0           #Time processor is idle
        self.tactive = 0         #Time processor is runnings
        self.pid = 0
        self.processingtime = 0  #Time spent processing (needed for RR)
        self.processtime = 0     #Counter for processor to increment to burst time
        self.currentq = -1        #Store current queue processing from (-1 means none)

    #Set processor to execute a specified process from the pid
    def Execute(self,pid,runtime,qlvl):
        self.pid = pid
        self.processtime = runtime
        self.processingtime = 0
        self.currentq = qlvl
        pcb = self.ProcTbl.GetPCB(pid)
        pcb.state = 2
        self.state = "running"   #Set processor to running state

    # Stop processing and return the pid and remaining time for that process
    def Halt(self):
        pcb = self.ProcTbl.GetPCB(self.pid)
        pcb.state = 1
        # Get pid and remaining time before CPU is reset
        pid = self.pid
        pt = self.processtime
        # Reset CPU
        self.state = "idle"
        self.pid = 0
        self.processingtime = 0
        self.processtime = 0
        self.currentq = -1
        return [pid,pt]

    #Return processor usage value
    def Usage(self):
        return tactive/(tactive+twait)
    ''' Don't need these, we can access class variables directly
    def getstate(self):
        return self.state

    def currentruntime(self):
        return self.processtime
    '''
    def DecrementTime(self,subtime):
        if self.state == "running":
            pcb = self.ProcTbl.GetPCB(self.pid)
            pcb.state = 2
            self.tactive += subtime
            self.processtime -= subtime
            self.processingtime += subtime
            # If process finised reset CPU
            if self.processtime == 0:
                # Retrieve finished pid
                pid = self.pid
                # Reset
                self.state = "idle"
                self.pid = 0
                self.processingtime = 0
                self.processtime = 0
                self.currentq = -1
                return self.pid
            # Error
            elif self.processtime < 0:
                print("error CPU time < 0")
        # If processor is idle, add to the cpu wait time
        elif self.state == "idle":
            self.twait += subtime
            #print("error can't decrement, CPU is idle")
        
        return 0

    #Loop function to regularly update cpu state
    #Don't think we need this
    """def loop(self):
        if state == "running":
            self.tactive += 1       #Increment active time
            self.processtime += 1   #Increment burst time and check if it is the final value
            if (self.processtime == PCB.tburst[self.processslot]):
                if self.processslot/2 < (len(PCB.tburst)-1)/2:    #Move to the next burst slot if it exists
                    self.processslot += 2
                    state = "idle"       #Processor goes into blocked state since next slot is IO
        else:
            self.twait += 1         #If processor is not running increment wait time"""
