#Do this to start
#example = turnaroundtime()

#Do this for each process
#example.addtime(tarr,tfin)

#Do this at the end
#averageturnaroundtime = example.totaltime()

class turnaroundtime:
        def __init__(self):
                self.times = []

        def addtime(self,tarr,tfin):
                self.times.append(tfin - tarr)

        def totaltime(self):
                return sum(self.times)

#Do this to start
#example = waittime()

#Do this for each process
#example.addtime(tarr,tfin,tburst)

#Do this at the end
#averagewaittime = example.totaltime()

class waittime:
        def __init__(self):
                self.times = []

        def addtime(self,tarr,tfin,tburstsum):
                self.times.append((tfin - tarr) - tburstsum)

        def totaltime(self):
                return sum(self.times)


#Do this to start
#example = responsetime()

#Do this for each process
#example.addtime(trep)

#Do this at the end
#averageresponsetime = example.totaltime()

class responsetime:
        def __init__(self):
                self.times = []

        def addtime(self,trep):
                self.times.append(trep)

        def totaltime(self):
                return sum(self.times)

