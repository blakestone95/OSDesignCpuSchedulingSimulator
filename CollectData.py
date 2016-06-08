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

        def totaltime(self,length):
                return sum(self.times)/length

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

        def totaltime(self,length):
                return sum(self.times)/length


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

        def totaltime(self,length):
                return sum(self.times)/length

