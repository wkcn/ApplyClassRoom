# -*- coding: utf-8 -*-
from evalRoom import *

def GetValidRooms(roomsData,d,st,en):
    res = []
    for r in roomsData.values():
        if r.IsValid(d,st,en):
            res.append(r)
    return res

def GetTwoKindRooms(roomsData,list,people):
    #��������������ֿ���
    li = [[],[]]
    for c in list:
        if c.PeopleScore(people) >= 100:
            li[0].append(c)
        else:
            li[1].append(c)
    return li
    
def SelectRooms(roomsData,d,st,en,people,kind):
    '''
    while True:
       print '������������ҵ�ʱ��(���ڼ�,��ʼʱ��,����ʱ��), ���� 2,14:30,15:30'
        s = raw_input()
        
        s = '2,14:30,15:30'
        people = 80
        kind = 0#ѧϰ��
        
        d = int(s[0])
        st = Time2Int(s[2:+2+5])
        en = Time2Int(s[8:8+5])
        #print st,en
    '''
    li = GetValidRooms(roomsData,d,st,en) # liΪһ���б�
    #for u in li:
    #    print u.name
    #for u in roomsData['A202'].courses[d]:
    #   print u.name
    twoList = GetTwoKindRooms(roomsData,li,people) #��������

    result = []
    for i in twoList[0]:
        e = RoomS(i.name,EvalRoom(roomsData,i.name,d,st,en,kind))
        result.append(e)
    result.sort()
    tempList = []
    for i in twoList[1]:
        e = RoomS(i.name,EvalRoom(roomsData,i.name,d,st,en,kind))
        tempList.append(e)
    tempList.sort()
    result += tempList
        
    return result
