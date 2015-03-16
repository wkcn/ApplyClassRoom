# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy
import random


courese = ['����','�ߵ���ѧ','��ɢ��ѧ','������ͼ','�������','��ʷ','��ѧӢ��','���ۿ�','���ֵ�·','ģ���·','˼��','���＼��','����','ҽѧ','����','����','����']
activity = ['����','����','��ϰ','��ѡ','��ѡ2','��ѡ3','','']
#��ʽ������[08:00,08:45],
#ʱ�䣺8�㿪ʼ��45��һ��,10���ӿμ�ʱ�䣬��21:35
def GT(t):
    h = t/60
    m = t%60
    return '%02d:%02d'%(h,m)

def GetData(st,en,li):
    t = st
    text = ''
    while t < en:
        js = random.randint(-1,3)
        if js<=0:
            t += 45 + 10
            continue
        needTime = js * 45 + (js-1)*10
        leaveTime = en - t
        if leaveTime <45:
            break
        if leaveTime<needTime:
            needTime = leaveTime
        name = random.choice(li)
        temp = name + '[' + GT(t) + ',' + GT(t+needTime) + '],'
        t += needTime + 10
        if name == '':
            continue
        text += temp
    return text

data = xlrd.open_workbook('������Ϣ.xlsx')
table = data.sheet_by_index(0)
nrows = table.nrows
ncols = table.ncols

data2 = xlrd.open_workbook('������Ϣ.xlsx')#,formatting_info=True)
wb = copy(data2)
ws = wb.get_sheet(0)

for i in range(1,nrows):
    name = table.cell_value(i,0)
    for d in range(3,3+7):
        if not (d == 3 or d == 3+7-1):
            ws.write(i,d,GetData(8*60,18*60,courese))
            
        ws.write(i,d+9,GetData(19*60,21*60+35,activity))
        
wb.save('data.xls')