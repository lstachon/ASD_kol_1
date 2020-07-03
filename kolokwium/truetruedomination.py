class punkt:
    def __init__(self,xval,yval):
        self.punkt = (xval,yval)


class toblerone:
    def __init__(self,sizer):
        self.table =[None for i in range(sizer)]
        self.curr = 0

    def add(self,xer,yger):
        new = punkt(xer,yger)
        self.table[self.curr]=new
        self.curr+=1

    def printer(self):
        for i in range(len(self.table)):
            x , y = self.table[i].punkt
            print(x,y)


def domination(t):
    # 2 * n log n
    t.table.sort(key=lambda tup: tup.punkt[0],reverse=True)
    t.table.sort(key=lambda tup: tup.punkt[1], reverse=True)
    t.printer()
    l =0
    i =0
    # n razy
    while (t.table[i].punkt[0]==t.table[i+1].punkt[0] or t.table[i+1].punkt[1]==t.table[i].punkt[1]) and i+2<len(t.table):
        l+=1
        i+=1

    if i+1<len(t.table) and t.table[i].punkt[0]>t.table[i+1].punkt[0] and t.table[i].punkt[1]>t.table[i+1].punkt[1]:
        l+=1
    else:
        l=0

    return l


stol = toblerone(6)
stol.add(1,1)
stol.add(3,3)
stol.add(2,2)
stol.add(2,1)
stol.add(4,3)
stol.add(4,4)



print(domination(stol))