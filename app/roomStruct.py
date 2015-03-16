# -*- coding: utf-8 -*-

class Arrange:
    def __init__(self):
        self.name = ''
        self.left = 0
        self.right = 0
        self.kind = 0
    def IsIn(self,i):
        return self.left <= i <= self.right
        
class Room:
    def __init__(self):
        self.name = ''
        self.area = 0
        self.area2 = 0
        self.courses = [[],[],[],[],[],[],[]] #固定安排
        self.applys = [{},{},{},{},{},{},{}] #申请
    def __str__(self):
        return self.name
    def GetDayArrange(self,i):
        #return Arrage()
        for c in self.courses[i]:
            #return an Arrange List
            yield c
        for c in self.applys[i].values():
            yield c
            
    def GetDayApply(self,i):
        for c in self.applys[i].values():
            yield c
    
    def GetTimeArrange(self,i,st,en):
        res = []
        for c in self.GetDayArrange(i):
            for t in range(st,en,10):
                if c.IsIn(t):
                    res.append(c)
                    break
                    
        return res
            
    def PushDayCourse(self,i,a):
        self.courses[i] += a
        
    def PushDayApply(self,i,a,name):
        self.applys[i][name] = a
    def IsValid(self,d,st,en):
        #暂时用暴力法
        for c in self.GetDayArrange(d):
            for t in range(st,en,10):
                if c.IsIn(t):
                    return False
        return True
        
    def GetKindScore(self,d,st,en,kind):
        #暂时用暴力法,分数越小越好,注意：这里的t步进会使同一时间段加很多分
        sum = 0
        for c in self.GetDayArrange(d):
            for t in range(st,en,10):
                if c.IsIn(t):
                    if c.kind == kind:
                        sum += 10
                    else:
                        sum += 3
        return sum
        
    def GetNearTime(self,d,st,en):
        #得到附近最大区间
        left = 8 * 60
        right = 22*60 + 30
        for c in self.GetDayArrange(d):
            if c.right < st and c.right > left:
                left = c.right
            if c.left > en and c.left < right:
                right = c.left
        return [left,right]
        
    def PeopleScore(self,p):
        c = (p-self.area)
        if -10<=c<=30:
            return 100-abs(c)*0.1
        if c < -10:
            return c
        #c>30
        return 80-c
        

        
class RoomS():
    def __init__(self,name,score):
        #Room.__init__(self)
        self.name = name
        self.score = score
    def __lt__(self,other):
        return self.score < other.score
        
def Int2Time(t):
    h = t/60
    m = t%60
    return '%02d:%02d'%(h,m)
    
def Time2Int(s):
    try:
        p = s.split(':')
        h = int(p[0])
        m = int(p[1])
        return h*60 + m
    except:
        return 0