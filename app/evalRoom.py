# -*- coding: utf-8 -*-
from loadData import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

#到时候可以把时间等资料封装
def ExistRoom(roomsData,name):
    #print name,roomData.has_key(name)
    return roomsData.has_key(name)
    
def GetLRRoom(roomsData,name,co):
    #以name为中心
    #res = []
    c = name[0]
    id = int(name[1:])
    for i in range(id-1,id+2):
        y  = c + '%03d'%i
        if ExistRoom(roomsData,y):
            s = (abs(id-i) * (-0.2) + 1)*co  #0.8,1
            yield (y,s)
            #res.append((y,s))
    #return res
    
def GetUDRoom(roomsData,name,co):
    #res = []
    c = name[0]
    f = int(name[1])
    back = name[2:]
    for i in range(f-1,f+2):
        y = c + '%d'%i + back
        if ExistRoom(roomsData,y):
            s = (abs(f-i)*(-0.3) + 1)*co
            yield (y,s)
            #res.append((y,s))
    #return res

def GetNearRooms(roomsData,name):
    #九宫格模式,除了中间一格
    #res = []
    for c in GetUDRoom(roomsData,name,1.0):
        for q in GetLRRoom(roomsData,c[0],c[1]): 
            if q[0] != name:
                yield q
        #res += GetLRRoom(roomData,c[0],c[1])
    #return res

def GetFourRooms(roomsData,name):
    for q in GetLRRoom(roomsData,name,1.0):
        if q[0] != name:
            yield q
    for q in GetUDRoom(roomsData,name,1.0):
        if q[0] != name:
            yield q
            
def EvalRoom(roomsData,name,d,st,en,kind):
    #分数越低越前
    sum = 0
    for q in GetNearRooms(roomsData,name):
        co = 1
        near = roomsData[q[0]].GetNearTime(d,st,en)
        h = (en - st) *1.0 /(near[1] - near[0])
        sum += roomsData[q[0]].GetKindScore(d,st,en,kind) * q[1] * 0.7 + h * 100.0 * 0.3
    return sum
    
def RoomDetail(roomsData,name,d,st,en):
    room = roomsData[name]
    res = [ room.name + "课室",
                "课室大小：可容纳" + str(room.area) + "人",
                "具有可移动桌椅，多媒体",
                "请务必提前一天申请",
                "",
                "周围环境:"
             ]
    for q in GetFourRooms(roomsData,name):
        r = roomsData[q[0]]
        k = r.GetTimeArrange(d,st,en)
        if len(k) > 0:
            text = r.name + '课室:     '
            for a in k:
                text += a.name + '     ' + Int2Time(a.left) + ' ~ ' + Int2Time(a.right)
            res.append(text)
        else:
            res.append(r.name + '课室空闲')
    return res