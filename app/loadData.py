# -*- coding: utf-8 -*-
import xlrd
from roomStruct import *

def GetAR(q):
    st = 0
    res = []
    for i in range(len(q)):
        if q[i:i+2] == '],':
           c = q[st:i]#不包括右括号
           l = c.index('[')
           w = c.index(',')
           #r = c.index(']')
           a = Arrange()
           a.name = c[0:l]
           a.left = Time2Int(c[l+1:w])
           a.right= Time2Int(c[w+1:])
           res.append(a)
           st = i+2
    return res
    
def LoadRoomData():
    data = xlrd.open_workbook('data.xls')
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    
    roomData = {}
    
    for i in range(1,nrows):
        name = table.cell_value(i,0)
        r = Room()
        r.name = name
        size = table.cell_value(i,1)
        m = size.index('/')
        r.area = int(size[0:m]) #容纳人数
        r.area2 = int(size[m+1:]) #考位
        for d in range(7):
            q = table.cell_value(i,3+d)
            ar = GetAR(q)
            q2 = table.cell_value(i,12+d)
            ar2 = GetAR(q2)
            r.PushDayCourse(d,ar)
            r.PushDayCourse(d,ar2)
            
        roomData[name] = r
    return roomData