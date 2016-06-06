# Execute and loop function need work
# An IO queue needs to be created for the processor to hand processes.
# Processes might need to have the processslot associated with them

class CPU:
    #Initialize Variables
    state = "idle"      #State of processor
    twait = 0           #Time processor is idle
    tactive = 0         #Time processor is runnings
    pid = 0
    processingtime = 0  #Time spent processing (needed for RR)
    processtime = 0     #Counter for processor to increment to burst time
    currentq = -1        #Store current queue processing from (-1 means none)
    #ProcTbl = None      #Process table 

    #Initialize process table to the same address as a passed variable
    #def __init__(self,ProcTbl):
    #    self.ProcTbl = ProcTbl

    #Set processor to execute a specified process from the pid
    def Execute(self,pid,runtime,qlvl):
        self.pid = pid
        self.processtime = runtime
        self.processingtime = 0
        self.currentq = qlvl
        state = "running"   #Set processor to running state

    #Set processor to execute a specified process from the pid
    def Halt(self):
        state = "idle"   #Set processor to running state
        self.processingtime = 0
        self.currentq = -1
        return [self.pid,self.processtime]

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
        if state == "running":
            self.tactive += subtime
            self.processtime -= subtime
            self.processingtime += subtime
            if self.processtime == 0:
                self.state = "idle"
                self.currentq = -1
                return self.pid
            elif self.processtime < 0:
                print("error CPU time < 0")
        elif state == "idle":
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
