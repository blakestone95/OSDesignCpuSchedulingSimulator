class throughput:
        def __init__(self):
                self.times = []
                
        def addtime(self,thru):
                self.times.append(sum(thru)/len(thru))
                
        def totaltime(self,queueslist):
                i = 0
                x = []
                for a in self.times:
                        x.append([queueslist[i],a])
                        i += 1
                return x
                #return sum(self.times)/len(self.times)

#Do this to start
#example = turnaroundtime()

#Do this for each process
#example.addtime(tarr,tfin)

#Do this at the end
#averageturnaroundtime = example.totaltime(length)

class turnaroundtime:
        def __init__(self):
                self.times = []

        def addtime(self,tarr,tfin):
                self.times.append(tfin - tarr)

        def totaltime(self):
                return sum(self.times)/len(self.times)

#Do this to start
#example = waittime()

#Do this for each process
#example.addtime(tarr,tfin,tburst)

#Do this at the end
#averagewaittime = example.totaltime(length)

class waittime:
        def __init__(self):
                self.times = []

        def addtime(self,tarr,tfin,tburstsum):
                self.times.append((tfin - tarr) - tburstsum)
                
        def addtime(self,twait):
                self.times.append(twait)

        def totaltime(self):
                return sum(self.times)/len(self.times)


#Do this to start
#example = responsetime()

#Do this for each process
#example.addtime(trep)

#Do this at the end
#averageresponsetime = example.totaltime(length)

class responsetime:
        def __init__(self):
                self.times = []

        def addtime(self,trep):
                self.times.append(trep)

        def totaltime(self):
                return sum(self.times)/len(self.times)

